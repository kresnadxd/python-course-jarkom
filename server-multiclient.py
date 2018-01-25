import socket
import threading
import logging
import __future__

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def handle_client(sock_client, addr):
    logging.debug('koneksi klien diterima dari : {}'.format(addr))
    message = ''
    while message.find('bye') == -1:
        message = sock_client.recv(1024)
        hitung=eval(compile(message, '<string>', 'eval',__future__.division.compiler_flag))
        hitung = 'Jawaban : {}'.format(hitung)
        sock_client.send(hitung)
    sock_client.close()

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(('127.0.0.1',9999))
sock_server.listen(5)
clients = []
while True:
    try:
        s, a = sock_server.accept()
        t_client = threading.Thread(target=handle_client, args=(s,a))
        t_client.start()
        t_client.join(1)
        clients.append(t_client)
    except Exception as e:
        logging.debug(e)
        break
    except KeyboardInterrupt as k:
        break
