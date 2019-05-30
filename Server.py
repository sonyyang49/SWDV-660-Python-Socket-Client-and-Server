#By Sony Yang
import socket                
  
#define the socket object.
s = socket.socket()          
print("Socket successfully created")
  
# defines the host ip and port
host = '127.0.0.1'
port = 9500                
  
# Bind to the port 
s.bind((host, port))         
print("The Socket has successfully binded to host {} and port {}".format(host, port)) 
  
# puts the socket into listening mode 
s.listen(5)      
print("Socket is listening on port ", port)            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True:
    # Establish connection with client. 
    conn, addr = s.accept()      
    print('Got connection from', addr)
    
    #receives and decodes message from the client. 
    msg_rec = conn.recv(1024)
    msg_str = msg_rec.decode()
    print(msg_str)
    
    #resonds with a 'Hi' to client if client sends 'Hello'
    #Else respond with 'Goodbye'
    if msg_str.lower() == "hello":
        conn.send(b'Hi')
    
    else:
        conn.send(b'Goodbye')
  
    # Close the connection with the client if the client quits. 
    conn.close() 