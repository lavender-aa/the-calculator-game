#! /usr/bin/bash

# check if python is installed (else exit)
echo "Checking python3 installation"
python3 --version \
|| {
    echo "Python3 is not installed; cancelling install."
    exit 1
}

# install pyinstaller and sympy
echo "Installing dependencies (pyinstaller, sympy)"
python3 -m pip install pyinstaller sympy

# create binary
pyinstaller --noconfirm --onefile src/game.py