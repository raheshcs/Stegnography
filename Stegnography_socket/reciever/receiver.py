import socket
import os
# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')
# Send a greeting to the server
sock.send('A message from the client'.encode())

# Write File in binary
di=input(str("CD:"))
os.chdir(di)
while True:
     frec=input(str("Enter the file received:"))
     file = open(frec, 'wb')
     line = sock.recv(1024)
     while(line):
          file.write(line)
          line = sock.recv(1024)
     file.close()
     print('File has been received successfully.')
     break
sock.close()
print('Connection Closed.')
os.system("python stegbyte.py")
