from googletrans import Translator

with open('text_4.txt', 'r', encoding='utf-8') as lang:
    for line in lang:
        translator = Translator()
        result = translator.translate(line, src='en', dest='ru')
        with open('translate.txt', 'a+', encoding='utf-8') as tr:
            tr.write(result.text + '\n')
            print(tr.read())
