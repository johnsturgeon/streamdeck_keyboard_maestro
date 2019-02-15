#!/Users/johnsturgeon/Code/streamdeck/bin/python

import argparse
import websocket
import json
from subprocess import Popen

plugin_name = "keyboard_maestro"
DEBUG = True

plugin_dir = f"/Users/johnsturgeon/Code/streamdeck/Plugins/com.sturgeonfamily.{plugin_name}.sdPlugin"
log_filename = f"/Users/johnsturgeon/Code/streamdeck/{plugin_name}.log"

parser = argparse.ArgumentParser(description='Streamdeck Plugin')
parser.add_argument('-port', dest='port')
parser.add_argument('-pluginUUID', dest='pluginUUID')
parser.add_argument('-registerEvent', dest='event')
parser.add_argument('-info', dest='info')
parser.add_argument('-propertyInspectorUUID', dest='propertyInspectorUUID')
args = parser.parse_args()

registration_dict = {'event': args.event, 'uuid': args.pluginUUID}
pi_registration_dict = {'event': args.event, 'uuid': args.propertyInspectorUUID}

macroUUID = ""
instance_context = ""
device_id = ""


def log_debug(message):
    if DEBUG:
        log_file = open(log_filename, "a+")
        log_file.write(f"{message}\n")
        log_file.close()


log_debug(args.port)
log_debug(args.pluginUUID)
log_debug(args.event)
log_debug(args.info)
log_debug(args.propertyInspectorUUID)


def on_message(ws, raw_message):
    global macroUUID
    global instance_context
    global device_id
    message = json.loads(raw_message)
    log_debug("== got message" + raw_message)
    event = message['event']
    payload = message['payload']

    if (event == 'willAppear'):
        log_debug("Got view will appear")
        instance_context = message['context']
        log_debug("saving context " + message['context'])
        device_id = message['device']
        log_debug("saving device_id " + message['device'])
        settings = payload['settings']
        if 'macroUUID' in settings:
            log_debug("macro id is in settings, so saving that off")
            macroUUID = settings['macroUUID']

    if (event == 'keyUp'):
        Popen(['osascript', '-e', 'tell application "Keyboard Maestro Engine" to do script "' + macroUUID + '"'])

    if (event == 'sendToPlugin'):
        log_debug("setting settings")
        log_debug("Payload is:")
        log_debug(json.dumps(payload))
        if 'macroUUID' in payload:
            macroUUID = payload['macroUUID']
            save_settings_dict = {
                "event": "setSettings",
                "context": instance_context,
                "payload": payload
            }
            log_debug("Sending the following to the server")
            log_debug(json.dumps(save_settings_dict))
            ws.send(json.dumps(save_settings_dict))

        if 'property_inspector' in payload:
            log_debug("\n\nSending info to plugin!!!")
            send_to_pi_dict = {
                "action": "com.elgato.example.action1",
                "event": "sendToPropertyInspector",
                "context": instance_context,
                "payload": {"macroUUID": macroUUID}
            }
            log_debug(json.dumps(send_to_pi_dict))
            ws.send(json.dumps(send_to_pi_dict))


def on_error(ws, error):
    log_debug(error)


def on_close(ws):
    log_debug("### closed ###")


def on_open(ws):
    global registration_dict
    global pi_registration_dict
    log_debug("### open ###")
    ws.send(json.dumps(registration_dict))
    ws.send(json.dumps(pi_registration_dict))


if __name__ == "__main__":
    ws = websocket.WebSocketApp('ws://localhost:' + args.port,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
