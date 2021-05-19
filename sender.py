import requests

text="Paunawa po, ang mga awit po na sinend sa atin ay maeexpire ng kusa matapos ang linggong ito. Ang mga ito po ay nakasecure at wala pong ibang makaviview nito kundi tayo lamang po na sinend-an ng link nito. Pakaingatan po natin ito."
chat_dict={'Chris':964021441,'Michelle V':1042463303,'Jun':1226426318, 'Lita':1661930147, 'Paul':327852044,'Elmer':1515575432, 'Ivy S':937470352, 'Ivy E':1786457412, 'Eden':238577774}
# chat_dict={'chris':964021441}
def getKey(d,val):
	return [k for k, v in d.items() if v==val]

for chat_id in [y for y in chat_dict.values()]:
    requests.get(f"https://api.telegram.org/bot1847416664:AAFz9XInjigAZ9gHA_SlvmdbIqV3dBbFyPA/sendMessage?chat_id={chat_id}&text={text}")
    print(f"message sent to Ka {getKey(chat_dict,chat_id)[0]}")