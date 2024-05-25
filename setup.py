import sys
from cx_Freeze import setup, Executable

script_name = 'main.py'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
    script_name,
    base=base,
    icon='C:\\My files\\Coding\\programming_main\\New projects\\Calculator\\icon.ico',
)


includes = [
    'numpy',
    'tkinter',
    'random',
    'pandas',
    'matplotlib',
    'cmath',
    'sympy',
]

packages = ['numpy', 'tkinter', 'random', 'pandas', 'matplotlib', 'cmath', 'sympy']


icon_path = r'C:\My files\Coding\programming_main\New projects\Calculator\icon.ico'
me_path = r'C:\My files\Coding\programming_main\New projects\Calculator\Me.png'


include_files = [
    (icon_path, 'icon.ico'),  # Destination path relative to the executable
    (me_path, 'Me.png'),      # Destination path relative to the executable
]

setup(
    name='Calculator',
    version='1.0',
    description='This is a simply made calculator that includes usual,scientific,complex,functions and equations calculations',
    options={
        'build_exe': {
            'includes': includes,
            'include_files': include_files,
            'packages': packages,
        },
    },
    executables=[exe],
)
