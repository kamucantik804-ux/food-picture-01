#!/usr/bin/env python3
"""
Food Picture Generator - Generate best-looking food picture
Output: /output/entry.png (max 1024x1024, max 1 MiB)
"""

import os
import random
from PIL import Image, ImageDraw, ImageFilter

def generate_food_image():
    """Generate a delicious-looking food image"""
    width, height = 1024, 1024
    
    # Create image with warm, appetizing colors
    img = Image.new("RGB", (width, height), "#FFF8E7")
    draw = ImageDraw.Draw(img)
    
    # Background gradient (warm tones)
    for y in range(height):
        ratio = y / height
        r = int(255 - ratio * 30)
        g = int(248 - ratio * 40)
        b = int(231 - ratio * 50)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Add plate (white oval)
    plate_center = (width // 2, height // 2 + 50)
    plate_radius_x = 350
    plate_radius_y = 280
    plate_bbox = [
        plate_center[0] - plate_radius_x,
        plate_center[1] - plate_radius_y,
        plate_center[0] + plate_radius_x,
        plate_center[1] + plate_radius_y
    ]
    
    # Plate shadow
    draw.ellipse(
        [plate_bbox[0] + 10, plate_bbox[1] + 10, 
         plate_bbox[2] + 10, plate_bbox[3] + 10],
        fill="#E8E0D5"
    )
    
    # Plate
    draw.ellipse(plate_bbox, fill="#FFFFFF", outline="#E0E0E0", width=3)
    
    # Inner plate
    inner_bbox = [
        plate_bbox[0] + 20,
        plate_bbox[1] + 20,
        plate_bbox[2] - 20,
        plate_bbox[3] - 20
    ]
    draw.ellipse(inner_bbox, fill="#FAFAFA", outline="#F0F0F0", width=2)
    
    # Food - burger stack
    burger_center_x = plate_center[0]
    burger_base_y = plate_center[1] + 40
    
    # Bun bottom
    bun_bottom = [
        (burger_center_x - 180, burger_base_y),
        (burger_center_x + 180, burger_base_y),
        (burger_center_x + 160, burger_base_y - 60),
        (burger_center_x - 160, burger_base_y - 60)
    ]
    draw.polygon(bun_bottom, fill="#D4A574", outline="#C49564")
    
    # Lettuce
    lettuce_y = burger_base_y - 55
    for i in range(20):
        x = burger_center_x - 150 + i * 15
        draw.ellipse([x, lettuce_y, x + 10, lettuce_y + 20], 
                     fill="#4A8C3F", outline="#3D7A33")
    
    # Patty
    patty_y = burger_base_y - 80
    draw.ellipse(
        [burger_center_x - 160, patty_y - 15, 
         burger_center_x + 160, patty_y + 35],
        fill="#8B4513", outline="#6B3410"
    )
    
    # Cheese
    cheese_y = patty_y - 5
    draw.ellipse(
        [burger_center_x - 140, cheese_y - 25,
         burger_center_x + 140, cheese_y + 5],
        fill="#FFD700", outline="#E6C200"
    )
    # Cheese drip
    for dx in [-100, -50, 50, 100]:
        draw.ellipse(
            [burger_center_x + dx, cheese_y - 15,
             burger_center_x + dx + 15, cheese_y + 5],
            fill="#FFD700"
        )
    
    # Tomato slice
    tomato_y = cheese_y - 15
    draw.ellipse(
        [burger_center_x - 120, tomato_y - 25,
         burger_center_x + 120, tomato_y + 5],
        fill="#FF6347", outline="#CC5233"
    )
    # Tomato seeds
    import math
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        sx = burger_center_x + 50 * math.cos(rad)
        sy = tomato_y - 5 + 20 * math.sin(rad)
        draw.ellipse([sx-3, sy-3, sx+3, sy+3], fill="#FFD700")
    
    # Patty 2
    patty2_y = tomato_y - 35
    draw.ellipse(
        [burger_center_x - 150, patty2_y - 12,
         burger_center_x + 150, patty2_y + 30],
        fill="#A0522D", outline="#8B4513"
    )
    
    # Onion rings
    for i in range(3):
        ring_x = burger_center_x - 100 + i * 100
        draw.ellipse(
            [ring_x - 30, patty2_y - 20, ring_x + 30, patty2_y + 5],
            outline="#FFE4B5", width=3
        )
    
    # Upper bun
    upper_bun = [
        (burger_center_x - 170, patty2_y - 50),
        (burger_center_x + 170, patty2_y - 50),
        (burger_center_x + 150, patty2_y - 110),
        (burger_center_x - 150, patty2_y - 110)
    ]
    draw.polygon(upper_bun, fill="#C9956B", outline="#B8855B")
    
    # Sesame seeds on bun
    seeds = [
        (burger_center_x - 80, patty2_y - 85),
        (burger_center_x - 30, patty2_y - 90),
        (burger_center_x + 30, patty2_y - 88),
        (burger_center_x + 80, patty2_y - 82),
        (burger_center_x - 50, patty2_y - 100),
        (burger_center_x + 50, patty2_y - 98),
        (burger_center_x, patty2_y - 95),
    ]
    for sx, sy in seeds:
        draw.ellipse([sx-3, sy-2, sx+3, sy+3], fill="#F5DEB3")
    
    # French fries in basket
    basket_x = plate_center[0] + 220
    basket_y = plate_center[1] + 150
    
    # Basket
    basket_bbox = [
        basket_x - 80, basket_y - 30,
        basket_x + 80, basket_y + 80
    ]
    draw.ellipse(basket_bbox, fill="#8B6914", outline="#6B4F10", width=3)
    draw.ellipse(
        [basket_bbox[0]+10, basket_bbox[1]+10,
         basket_bbox[2]-10, basket_bbox[3]-10],
        fill="#A0782C"
    )
    
    # Fries
    for i in range(15):
        fx = basket_x - 60 + i * 8
        fy = basket_y + 10 + random.randint(0, 30)
        length = random.randint(40, 80)
        draw.rectangle(
            [fx, fy, fx + 8, fy + length],
            fill="#FFD700", outline="#E6C200"
        )
        # Fry chip lines
        for line in range(3):
            ly = fy + 10 + line * 20
            if ly < fy + length:
                draw.line([(fx+1, ly), (fx+7, ly)], fill="#E6C200")
    
    # Coleslaw side
    slaw_x = plate_center[0] - 250
    slaw_y = plate_center[1] + 180
    draw.ellipse(
        [slaw_x - 60, slaw_y - 20, slaw_x + 60, slaw_y + 60],
        fill="#B8D4A0", outline="#9BC08A"
    )
    for i in range(30):
        sx = slaw_x - 50 + random.randint(0, 100)
        sy = slaw_y - 10 + random.randint(0, 60)
        draw.ellipse([sx-5, sy-5, sx+5, sy+5], 
                     fill="#FFFFFF", outline="#E8E8E8")
    
    # Garnish - parsley leaves
    for i in range(5):
        gx = plate_center[0] - 300 + i * 150
        gy = plate_center[1] + 250
        draw.ellipse([gx-8, gy-4, gx+8, gy+4], fill="#2D5016")
        draw.ellipse([gx-4, gy-8, gx+4, gy+2], fill="#3D7A1C")
    
    # Soft glow effect
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    # Add warm vignette
    for i in range(10):
        alpha = 5 * (10 - i)
        draw.rectangle(
            [i*10, i*10, width-i*10, height-i*10],
            outline=(0, 0, 0, alpha),
            width=1
        )
    
    # Convert to RGB and save
    img = img.convert("RGB")
    
    output_path = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    
    # Verify file size
    file_size = os.path.getsize(output_path)
    print(f"Generated: {output_path}")
    print(f"Size: {file_size} bytes ({file_size/1024:.1f} KB)")
    print(f"Dimensions: {width}x{height}")
    
    if file_size > 1024 * 1024:
        print("ERROR: File too large! Reducing...")
        img_small = img.resize((512, 512), Image.Resampling.LANCZOS)
        img_small.save(output_path, "PNG", optimize=True)
        file_size = os.path.getsize(output_path)
        print(f"Resized: {file_size} bytes ({file_size/1024:.1f} KB)")
    
    return output_path

if __name__ == "__main__":
    generate_food_image()
    print("\n✅ Food picture generated successfully!")
