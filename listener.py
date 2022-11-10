import socket
listener=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('localhost',4444))
listener.listen()
print('Listener has initiated')
connection,address=listener.accept()
print(f"[+] CONNECTION FROM {address}")
while True:
    commands=input("Enter the cmd: ")
    commands=bytes(commands,'utf-8')
    connection.send(commands)
    output=connection.recv(2048).decode('utf-8')
    print(output)
