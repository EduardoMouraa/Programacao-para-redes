import socket, _thread, time, os
from envios import *

def funcao(con, client):
	
	print(client[0],'\033[1m\033[31mse conectou no servidor!\033[0;0m')

	rec = con.recv(1024).decode('utf-8')

#======================--Guardando conexões e nomes--====================================#
	if con not in clientes:
		clientes[con] = [rec]

	if con not in online:
		online[con] = rec
#======================--Guardando conexões e nomes--====================================#

#---função para usuarios online----#
	Online(online, con)

#---função para avisar que o usuario se conectou no chat------#
	Con_user(clientes,con, rec, mensagens)

	

#================================reconstruir bate papo====================================================#
	BatePapo(clientes, mensagens, con)
#===========================^=====reconstruir bate papo===^===============================================#

	mensagens.append('\n'+rec+'\033[1m\033[31m se conectou ao chat!!\033[0;0m')
	while True:
		
		msg = con.recv(1024).decode('utf-8')
		if len(msg) >=1: 
			mensagens.append('\n'+rec+': '+msg)
#----função para enviar mensagens para os usuarios---------#
		Enviar(clientes, con, msg, rec)

		if not msg:
			mensagens.append('\n'+rec+"\033[1m\033[31m se desconectou do servidor!!\033[0;0m")
			#----função para avisar que usuario se desconectou----#
			Desconect(clientes, con, rec)
			del online[con] ; del clientes[con]
			break

	print(client[0],'\033[1m\033[31mse desconectou do servidor!\033[0;0m')
	con.close()
#===========================^=====recebimento e envio das msg===^=========================================#

os.system('clear')

host= ''
port = 5001

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind((host,port))

clientes = {}
mensagens = []
online = {}


serv.listen(5)

print("\033[1m\033[31mSERVIDOR INICIADO!!\033[0;0m")
while True:

	con, client = serv.accept()
	_thread.start_new_thread(funcao, tuple([con, client]))
serv.close()