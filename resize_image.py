#!/usr/bin/env python3
"""
Simple image resizer script
"""
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("PIL/Pillow not installed. Trying to install...")
    os.system("pip3 install --user Pillow")
    from PIL import Image

def resize_image(input_path, max_width=1200, quality=85):
    """Resize and optimize an image"""
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Get original size
        width, height = img.size
        print(f'Original size: {width}x{height}')
        print(f'Original file size: {os.path.getsize(input_path) / (1024*1024):.2f} MB')
        
        # Calculate new dimensions
        if width > max_width:
            ratio = max_width / width
            new_height = int(height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            print(f'Resized to: {max_width}x{new_height}')
        else:
            print('Image width is already optimal')
        
        # Convert to RGB if necessary (for JPEG)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Save with optimization
        img.save(input_path, 'JPEG', quality=quality, optimize=True)
        
        print(f'New file size: {os.path.getsize(input_path) / (1024*1024):.2f} MB')
        print('✅ Image optimized successfully!')
        
    except Exception as e:
        print(f'❌ Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    image_path = 'images/homepage-2/service/logistic.jpg'
    resize_image(image_path)
