"""
This script initializes a chat model using the Google Gemini API for testing purposes
"""

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Initialize the chat model
gemini = init_chat_model(model="gemini-2.5-flash-lite", api_key=os.getenv("GOOGLE_STUDIO_API_KEY"), model_provider="google_genai")

# Print the model response
gemini_response = gemini.invoke("Hello, world!")
print(gemini_response.content)

# -------------
# Expect an answer like:
"""
Hello there! How can I help you today?
"""