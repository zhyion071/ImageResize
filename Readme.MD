# ImageResize

A CLI tool for Android (Termux) that resizes texture files to custom dimensions without locking the aspect ratio. It completely wipes out hidden metadata and canvas layout tags from software like Roblox exporters, preventing Blockbench from slicing your images in half on import.

All resized images match their original filenames and are saved straight to `/sdcard/Pictures/ImageResizer`.

## Installation

Run these commands in Termux to clone the repository and run the setup script:

```bash
git clone https://github.com ~/ImageResize
cd ~/ImageResize
chmod +x setup.sh
./setup.sh
```

## How to Use

You can run the script from any directory on your device.

1. Type the global command:
```bash
imageresizer
```

2. When prompted, enter the full path to your file:
```text
Import File Path (e.g. /sdcard/textures/image.png): /sdcard/textures/my_texture.png
```

3. Enter your target resolution using 'x' as a separator:
```text
Enter size to resize? (e.g. 1024x1024): 1024x1024
```

The script will copy the pure pixels onto a sterile canvas, strip the header data, and drop the output file directly into your Pictures directory.
