import socket

ADDRESS = ('localhost', 4455) # IP Address of the hardware devices
FORMAT = "utf-8"
SIZE = 1024

def main():
    # Staring a TCP socket.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connecting to the server. 
    client.connect(ADDRESS)
    
    # Opening and reading the file data.
    file = open("xml_files/radio_data.xml", "r")
    data = file.read()
    
    # Sending the filename to the server.
    client.send("radio_data.xml".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    
    # Sending the file data to the server.
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    
    # Closing the file.
    file.close()
    
    # Closing the connection from the server.
    client.close()
if __name__ == "__main__":
    main()