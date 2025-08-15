from PIL import Image, ImageDraw, ImageFont

# Create a white background image
card = Image.new('RGB', (600, 300), color='gray')
draw = ImageDraw.Draw(card)

# Add fonts (use default if custom not available)
try:
    font_large = ImageFont.truetype("arial.ttf", 36)
    font_small = ImageFont.truetype("arial.ttf", 24)
except:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Add text
draw.text((20, 30), "Drisha Vaishnav", font=font_large, fill='black')
draw.text((20, 80), "Software Developer", font=font_small, fill='black')
draw.text((20, 130), "Phone: 9876543210", font=font_small, fill='black')
draw.text((20, 170), "Email: drisha@email.com", font=font_small, fill='black')
draw.text((20, 210), "Address: Mumbai, India", font=font_small, fill='black')

# Save the visiting card image
card.save("visiting_card.png")
print("✅ Visiting card saved as 'visiting_card.png'")
