import telnetlib
import json
import base64
import codecs

decryption_function = {
    'base64': lambda x: base64.b64decode(x).decode('utf-8'),
    'hex': lambda x: bytes.fromhex(x).decode('utf-8'),
    'rot13': lambda x: codecs.encode(x, "rot13"),
    'bigint': lambda x: bytes.fromhex(x[2:]).decode("utf-8"),
    'utf-8': lambda x: ''.join([chr(y) for y in x])
}

#only need to establish one connection, was reestablishing a 
#connection with this included in the for loop

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

for z in range(101):
    received = json_recv()
    if "flag" in received:
        print(f"FLAG: {received['flag']}")
        break
    encoding = received["type"]
    cipher  = received["encoded"]

    if encoding in decryption_function:
        x = decryption_function[encoding](cipher)
        
    to_send = {
        "decoded": x
    }

    print(to_send)
    json_send(to_send)
    
    

