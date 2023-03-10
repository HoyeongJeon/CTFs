from pwn import *  # pip install pwntools
import json
import base64
import codecs
import sys

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]


'''
- for loop in 100 times
- make switch in Encoding(if -elif?)
- decode it depeding on Encoding
- to send = {"decode : "decoded messages"}
'''

while True:
    received = json_recv()
    if "flag" in received:
        print("Flag is...", received["flag"])
        sys.exit()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    decoded_msg = ""
    if received["type"] == "base64":
        decoded_msg = base64.b64decode(received["encoded"]).decode()
    elif received["type"] == "hex":
        decoded_msg = bytes.fromhex(received["encoded"]).decode()
    elif received["type"] == "rot13":
        decoded_msg = codecs.decode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        decoded_msg = bytes.fromhex(received["encoded"][2:]).decode()
    elif received["type"] == "utf-8":
        for c in received["encoded"]:
            decoded_msg += chr(c)
    to_send = {
        "decoded": decoded_msg
    }
    json_send(to_send)
