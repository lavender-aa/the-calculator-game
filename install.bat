:: make sure python exists
python3 --version || {
    echo "Python3 is not installed; cancelling install."
    exit
}

:: install dependencies
echo "Installing dependencies (pyintaller, sympy)"
python3 -m pip install pyinstaller sympy

:: create binary
pyinstaller --noconfirm --onefile scr/game.py