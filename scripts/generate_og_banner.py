from PIL import Image, ImageDraw, ImageFont
import os

width = 1200
height = 630

# Create dark gradient background
img = Image.new('RGBA', (width, height), (10, 15, 29, 255))
draw = ImageDraw.Draw(img)

# Draw subtle background glow & grid elements
for y in range(0, height, 30):
    draw.line([(0, y), (width, y)], fill=(30, 41, 59, 40), width=1)
for x in range(0, width, 30):
    draw.line([(x, 0), (x, height)], fill=(30, 41, 59, 40), width=1)

# Glowing accent shapes
draw.ellipse([(-100, -100), (400, 400)], fill=(16, 185, 129, 25))
draw.ellipse([(800, 200), (1300, 700)], fill=(99, 102, 241, 25))

# Draw border frame
draw.rectangle([(20, 20), (width - 20, height - 20)], outline=(30, 41, 59, 255), width=2)
draw.rectangle([(24, 24), (width - 24, height - 24)], outline=(16, 185, 129, 100), width=1)

# Try loading TrueType fonts or fall back to default
font_title = None
font_subtitle = None
font_badge = None

try:
    font_title = ImageFont.truetype("arial.ttf", 68)
    font_subtitle = ImageFont.truetype("arial.ttf", 34)
    font_badge = ImageFont.truetype("arial.ttf", 26)
    font_small = ImageFont.truetype("arial.ttf", 22)
except Exception:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_badge = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Header Pill Badge
badge_text = "  PRO PORTFOLIO  "
draw.rectangle([(80, 70), (280, 110)], fill=(16, 185, 129, 40), outline=(16, 185, 129, 255), width=1)
draw.text((95, 78), "SANJAY G. L.", fill=(52, 211, 153), font=font_badge)

# Main Title
draw.text((80, 140), "Full Stack AI Developer", fill=(255, 255, 255), font=font_title)
draw.text((80, 220), "& Software Engineer", fill=(148, 163, 184), font=font_title)

# Subtitle / Education
draw.text((80, 320), "BCA Student (PESIAMS) • Shivamogga, Karnataka, India", fill=(203, 213, 225), font=font_subtitle)

# Stats Cards
card_y = 410
card_h = 130
card_w = 320

# Card 1: Projects
draw.rectangle([(80, card_y), (80 + card_w, card_y + card_h)], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((100, card_y + 20), "28+ Projects", fill=(16, 185, 129), font=font_subtitle)
draw.text((100, card_y + 70), "Full Stack, AI & Security", fill=(148, 163, 184), font=font_small)

# Card 2: Certificates
draw.rectangle([(430, card_y), (430 + card_w, card_y + card_h)], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((450, card_y + 20), "86+ Certificates", fill=(99, 102, 241), font=font_subtitle)
draw.text((450, card_y + 70), "Govt, AICTE & HackerRank", fill=(148, 163, 184), font=font_small)

# Card 3: Core Stack
draw.rectangle([(780, card_y), (780 + card_w, card_y + card_h)], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((800, card_y + 20), "Python & Flask", fill=(244, 63, 94), font=font_subtitle)
draw.text((800, card_y + 70), "React, Gemini API, Docker", fill=(148, 163, 184), font=font_small)

# Footer domain pill
draw.text((80, 565), "https://sanjaygl30ai.vercel.app", fill=(16, 185, 129), font=font_small)

out_dir = 'assets'
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'og-banner.png')
img.save(out_path)
print(f"Generated OG Banner at {out_path} ({width}x{height})")
