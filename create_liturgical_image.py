import sys
import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from liturgical_calendar.liturgical import liturgical_calendar
from liturgical_calendar.artwork import get_image_source_for_date

# Font paths
FONTS_DIR = Path(__file__).parent / 'fonts'
SERIF_FONT = FONTS_DIR / 'TestSignifier-Regular.otf'
SANS_FONT = FONTS_DIR / 'HankenGrotesk-VariableFont_wght.ttf'

# Image settings
WIDTH, HEIGHT = 1404, 1872
PADDING = 48
ARTWORK_SIZE = 1080
ROW_SPACING = 48

# Font sizes
HEADER_FONT_SIZE = 36
TITLE_FONT_SIZE = 96
COLUMN_FONT_SIZE = 36

# Colors
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (74, 74, 74)  # #4A4A4A
LINE_COLOR = (151, 151, 151)


def get_date_str(date):
    return date.strftime('%Y-%m-%d')

def get_friendly_date(date):
    return date.strftime('%-d %B, %Y')

def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

def main():
    # Parse date argument
    if len(sys.argv) > 1:
        try:
            date = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d').date()
        except Exception:
            print('Invalid date format. Use YYYY-MM-DD.')
            sys.exit(1)
    else:
        date = datetime.date.today()
    date_str = get_date_str(date)
    friendly_date = get_friendly_date(date)

    # Get liturgical info
    info = liturgical_calendar(date_str)
    artwork = get_image_source_for_date(date_str, info)

    # Prepare fonts
    serif_font_36 = ImageFont.truetype(str(SERIF_FONT), HEADER_FONT_SIZE)
    serif_font_96 = ImageFont.truetype(str(SERIF_FONT), TITLE_FONT_SIZE)
    sans_font_36 = ImageFont.truetype(str(SANS_FONT), COLUMN_FONT_SIZE)
    sans_font_36_uc = ImageFont.truetype(str(SANS_FONT), COLUMN_FONT_SIZE)

    # Create base image
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Row 1: Season (sans, uppercase) — Date (serif)
    season = info.get('season', '').upper()
    # Use EM DASH (–) in sans-serif to avoid rendering artifacts
    header_dash = ' — '
    season_text = season
    date_text = f"{friendly_date}"
    # Measure for baseline alignment
    season_w, season_h = get_text_size(draw, season_text, sans_font_36_uc)
    dash_w, dash_h = get_text_size(draw, header_dash, sans_font_36_uc)
    date_w, date_h = get_text_size(draw, date_text, serif_font_36)
    total_w = season_w + dash_w + date_w
    x = (WIDTH - total_w) // 2
    y = PADDING
    # Baseline alignment: get font metrics
    sans_ascent, sans_descent = sans_font_36_uc.getmetrics()
    serif_ascent, serif_descent = serif_font_36.getmetrics()
    baseline_y = y + max(sans_ascent, serif_ascent)
    # Draw season (sans, upper)
    draw.text((x, baseline_y - sans_ascent), season_text, font=sans_font_36_uc, fill=TEXT_COLOR)
    # Draw dash (sans)
    draw.text((x + season_w, baseline_y - sans_ascent), header_dash, font=sans_font_36_uc, fill=TEXT_COLOR)
    # Draw date (serif)
    draw.text((x + season_w + dash_w, baseline_y - serif_ascent), date_text, font=serif_font_36, fill=TEXT_COLOR)

    # Row 2: Artwork (centered)
    art_y = y + HEADER_FONT_SIZE + ROW_SPACING
    art_x = (WIDTH - ARTWORK_SIZE) // 2
    artwork_img = None
    next_artwork = None
    show_next_artwork = False
    if artwork and artwork.get('cached_file'):
        try:
            artwork_img = Image.open(artwork['cached_file']).convert('RGB')
        except Exception:
            artwork_img = None
    if not artwork_img:
        # Try to find the next available artwork after this date
        from datetime import timedelta
        search_date = date
        for _ in range(366):  # Search up to a year ahead
            search_date += timedelta(days=1)
            next_artwork_candidate = get_image_source_for_date(get_date_str(search_date))
            if next_artwork_candidate and next_artwork_candidate.get('cached_file'):
                next_artwork = next_artwork_candidate
                break
        # fallback: blank or placeholder
        artwork_img = Image.new('RGB', (ARTWORK_SIZE, ARTWORK_SIZE), (230, 230, 230))
        show_next_artwork = next_artwork is not None
    img.paste(artwork_img.resize((ARTWORK_SIZE, ARTWORK_SIZE)), (art_x, art_y))
    # If showing next artwork, draw it at 50% size centered in the square
    if show_next_artwork:
        thumb_size = ARTWORK_SIZE // 2
        thumb_x = art_x + (ARTWORK_SIZE - thumb_size) // 2
        thumb_y = art_y + (ARTWORK_SIZE - thumb_size) // 2
        try:
            thumb_img = Image.open(next_artwork['cached_file']).convert('RGB').resize((thumb_size, thumb_size))
            img.paste(thumb_img, (thumb_x, thumb_y))
        except Exception:
            pass
        # Draw the next artwork title below the thumbnail
        next_title = next_artwork.get('name', '')
        next_title_y = thumb_y + thumb_size + 16
        # Draw 'NEXT: ' in sans-serif, then title in serif, baseline aligned
        next_prefix = 'NEXT: '
        # Get font metrics for baseline alignment
        sans_ascent, sans_descent = sans_font_36.getmetrics()
        serif_ascent, serif_descent = serif_font_36.getmetrics()
        next_prefix_w, _ = get_text_size(draw, next_prefix, sans_font_36)
        next_title_w, _ = get_text_size(draw, next_title, serif_font_36)
        total_next_w = next_prefix_w + next_title_w
        next_x = art_x + (ARTWORK_SIZE - total_next_w) // 2
        # Align baselines
        baseline_y = next_title_y + max(sans_ascent, serif_ascent)
        draw.text((next_x, baseline_y - sans_ascent), next_prefix, font=sans_font_36, fill=TEXT_COLOR)
        draw.text((next_x + next_prefix_w, baseline_y - serif_ascent), next_title, font=serif_font_36, fill=TEXT_COLOR)
        # Draw the date of the next artwork in parentheses below, centered
        next_artwork_date = next_artwork.get('date')
        if not next_artwork_date:
            # Try to find the date by searching forward again
            from datetime import timedelta
            search_date = date
            for _ in range(366):
                search_date += timedelta(days=1)
                candidate = get_image_source_for_date(get_date_str(search_date))
                if candidate and candidate.get('cached_file') == next_artwork.get('cached_file'):
                    next_artwork_date = get_friendly_date(search_date)
                    break
        if next_artwork_date:
            date_text = next_artwork_date
            # Use sans-serif 32px font
            sans_font_32 = ImageFont.truetype(str(SANS_FONT), 32)
            # Align left edge of date to left edge of next artwork name
            date_x = next_x + next_prefix_w
            date_y = baseline_y + 8  # 8px below the title
            draw.text((date_x, date_y), date_text, font=sans_font_32, fill=TEXT_COLOR)

    # Row 3: Artwork title (serif, 96px, centered, wrap if too long)
    if artwork and artwork.get('name', ''):
        title = artwork.get('name', '')
    else:
        title = date.strftime('%A')  # Use weekday name if no artwork
    title_y = art_y + ARTWORK_SIZE + ROW_SPACING
    # Replace Unicode colon with sans-serif colon for rendering
    title = title.replace('：', ':')
    # Wrap title if too wide
    def wrap_text(text, font, max_width):
        words = text.split()
        lines = []
        current = ''
        for word in words:
            test = current + (' ' if current else '') + word
            w, _ = get_text_size(draw, test, font)
            if w <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines
    title_lines = wrap_text(title, serif_font_96, WIDTH - 2 * PADDING)
    # Draw each line and track total height and last baseline
    last_title_baseline = title_y
    for i, line in enumerate(title_lines):
        line_w, line_h = get_text_size(draw, line, serif_font_96)
        line_x = (WIDTH - line_w) // 2
        line_y = title_y + i * line_h
        draw.text((line_x, line_y), line, font=serif_font_96, fill=TEXT_COLOR)
        last_title_baseline = line_y + serif_font_96.getmetrics()[0]  # baseline = y + ascent
    # Row 4: Two columns (week name, readings)
    week = info.get('week', '')
    # Calculate cap-height for sans-serif week font
    sans_ascent_col, _ = sans_font_36_uc.getmetrics()
    # Place cap-height of week at 96px below last title baseline
    col_y = last_title_baseline + 96 - sans_ascent_col
    week_w, week_h = get_text_size(draw, week, sans_font_36_uc)
    readings = info.get('readings', [])
    if not readings:
        readings = ['No assigned readings for this day.']
    readings_parts = []
    readings_w = 0
    import string
    PUNCTUATION = set(':,.;–—()[]!?')
    for r in readings:
        # Split the line into runs of punctuation and non-punctuation
        runs = []
        current = ''
        current_is_punct = None
        for ch in r:
            is_punct = ch in PUNCTUATION
            if current == '':
                current = ch
                current_is_punct = is_punct
            elif is_punct == current_is_punct:
                current += ch
            else:
                runs.append((current, current_is_punct))
                current = ch
                current_is_punct = is_punct
        if current:
            runs.append((current, current_is_punct))
        # Measure total width
        total_w = 0
        for text, is_punct in runs:
            font = sans_font_36_uc if is_punct else serif_font_36
            w, _ = get_text_size(draw, text, font)
            total_w += w
        readings_w = max(readings_w, total_w)
        readings_parts.append(runs)
    # Line height for fourth row
    LINE_HEIGHT = 48
    col_gap = 28 * 2 + 1  # 28px padding each side + 1px line
    total_cols_w = week_w + col_gap + readings_w
    col1_x = (WIDTH - total_cols_w) // 2
    col2_x = col1_x + week_w + col_gap
    # Baseline alignment for columns
    sans_ascent_col, _ = sans_font_36_uc.getmetrics()
    serif_ascent_col, _ = serif_font_36.getmetrics()
    col_baseline_y = col_y + max(sans_ascent_col, serif_ascent_col)
    # Draw left column (week)
    draw.text((col1_x, col_baseline_y - sans_ascent_col), week, font=sans_font_36_uc, fill=TEXT_COLOR)
    # Draw right column (readings, with line-height 48px and sans-serif colon)
    reading_y = col_baseline_y - serif_ascent_col
    reading_ys = []
    readings_x = col1_x + week_w + 32 + 32  # 32px margin + 32px for vertical line
    for runs in readings_parts:
        x = readings_x
        for text, is_punct in runs:
            font = sans_font_36_uc if is_punct else serif_font_36
            w, h = get_text_size(draw, text, font)
            draw.text((x, reading_y), text, font=font, fill=TEXT_COLOR)
            x += w
        reading_ys.append(reading_y)
        reading_y += 48  # Fixed 48px line height
    # Draw vertical line (1px wide, 6px above cap-height, 24px below baseline)
    line_x = col1_x + week_w + 28
    cap_height = serif_ascent_col
    line_top = col_baseline_y - serif_ascent_col - 6
    if reading_ys:
        last_baseline = reading_ys[-1] + serif_ascent_col
    else:
        last_baseline = col_baseline_y
    line_bottom = last_baseline + 24
    draw.rectangle([line_x, line_top, line_x + 1, line_bottom], fill=LINE_COLOR)

    # Save image
    build_dir = Path(__file__).parent / 'build'
    build_dir.mkdir(exist_ok=True)
    if len(sys.argv) > 1:
        out_path = build_dir / f"liturgical_{date_str}.png"
    else:
        out_path = build_dir / "liturgical-today.png"
    img.save(out_path)
    print(f"Saved image to {out_path}")

if __name__ == "__main__":
    main() 