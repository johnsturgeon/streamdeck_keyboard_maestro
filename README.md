# streamdeck_keyboard_maestro
A Streamdeck plugin for Keyboard Maestro integration

NOTES: I need to update the readme, I'll start out with some very basic 'getting started'

This is *not* redistributable, since Python relies on some libraries

## Prerequisites:

```
python 3.6+
pip install websocket-client
pip install websockets
```

* Look over the manifest.json to make sure it's configured to your liking
* Change the variables at the top of `main.py` to your plugin location

TODO: 

* Update README with links to StreamDeck SDK and reddit
* Lots of improvements to the plugin to support two-way communication between the plugin and Keyboard Maestro
* Create python classes to handle some of the messagign


