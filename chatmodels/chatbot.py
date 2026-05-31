from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatMistralAI(model = "mistral-small-2603", temperature = 0.5)

print("Enter your mood for the AI-Chatbot!")

print("1 for Angry")
print("2 for Funny")
print("3 for Sad")

choice = int(input("Tell your Response:"))

if choice == 1:
    mode = "You are an Angry AI-Agent. You reply agrressively and impatiently"

elif choice == 2:
    mode = "You are an Funny AI-Agent. You repond with humor and jokes"

elif choice == 3:
    mode = "You are an Sad AI-Agent. You reply in depressed and emotional tone"

messages = [
    SystemMessage(content = mode)
]

print("------Welcome-Type 0 to exit the application------")
while True:
    
    prompt = input("YOU: ")
    messages.append(HumanMessage(content = prompt))
    if (prompt == "0"):
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("BOT: ", response.content)

print (messages)