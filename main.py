import json
import requests
from difflib import get_close_matches
import wikipedia
import pyttsx3
import winsound
import speech_recognition as sr

 #initializing assistant
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)
voicespeed = 170
assistant.setProperty('rate', voicespeed)

#fuction for speaking
def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        winsound.Beep(2000, 100)

    try:
        print('recognising...')
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print('')
        return '_______________________________________'
    return query
    

#loading the json file named knowledge_base.json
def load_knowledge_base(file_path):
    with open(file_path,'r') as file:
        data = json.load(file)
    return data

#saving new data to json file named knowledge_base.json
def save_knowledge_base(file_path,data):
    with open(file_path,'w') as file:
        json.dump(data, file, indent=2)
    
#here we use a mach for the quesion in the knowledge_base.json
#when a mach occurs the "question" will be returned
def find_best_mach(user_question,question):
    matches = get_close_matches(
        user_question,
        question,
        n=1,        #for repitation
        cutoff=0.7  #for the % of mach(0.7 = 70%)
    )
    return matches[0] if matches else None

#the above returned quesion again check and return the answer
def get_answer_for_question(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
#this is the main function
def chat_bot(user_input=None):
    knowledge_base = load_knowledge_base('knowledge_base.json')

    if user_input:
        user_input=user_input
    else:
        user_input = input("You: ")
    if user_input.lower() == 'quit':
        pass

    best_mach = find_best_mach(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_mach:
        answer = get_answer_for_question(best_mach, knowledge_base)
        #this is like swich in c program and it is used to avoid elif lader
        match answer:
            case '__joke__':
                data = requests.get(r"https://official-joke-api.appspot.com/random_joke")  # noqa
                joke = json.loads(data.text)
                print(f'Bot: {joke["setup"]}\n         {joke["punchline"]}')
                text= f'{joke["setup"]}{joke["punchline"]}'
                speak(text)
            case '__time__':
                data = requests.get(r"https://timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata")  # noqa
                time = json.loads(data.text)
                text= f'Bot: {time["time"]}'
                print(text)
                speak(text)
            case _:     #this is the default case; means no maching case
                text=f'{answer}'
                print(text)
                speak(text)

    #this block of code will execute when there is no data in the knowledge_base.json file
    else:
        print(f"Bot: I don't know the answer. Do you wand me look for the ansewer in the internet insted?")

        new_answer= input('Type "Yes" for continue or "No" to skip:')

        #added wikipedia module for searching data online
        if new_answer.lower() in ["yes","y"]:
            wikipedia.set_lang('es')
            text=f'y{wikipedia.summary(user_input)}'
            print(text)
            speak(text)
        elif new_answer.lower() in ["no","n"]:
            #this is for added a new response; means adding data into the knowledge_base.json file
            print(f"Bot: So can you teach me the answer?")
            new_answer= input('Type your answer or "skip" to skip:')
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer" : new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you! I learned a new response!")

if __name__ == '__main__':
    #chat_bot()
    while True:
        text=takecommand()
        if text != '_______________________________________':

            chat_bot(text)

        else:
            print('_______________________________________')