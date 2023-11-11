![Platform Support](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opencv-contrib-python)

# AC10M

:white_check_mark: Tested on Windows 10/11, macOS 13/14 and Ubuntu 22.04 LTS

## Prerequisite

1. Install [Python](https://www.python.org/downloads/)

    For Ubuntu, Python 3 is already installed by default, however, you must install the Python package manager `pip` and the `Tkinter` library which are included by default on Windows and macOS

    ```
    sudo apt install python3-pip python3-tk
    ```

2. Install Python packages [opencv-contrib-python](https://pypi.org/project/opencv-contrib-python/) and [Pillow](https://pypi.org/project/Pillow/)

    ```
    pip3 install --upgrade opencv-contrib-python Pillow
    ```

## Usage

Before run the script, take a look at the `config.py` file

Run for Linux and macOS

```
python3 main-gui.py
```

Run for Windows

```
python main-gui.py
```

## Credits

* [OpenCV](https://opencv.org/)
