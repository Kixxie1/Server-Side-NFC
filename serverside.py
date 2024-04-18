import socket 
 
host = "" 
port = 5000 
 
s = socket.socket() 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # avoid reuse error message 
s.bind((host, port)) 
 
print("Server started. Waiting for connection...") 
s.listen() 
c, addr = s.accept() 
print("Connection from:", addr) 
 
# Receive data from the client 
data = c.recv(1024) 
if not data: 
    print("No data received.") 
else: 
    # Write the received data to a Notepad file 
    with open("received_data.txt", "w") as txt_file: 
        txt_file.write(data.decode())  # Decode the bytes data to a string before writing 
    print("Received data saved as 'received_data.txt'.") 
 
# Close the connection 
c.close() 
print("Disconnected. Exiting.") 
