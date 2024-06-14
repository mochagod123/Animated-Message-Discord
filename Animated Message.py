from discord_webhook import DiscordWebhook
from time import sleep

url = input("WebHookURLを入れてください: ")
msg = input("元のメッセージを入力: ")
msg2 = input("変更後のメッセージを入力: ")

print(f"{msg} -> {msg2}")

webhook = DiscordWebhook(url=url, content=msg)
webhook.execute()
while True:
	webhook.content = msg2
	sleep(0.5)
	webhook.edit()
	webhook.content = msg
	sleep(0.5)
	webhook.edit()