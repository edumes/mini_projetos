from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

bot = ChatBot('bot', read_only=True, tagger_language=ENGSM)

trainer = ListTrainer(bot)


for arq in os.listdir('conversas'):
    chats = open('conversas/' + arq, 'r').readlines()
    trainer.train(chats)

while True:
    resq = input('>>>: ')

    resp = bot.get_response(resq)
    print('bot: ' + str(resp))