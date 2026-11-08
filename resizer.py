import os
import re
from PIL import Image
from PIL.PngImagePlugin import PngInfo

def run():
    print("\n--- IMAGE RESIZER CLI ---")
    
    # 1. Ask for full folder path + filename import
    file_path = input("Import File Path (e.g. /sdcard/textures/image.png): ").strip()
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return
        
    filename = os.path.basename(file_path)
    
    # 2. Dimensions prompt (WidthxHeight)
    dimensions = input("Enter size to resize? (e.g. 1024x1024): ").strip()
    
    match = re.match(r"^([0-9]+)[xX]([0-9]+)$", dimensions)
    if not match:
        print("Error: Invalid format. Please use 'WidthxHeight' like 1024x1024.")
        return
        
    width, height = int(match.group(1)), int(match.group(2))
    print(f"Structuring pure pixels and resizing to {width}x{height}...")
    
    try:
        # Replicate ImResizer logic: paste onto a standard fresh grid to drop layout metadata arrays
        orig = Image.open(file_path)
        canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        resized = orig.resize((width, height))
        canvas.paste(resized, (0, 0))
        
        # Output directly to the target directory
        output_dir = "/sdcard/Pictures/ImageResizer"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)
        
        # Enforce empty PngInfo so Blockbench never reads original texture bounds
        empty_info = PngInfo()
        canvas.save(output_path, "PNG", pnginfo=empty_info)
        
        print("Resize complete!")
        print(f"Saved to: {output_path}\n")
        
    except Exception as e:
        print(f"Execution Failure: {e}")

if __name__ == "__main__":
    run()
