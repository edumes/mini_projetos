from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from spacy.cli import download
download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


chatbot = ChatBot('gg', tagger=language='pt-BR')