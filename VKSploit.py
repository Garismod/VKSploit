#!/usr/bin/python3

import vk_api

def send_message(target_id, msg):
	vk.messages.send(user_id = target_id, message = msg, random_id = 0)
	print("[ + ] Запрос отправлен")
def friends_get():
	flist = str(vk.friends.get())
	fflist = flist.replace('[','').replace(']', '').replace(',', '').replace('{','').replace('}','')
	print(fflist)
def blacklist():
	i = vk.account.getBanned()
	print(i)
def info_get():
	inf = vk.account.getInfo()
	print(inf)
print("""


















██╗░░░██╗██╗░░██╗░██████╗██████╗░██╗░░░░░░█████╗░██╗████████╗
██║░░░██║██║░██╔╝██╔════╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝
╚██╗░██╔╝█████═╝░╚█████╗░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░
░╚████╔╝░██╔═██╗░░╚═══██╗██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░
░░╚██╔╝░░██║░╚██╗██████╔╝██║░░░░░███████╗╚█████╔╝██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░
[ + ] Author: XSelf
[ + ] Version: 1.0
[ + ] Country: Russia
[ + ] Language: english(сорян что не русский)

[ * ] Tokens site: https://oauth.vk.com/authorize?client_id=6121396&scope=476003870&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1
""")

token = input("Token: ")
print("\nLogs:")
session = vk_api.VkApi(token = token)
print(session)
vk = session.get_api()
print(vk)
print("""
	send_message <target_id> <msg> - request to send a message
	friends_get - request for a list of friends
	info_get - request to get account info
	info_get_blacklist - request to get blacklist
	exit - stop script
""")
while True:
	cmd = input("VKSploit > ").split(" ")
	if cmd[0] == "send_message":
		target_id = cmd[1]
		msg = cmd[2]
		send_message(target_id,msg)
	elif cmd[0] == "friends_get":
		friends_get()
	elif cmd[0] == "info_get_blacklist":
		blacklist()
	elif cmd[0] == "info_get":
		info_get()
	elif cmd[0] == "exit":
		quit()



