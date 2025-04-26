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
pyinstaller --noconfirm --onefile --noconsole src\game.py || (
    :: pyinstaller not found
    echo Build failed; please ensure PyInstaller's parent folder is included in your PATH.
    echo This folder is in one of two places; run these lines inside a python environment to find them:
    echo
    echo 1) >>> import sysconfig; print(sysconfig.get_path("scripts"))
    echo 2) >>> import site; print(site.USER_BASE + "\\Scripts")
    echo
    echo Open both of these folders; whichever one has `pyinstaller.exe`, add that one to your system or user PATH, and try installing again.
    pause
)
