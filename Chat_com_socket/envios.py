import time

def Desconect(dic, user, name):
	for c in dic:
		try:
			if c != user:
				c.send((name+"\033[1m\033[31m se desconectou do servidor!!\033[0;0m").encode())
		except:
			pass

def Online(online, user):
	people = ''

	for q in online:
		try:
			if q != user:
				people += online[q] + ', '
		except:
			pass

	if len(people) != 0:
		user.send( ('\033[1m\033[31mPessoas ON no chat: {}\033[0;0m \n'.format(people[0:-2]) ).encode() )
	else:
		user.send( ('\033[1m\033[31mNinguém está ON no chat. :c\033[0;0m \n').encode() )


def Enviar(dic, user, msg, name):
	for c in dic:
		try:
			if c != user:
				if len(msg) >=1:
					envio =  '{}: {}'.format(name,msg)
					c.send(envio.encode())
		except:
			pass

def BatePapo(dic, mensagens, user):

	if len(dic) > 1:
		for i in dic:
			for n in mensagens:
				try:
					if i != user and len(dic[i]) >= 1:
							user.send(n.encode())
				except:
					pass

	if len(dic) == 1 and len(mensagens) > 0:
		for c in dic:
			for m in mensagens:
				try:
					c.send(m.encode())
				except:
					pass

def Con_user(dic, user, name, mensagens):
	for y in dic:
		try:
			if y != user:
				y.send((name+'\033[1m\033[31m se conectou ao chat!!\033[0;0m').encode())
		except:
			pass