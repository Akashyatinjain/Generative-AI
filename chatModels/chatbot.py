from langchain_core.prompts import message
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage ,SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.9
)

print("choose Your AI model type")
print("1. Funny AI")
print("2. Professional AI")
print("3. Romantic AI")
if(KeyboardInterrupt=="1"):
    print("You are a Funny AI")
    messages=[
        SystemMessage(content="You are a FUNNY Kinf of person,Please respond in a Funny manner")
    ]
if(KeyboardInterrupt=="2"):
    print("You are a Professional AI")
    messages=[
        SystemMessage(content="You are a Professional AI")
    ]
if(KeyboardInterrupt=="3"):
    print("You are a Romantic AI")
    messages=[
        SystemMessage(content="You are a Romantic AI")
    ]
print("-----------------------Welcome tryyyy 0 to exit the application----------------------------------")
while True:
    print("\n")
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt== "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:", response.content[0]["text"])
print(messages)