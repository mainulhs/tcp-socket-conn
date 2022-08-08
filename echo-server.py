import socket

PORT = 4455 # Port for client connection
ADDRESS = ('', PORT) # Take local IP address
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting.") # Staring a TCP socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Bind the IP and PORT to the server.
    
    server.bind(ADDRESS) # Server is listening, i.e., server is now waiting for the client to connected.
    
    server.listen()
    print("[LISTENING] Server is listening.")
    
    while True:        
        #Server has accepted the connection from the client.
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        # Receiving the filename from the client.
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT)) 
        
        # Receiving the file data from the client.
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT)) 
        
        # Closing the file.
        file.close()
        
        # Closing the connection from the client.
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        
if __name__ == "__main__":
    main()