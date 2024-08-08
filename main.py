The main.py file is the core of the ChatGPT clone application. It contains the main code for the Flask web server and handles communication between the frontend and the OpenAI API. This file imports necessary modules and sets up the routes for handling user interactions.

Key Components:
Imports: Includes modules such as Flask for web server functionality, requests for API calls, and dotenv for loading environment variables.
API Key: The OpenAI API key is securely loaded from a .env file to authenticate requests to the OpenAI service.
Routes: Defines the endpoints for serving the chat interface and processing user queries.




import openai
import os
import sys




try:
    openai.api_key = os.environ['key']
except KeyError:
    sys.stderr.write("""


    1.
    2. 
    3. 
    """)
    exit(1)

while True:
    user_input = input("User: ")

    if user_input == "exit":
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )

    assistant_response = response.choices[0].message["content"]
    print("Assistant:", assistant_response)
