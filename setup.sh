#!/usr/bin/env bash

echo "Setting up Image Resizer dependencies..."
pkg install python python-pillow -y

# Create global binary link to execute from any path
mkdir -p ~/bin
cat << 'INNER_EOF' > ~/bin/imageresizer
#!/usr/bin/env bash
cd ~/ImageResize/ && python3 resizer.py
INNER_EOF

chmod +x ~/bin/imageresizer
export PATH="$HOME/bin:$PATH"
if [[ ! ":$PATH:" == *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

echo "Package installation complete! Try typing: imageresizer"
