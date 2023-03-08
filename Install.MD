# How to install and run the app with Kivy framework
This is the steps to install and run Kivy framework on macOS:

1. Open Terminal and install Homebrew, a popular package manager for macOS, by running the following command:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Use Homebrew to install Python 3 by running the following command:
`brew install python@3.9`

3. Install the necessary dependencies for Kivy by running the following command:
`brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer`

4. Install Cython, a compiler for Python extensions, by running the following command:
`pip3 install cython`

5. Install Pygame using pip by running the following command:
`pip3 install pygame`

6. Install Kivy by running the following command:
`pip3 install kivy`

7. Test the installation by running the following command:
`python3 main.py`
