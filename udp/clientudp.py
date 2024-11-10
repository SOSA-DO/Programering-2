import socket

host = '127.0.0.1'
port = 64321

# skapa en socket och definera att det är udp
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:

    # Meddelande att skicka
    message = "Hello from client code!"

    # Skicka meddelandet till servern
    udp_socket.sendto(message.encode(), ('127.0.0.1', 64321))
    print(f"Meddelande skickat till server, {'127.0.0.1'}:{64321}")

    # Ta emot svar från servern (storlek 1024 byte)
    response, server_address = udp_socket.recvfrom(1024)
    print(f"Svar från servern: {response.decode('utf-8')}")

    # Stäng socketen
    udp_socket.close()