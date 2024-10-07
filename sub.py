import socket

def main():
    # Create or open the file for writing
    with open("output.txt", "wb") as file:
        # Establish a TCP connection to the server
        stream = socket.create_connection(("prem-pt1.365lpodds.com", 443))

        # Send the message (topic subscriptions)
        message = b"#\x03P\x01__time,OVInPlay_1_1,S_6FBFB48A1ECC4DAAABC91F676584DC1A000003\x00"
        stream.sendall(message)
        print(f"Sent: {message.decode('utf-8', errors='ignore')}")

        while True:
            # Read data from the stream
            buffer = stream.recv(1024)
            if not buffer:
                break
            # Write the received data to the file
            file.write(buffer)

if __name__ == "__main__":
    main()
