#!/usr/bin/env python3
"""
Script to download and cache Instagram images from the artwork data.
Downloads images at highest resolution and stores them in ./cache/ directory.
"""

import os
import re
import hashlib
import requests
from urllib.parse import urlparse
from pathlib import Path
import time
import json
from PIL import Image
from shutil import move
from liturgical_calendar.funcs import get_cache_filename

def get_instagram_image_url(instagram_url):
    """
    For Instagram post URLs, append '/media?size=l' to get the 640x640 image directly.
    """
    if 'instagram.com' in instagram_url:
        # Remove any trailing slash for consistency
        url = instagram_url.rstrip('/')
        return f"{url}/media?size=l"
    return None

def check_image_dimensions(image_path):
    """
    Check the dimensions of a downloaded image.
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except ImportError:
        # If PIL is not available, use file command
        import subprocess
        try:
            result = subprocess.run(['file', image_path], capture_output=True, text=True)
            if 'JPEG' in result.stdout:
                # Extract dimensions from file output
                import re
                match = re.search(r'(\d+)x(\d+)', result.stdout)
                if match:
                    return int(match.group(1)), int(match.group(2))
        except:
            pass
    except Exception as e:
        print(f"    Error checking image dimensions: {e}")
    
    return None, None

def download_image(image_url, cache_path, original_instagram_url=None):
    """
    Download an image from the given URL and save it to the cache path.
    """
    try:
        # Use a session to maintain cookies and headers
        session = requests.Session()
        
        # Comprehensive headers to look like a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        }
        
        # Add referrer if we have the original Instagram URL
        if original_instagram_url:
            headers['Referer'] = original_instagram_url
        
        session.headers.update(headers)
        
        print(f"    Downloading: {image_url}")
        response = session.get(image_url, timeout=30, stream=True)
        response.raise_for_status()
        
        with open(cache_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Check image dimensions
        width, height = check_image_dimensions(cache_path)
        if width and height:
            print(f"    Downloaded image: {width}x{height} pixels")
            if width >= 1080 or height >= 1080:
                print(f"    ✓ High resolution image downloaded")
            elif width >= 640 or height >= 640:
                print(f"    ⚠ Medium resolution image downloaded")
            else:
                print(f"    ⚠ Low resolution image downloaded")
        
        return True
        
    except Exception as e:
        print(f"    Error downloading image from {image_url}: {e}")
        return False

def extract_source_urls_from_feasts():
    """
    Extract all source URLs from the feasts object in artwork.py
    """
    source_urls = []
    
    try:
        # Import the feasts object from artwork.py
        from liturgical_calendar.artwork import feasts
        
        def extract_from_dict(data, path=""):
            """Recursively extract source URLs from nested dictionaries and lists"""
            if isinstance(data, dict):
                if 'source' in data and data['source']:
                    source_urls.append({
                        'url': data['source'],
                        'name': data.get('name', 'Unknown'),
                        'path': path
                    })
                for key, value in data.items():
                    extract_from_dict(value, f"{path}.{key}" if path else key)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    extract_from_dict(item, f"{path}[{i}]" if path else f"[{i}]")
        
        extract_from_dict(feasts)
        
    except ImportError as e:
        print(f"Error importing feasts from artwork.py: {e}")
        return []
    
    return source_urls

def upsample_if_needed(original_path, upsampled_path):
    """
    Move the original image to cache/original and upsample to 1080x1080 if needed, saving the upsampled image in cache/.
    """
    orig_dir = original_path.parent / "original"
    orig_dir.mkdir(exist_ok=True)
    orig_backup = orig_dir / original_path.name
    # Move the original image to cache/original
    move(str(original_path), str(orig_backup))
    with Image.open(orig_backup) as img:
        width, height = img.size
        if width < 1080 or height < 1080:
            print(f"    Upsampling {original_path.name} ({width}x{height}) to 1080x1080...")
            upsampled = img.resize((1080, 1080), Image.LANCZOS)
            upsampled.save(upsampled_path, quality=95)
        else:
            print(f"    Copying {original_path.name} ({width}x{height}) - already 1080 or larger.")
            img.save(upsampled_path, quality=95)

def main():
    """
    Main function to download and cache all artwork images.
    """
    print("Starting artwork image caching...")
    
    # Create cache directory
    cache_dir = Path("./cache")
    cache_dir.mkdir(exist_ok=True)
    print(f"Cache directory: {cache_dir.absolute()}")
    
    # Extract all source URLs
    source_entries = extract_source_urls_from_feasts()
    print(f"Found {len(source_entries)} source URLs in artwork data")
    
    # Track progress
    total_images = len(source_entries)
    cached_images = 0
    failed_images = 0
    skipped_images = 0
    failed_downloads = []  # List to record failed downloads
    
    # Process each source URL
    for i, entry in enumerate(source_entries, 1):
        source_url = entry['url']
        name = entry['name']
        path = entry['path']
        
        print(f"\n[{i}/{total_images}] Processing: {name} ({path})")
        print(f"  Source URL: {source_url}")
        
        # Generate cache filename
        cache_filename = get_cache_filename(source_url)
        cache_path = cache_dir / cache_filename
        
        # Check if already cached
        if cache_path.exists():
            print(f"  ✓ Already cached: {cache_filename}")
            skipped_images += 1
            continue
        
        # Extract actual image URL from Instagram
        if 'instagram.com' in source_url:
            print("  Extracting image URL from Instagram using /media?size=l...")
            image_url = get_instagram_image_url(source_url)
            if not image_url:
                print(f"  ✗ Failed to extract image URL")
                failed_images += 1
                failed_downloads.append({
                    'url': source_url,
                    'date': name,
                    'reason': 'Failed to extract image URL'
                })
                continue
        else:
            # For non-Instagram URLs, use the URL directly
            image_url = source_url
        
        print(f"  Downloading: {image_url}")
        
        # Download the image
        if download_image(image_url, cache_path, source_url):
            upsample_if_needed(cache_path, cache_path)
            print(f"  ✓ Downloaded and upsampled: {cache_filename}")
            cached_images += 1
        else:
            print(f"  ✗ Failed to download")
            failed_images += 1
            failed_downloads.append({
                'url': source_url,
                'date': name,
                'reason': f'Failed to download from {image_url}'
            })
        
        # Progress update every 10 items
        if i % 10 == 0:
            print(f"\n--- Progress Update ---")
            print(f"Processed: {i}/{total_images}")
            print(f"Successfully cached: {cached_images}")
            print(f"Failed: {failed_images}")
            print(f"Skipped (already cached): {skipped_images}")
            print(f"Success rate: {(cached_images/i)*100:.1f}%")
            print(f"----------------------\n")
        
        # Small delay to be respectful to servers
        time.sleep(1)
    
    # Summary
    print(f"\n{'='*50}")
    print(f"Caching complete!")
    print(f"Total images: {total_images}")
    print(f"Successfully cached: {cached_images}")
    print(f"Failed: {failed_images}")
    print(f"Skipped (already cached): {skipped_images}")
    print(f"Success rate: {(cached_images/total_images)*100:.1f}%")
    print(f"Cache directory: {cache_dir.absolute()}")
    
    # Create a mapping file for easy lookup
    mapping_file = cache_dir / "url_mapping.json"
    mapping = {}
    
    for entry in source_entries:
        source_url = entry['url']
        cache_filename = get_cache_filename(source_url)
        cache_path = cache_dir / cache_filename
        
        if cache_path.exists():
            mapping[source_url] = {
                'filename': cache_filename,
                'name': entry['name'],
                'path': entry['path'],
                'size': cache_path.stat().st_size
            }
    
    with open(mapping_file, 'w') as f:
        json.dump(mapping, f, indent=2)
    
    print(f"URL mapping saved to: {mapping_file}")

    # Save failed downloads to a JSON file
    failed_file = cache_dir / "failed_downloads.json"
    with open(failed_file, 'w') as f:
        json.dump(failed_downloads, f, indent=2)
    print(f"Failed downloads saved to: {failed_file}")

if __name__ == "__main__":
    main() 