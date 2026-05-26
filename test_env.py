from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("AZURE_CONNECTION_STRING"))