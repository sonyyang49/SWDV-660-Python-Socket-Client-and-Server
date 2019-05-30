#By Sony Yang
import socket

msg = ''

while msg.lower() != 'q':
    #defines the host ip and port.  
    host = '127.0.0.1'
    port = 9500

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    msg = input('Send a message to the host server or type "q" to exit: ')

    #sends the encoded input message to the server.  
    s.send(msg.encode('utf-8'))
    
    #receive and print the response from the server.  
    data = s.recv(1024)
    print(repr(data.decode()))     #decodes the msg.
    
s.close()
