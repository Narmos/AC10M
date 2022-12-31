![Platform Support](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opencv-contrib-python)

# AC10M

:white_check_mark: Tested on Windows 10/11, macOS 13 Ventura and Ubuntu 22.04 LTS

## Prerequisite

1. Install [Python](https://www.python.org/downloads/)

    For Ubuntu, Python 3 is already installed by default, however, you must install the Python package manager `pip`

    ```
    sudo apt install python3-pip
    ```

2. Install Python package [opencv-contrib-python](https://pypi.org/project/opencv-contrib-python/)

    ```
    pip3 install opencv-contrib-python
    ```

## Usage

Take a look at the `config.py` file

Run for Linux and macOS

```
python3 main.py
```

Run for Windows

```
python main.py
```

Press `ESC` to exit the program

Press `p` to calibrate the target (set corner points from frame source)

## Credits

* [OpenCV](https://opencv.org/)
