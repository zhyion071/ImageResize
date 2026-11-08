import os
import re
import glob
from PIL import Image
from PIL.PngImagePlugin import PngInfo

def resize_image(file_path, width, height, output_dir):
    filename = os.path.basename(file_path)
    try:
        orig = Image.open(file_path)
        canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        resized = orig.resize((width, height))
        canvas.paste(resized, (0, 0))
        
        output_path = os.path.join(output_dir, filename)
        empty_info = PngInfo()
        canvas.save(output_path, "PNG", pnginfo=empty_info)
        print(f"Successfully processed: {filename}")
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

def run():
    print("\n--- IMAGE RESIZER CLI ---")
    
    # 1. Ask for input path (can be file or directory)
    input_path = input("Import Path (e.g. /sdcard/textures/ or path/to/file.png): ").strip()
    
    if not os.path.exists(input_path):
        print(f"Error: Path not found at '{input_path}'")
        return

    # 2. Dimensions prompt (WidthxHeight)
    dimensions = input("Enter size to resize? (e.g. 1024x1024): ").strip()
    
    match = re.match(r"^([0-9]+)[xX]([0-9]+)$", dimensions)
    if not match:
        print("Error: Invalid format. Please use 'WidthxHeight' like 1024x1024.")
        return
        
    width, height = int(match.group(1)), int(match.group(2))
    
    output_dir = "/sdcard/Pictures/ImageResizer"
    os.makedirs(output_dir, exist_ok=True)

    # 3. Check if path is folder or file
    if os.path.isdir(input_path):
        # Gather all png, PNG, jpg, and JPEG images in the directory
        extensions = ['*.png', '*.PNG', '*.jpg', '*.JPG', '*.jpeg', '*.JPEG']
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(input_path, ext)))
            
        if not files:
            print("No image files found in that directory.")
            return
            
        print(f"Structuring pure pixels and resizing {len(files)} files to {width}x{height}...")
        for file_path in files:
            resize_image(file_path, width, height, output_dir)
    else:
        print(f"Structuring pure pixels and resizing single file to {width}x{height}...")
        resize_image(input_path, width, height, output_dir)
        
    print(f"\nResize complete! Check your files in: {output_dir}\n")

if __name__ == "__main__":
    run()
