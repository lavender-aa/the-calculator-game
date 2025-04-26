:: make sure python exists
python --version || (
    echo Python3 is not installed; cancelling install.
    pause
    exit
)

:: install dependencies
echo Installing dependencies (pyintaller, sympy)
python -m pip install pyinstaller sympy

:: create binary
echo Buliding game binary
pyinstaller --noconfirm --onefile --noconsole src\game.py
