from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

text = "Hi, how are you?"
embedded_text = embeddings.embed_query(text)

print(embedded_text)    