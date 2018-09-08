import socket,time,threading, os ,sys

os.system('clear')

def receber():
	while True:
		msg = c.recv(1024).decode('utf-8')
		if len(msg) >=1:
			print('{}'.format(msg))

		if not msg: break

host=''
port=5001

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host,port))

t = threading.Thread(target=receber)
t.daemon=True
t.start()


name = input("Qual seu nome?")
name = '\033[1m\033[31m{}\033[0;0m'.format(name)
c.send(name.encode())
print()
while True:
	time.sleep(0.1)
	envio = input('')
	if envio.lower() == 'sair' or envio.lower() == "quit":
		c.close()
		print('\nSaindo...')

		time.sleep(0.5)
		print('Até a próxima. :)')
		break
	else:
		c.send(envio.encode())