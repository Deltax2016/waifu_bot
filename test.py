'''import requests

query = {
      "option": "Hero Story Villian",
      "main_field_value": "я",
      "secondary_field_value": "поход в кино",
      "tone": "Empathetic"
    }
r = requests.post("http://212.193.50.2:777/two_field_tools", json=query)
print(r.json())
'''
from googletrans import Translator


translator = Translator()  # initalize the Translator object
translations = translator.translate(['see if this helps'], dest='ru')
for translation in translations:  # print every translation
    print(translation.text)