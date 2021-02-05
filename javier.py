import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyttsx3
import requests

ouvinte = sr.Recognizer() #definindo uma variável para ouvir
engine = pyttsx3.init() #iniciando com uma variável para poder transformar texto em voz
voices = engine.getProperty("voices") #definindo a voz
engine.setProperty('voice', voices[0].id)
wikipedia.set_lang('pt')

#criando uma função onde você insere o texto e o pyttsx3 converte em som.
def falar(texto):
    engine.say(texto) #aqui, quando houver um texto, o engine vai transformar esse texto em voz
    print(texto)
    engine.runAndWait() #vai falar e esperar

#criando uma função onde tem um input da sua voz através do speech recognizer, printa ele e depois o pttsx3 fala.
def tomar_comando():
    try:
        with sr.Microphone() as fonte: #aqui estamos colocando o microfone como fonte do input, no caso a minha voz
            print('Ouvindo...')
            audio = ouvinte.listen(fonte) #criando a fonte audio, ou seja, ele vai ouvir o que foi dito e armazenado como fonte
            comando = ouvinte.recognize_google(audio, language='pt-BR') #o comando vai reproduzir o audio, settado em PTBR
            if 'roda' in comando:
                comando = comando.replace('roda','')
                print(comando)

    except:
        pass
    return comando

def rodai():
    comando = tomar_comando()
    print(comando)
    if 'toque' in comando:
        musica = comando.replace('toque', '')
        falar('Tocando ' + musica)
        pywhatkit.playonyt(musica)
    elif 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        falar('Agora no horário de Brasília ' + hora)
    elif 'data' in comando:
        dia = datetime.datetime.now().strftime('%d do %m de %Y')
        falar("Hoje é: " + dia)
    elif 'pesquise' in comando:
        coisa = comando.replace('pesquise','')
        info = wikipedia.summary(coisa, 2)
        falar(info)
    elif 'temperatura' in comando:
        api = 'f454b6de88f24007ba428341f2f82711'
        url = ' http://api.openweathermap.org/data/2.5/weather?appid=f454b6de88f24007ba428341f2f82711&units=metric&id=3451190'
        #cidade = input('Nome da Cidade:')
        json_data = requests.get(url).json()
        humidade = json_data["main"]['humidity']
        temp = json_data["main"]['temp']
        sensacao = json_data["main"]['feels_like']
        tempo = ('Agora no Rio de Janeiro,  a temperatura é de {}°, com sensação térmica de {}. Já a humidade está em {}%.'.format(temp, sensacao, humidade))
        falar(tempo)
    else:
        falar('Não entendi. Por favor, mestre, diga novamente o que deseja.')


while True:
    rodai()