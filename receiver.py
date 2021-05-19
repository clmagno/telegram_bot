import requests
import json

responses = requests.get(f"https://api.telegram.org/bot1847416664:AAFz9XInjigAZ9gHA_SlvmdbIqV3dBbFyPA/getUpdates")
json_data = json.loads(responses.content)

for j in json_data['result']:
	if "message" in j.keys():
		sender_fn = j['message']['from']['first_name']
		try:
			sender_ln = j['message']['from']['last_name']
		except:
			sender_ln = ""
		try:
			entry = f"sender: {sender_fn} {sender_ln}\nmessage: {j['message']['text']}\n\n"
			# requests.get(f"https://api.telegram.org/bot1847416664:AAFz9XInjigAZ9gHA_SlvmdbIqV3dBbFyPA/sendMessage?chat_id=964021441&text={entry}")
		except:
			try:
				entry = f"sender: {sender_fn} {sender_ln}\ncaption: {j['message']['caption']}\n\n"
			except:
				entry = f"sender: {sender_fn} {sender_ln}\ncaption: not available\n\n"
			# requests.get(f"https://api.telegram.org/bot1847416664:AAFz9XInjigAZ9gHA_SlvmdbIqV3dBbFyPA/sendMessage?chat_id=964021441&text={entry}")
			# requests.get(f"https://api.telegram.org/bot1847416664:AAFz9XInjigAZ9gHA_SlvmdbIqV3dBbFyPA/sendPhoto?chat_id=964021441&photo={j['message']['photo'][0]['file_id']}")
		print(entry)
