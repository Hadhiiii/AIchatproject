import json
import requests
from difflib import get_close_matches

def load_knowledge_base(file_path):
    with open(file_path,'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(file_path,data):
    with open(file_path,'w') as file:
        json.dump(data, file, indent=2)
    

def find_best_mach(user_question,question):
    matches = get_close_matches(
        user_question,
        question,
        n=1,
        cutoff=0.7
    )
    return matches[0] if matches else None

def get_answer_for_question(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        

def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        best_mach = find_best_mach(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_mach:
            answer = get_answer_for_question(best_mach, knowledge_base)
            if answer == '__joke__':
                data = requests.get(r"https://official-joke-api.appspot.com/random_joke")  # noqa
                joke = json.loads(data.text)
                print(f'Bot: {joke["setup"]}\n         {joke["punchline"]}')
            elif answer == '__time__':
                data = requests.get(r"https://timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata")  # noqa
                time = json.loads(data.text)
                print(f'Bot: {time["time"]}')
            else:
                print(f'Bot: {answer}')
        else:
            print(f"Bot: I don't know the answer. Can you teach me?")
            new_answer= input('Type your answer or "skip" to skip:')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer" : new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you! I learned a new response!")

if __name__ == '__main__':
    chat_bot()