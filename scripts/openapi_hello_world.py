"""
This script creates a chat model using the OpenAI API for testing purposes
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Create a chat model with the OpenAI API key
model = ChatOpenAI(model="gpt-5-nano", temperature=0.5, api_key=os.getenv("OPEN_API_KEY_ALL"))

# Create a message to the model
message = model.invoke("Hello, world!")

# Print the model response
print(message.content)


# -------------
# Expect an answer like:
"""
Hello! Nice to meet you. How can I help today? If you’re into programming, I can show you how to print “Hello, world!” in different languages. For example:

- Python: print("Hello, world!")
- JavaScript: console.log("Hello, world!");
- C: #include <stdio.h> int main() { printf("Hello, world!"); return 0; }

Want another language or a different topic?
(venv) PS C:\GitHub\GuilhermeRuy97\langchain
"""

