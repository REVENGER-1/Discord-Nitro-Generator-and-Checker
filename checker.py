import requests
from threading import Thread
import telegram_send

count_threads = int(input('Enter threads count:'))

def validcheck():
    r = requests.get(url)
    if r.status_code == 200:
        with open('valid.txt', 'a') as f:
            f.write('https://discord.gift/' + link)
        print('Found valid nitro!')
        telegram_send.send(messages = ['Found valid gift! - ' + 'https://discord.gift/' + link])
    else:
        print('Link is invalid')

gifts = open('links.txt')
for link in gifts:
    url = 'https://discordapp.com/api/v6/entitlements/gift-codes/' + link + '?with_application=false&with_subscription_plan=true'
    validcheck()

def main():
    while True:
        validcheck()

for i in range(count_threads-1):
    Thread(target=main()).start()
