#!/usr/bin/env bash

echo "Installing core Python environment..."
pkg install python -y

echo "Installing Pillow module via pip..."
pip install pillow

# Create global binary shortcut link named imr
mkdir -p ~/bin
cat << 'INNER_EOF' > ~/bin/imr
#!/usr/bin/env bash
cd ~/ImageResize && python3 resizer.py
INNER_EOF

chmod +x ~/bin/imr
export PATH="$HOME/bin:$PATH"
if [[ ! ":$PATH:" == *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

echo "Package installation complete! Try typing: imr"
