# StreamDeck <-> Keyboard Maestro
A Streamdeck plugin for Keyboard Maestro integration

This is *not* redistributable, since Python relies on some libraries

## Below is a VERY basic getting started

NOTE: feel free to create an issue if you have specific questions.  As always you can create a pull request to improve things... I really would love community help.

## Prerequisites:

```
python 3.6+
websocket-client
Tested on macOS 10.14.4
```

## Plugin Installation Instructions

1. Quit the StreamDeck app
2. Download the source (here)
3. Copy or link the folder `com.myhdbox.keyboard_maestro.sdPlugin` to `~/Library/Application\ Support/com.elgato.StreamDeck/Plugins`

## Plugin Configuration Instructions

1. Create a python3 virtual environment for your plugin(s)  
`python3 -m venv streamdeck_venv`
2. Activate  
`source streamdeck_venv/bin/activate`
3. Upgrade pip  
`pip install --upgrade pip`
4. Install websocket-client  
`pip install websocket-client`
5. Modify the first line of `main.py` to point to your virtual environment's python
6. Look over the `manifest.json` file to make sure it's configured to your liking
7. Modify the two variables `plugin_dir` and `log_filename` towards the top of `main.py` to match your locations
8. Restart the StreamDeck app

