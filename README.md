# Tic Tac Toe

[![Download Latest Release](https://img.shields.io/github/v/release/rohith-vp/tic-tac-toe-pygame?label=Download%20Latest%20Release)](https://github.com/rohith-vp/tic-tac-toe-pygame/releases)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-3776AB)](https://www.python.org/)
[![PyInstaller Version](https://img.shields.io/badge/PyInstaller-5.x-orange)](https://www.pyinstaller.org/)

**Play Tic Tac Toe instantly!**

If you just want to play the game, **download the latest prebuilt binary** for your platform from the [**Releases**](https://github.com/rohith-vp/tic-tac-toe-pygame/releases) section — no setup or Python installation required.

---

## Installation & Setup (for developers or from source)

### Prerequisites

- Python 3.7 or above  
- [`uv`](https://docs.astral.sh/uv/) (Python Package Manager)

### Installation Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/rohith-vp/tic-tac-toe-pygame.git
    cd tic-tac-toe-pygame
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    uv sync
    ```

3. Run the game:

    ```bash
    uv run python -m app.main
    ```

---

### Building an Executable (optional)

To build your own standalone binary using PyInstaller:

```bash
uv run pyinstaller --onefile --windowed --icon=app/res/icon.ico --add-data "app/res;res" app/main.py
```

### Project Structure

tic-tac-toe-pygame/
├── app/
│   ├── main.py           # Main game script
│   ├── res/              # Resources (icons, fonts, images)
│   │   ├── icon.ico
│   │   ├── font.ttf
│   │   └── bg.jpg
│   └── __init__.py
├── pyproject.toml        # UV & project configuration
├── uv.lock               # Locked dependencies
├── dist/                 # Compiled binaries (after PyInstaller build)
├── build/                # PyInstaller temporary build folder
└── README.md