from art import text2art
from termcolor import colored
import requests
from random import choice

base_url = "https://icanhazdadjoke.com"

TEXT = colored(text2art('Dad Joke 3000'), 'magenta')
print(TEXT)

user_inp = input("Let me tell you a joke! Give me a topic: ")

url = f'{base_url}/search'

try:
    res = requests.get(url=url, params={'term': user_inp}, headers={
                       'Accept': 'application/json'})
except:
    print(colored('Request Failed!', color='red', attrs=['bold', 'underline']))
else:
    data = res.json()
    jokes_len = data['total_jokes']
    plural = "s" if jokes_len != 1 else ''

    if jokes_len == 0:
        print(
            f"Sorry, I don't have any jokes about '{user_inp}'! Please try again.")
    else:
        joke = choice(data['results'])['joke']

        print(
            f"I've got {jokes_len} joke{plural} about '{user_inp}'. Here's one:")
        print(f'"{joke}"')
