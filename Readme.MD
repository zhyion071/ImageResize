# ImageResize

A Termux CLI tool for resizing single texture files or entire folders to custom dimensions while removing hidden metadata and canvas layout tags. This tool strips out the embedded canvas information blocks that cause software like Blockbench to slice imported textures in half.

## Prerequisites & Requirements

1. **Get Termux from F-Droid**
   Do NOT download Termux from the Google Play Store, as that version is abandoned and will throw network errors. Download the official, up-to-date app from F-Droid instead:
   * [Download Termux on F-Droid](https://f-droid.org)

2. **Grant Storage Access**
   Before installing or using the tool, you must allow Termux to access your device storage. Open Termux and run:
   ```bash
   termux-setup-storage
   ```
   Tap Allow on the system popup that appears.

3. **Install Git**
   You need git installed to download the repository. Open Termux and run:
   ```bash
   pkg install git -y
   ```

## Installation

Once your storage permissions and git are configured, run these commands inside Termux to clone the repository and run the setup script:

```bash
git clone https://github.com/zhyion071/ImageResize/
cd ~/ImageResize
chmod +x setup.sh
./setup.sh
```

Restart your terminal session or run `source ~/.bashrc` to activate the path shortcut.

## How to Use

Run the shortcut command from any directory on your device:
```bash
imr
```

### Input Options:
* **Single File:** Type or paste the full image file path (e.g., `/sdcard/textures/my_image.png`).
* **Entire Folder:** Type or paste the full folder directory path (e.g., `/sdcard/textures/`).

All processed files retain their original filenames and are saved straight to `/sdcard/Pictures/ImageResizer/` as flat, metadata-free PNGs.
