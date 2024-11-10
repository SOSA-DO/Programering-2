import socket

host = '127.0.0.1'
port = 64321

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as croqueta:
    croqueta.bind((host,port))
    print('I am listening!')
    
    
    while True:
        data, addr = croqueta.recvfrom(1024)
        print(f'{data.decode('utf-8')}')
        
        message = 'Hello from server'
        
        croqueta.sendto(message.encode('utf-8'),addr)

        
