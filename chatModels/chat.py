from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash",temperature=0,max_output_tokens=150)

response = model.invoke("Describe any horror story in 100 words.")

print(response)