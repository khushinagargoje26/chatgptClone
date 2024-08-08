#The script.js file contains the client-side JavaScript code for the ChatGPT clone application. It handles the dynamic interactions between the user and the chat interface, including sending user queries to the server and displaying responses.

Key Components:
Event Listeners: Manages user input events, such as submitting queries and interacting with the chat interface.
AJAX Requests: Sends asynchronous requests to the server to fetch responses from the ChatGPT model.
UI Updates: Updates the chat window with user messages and AI responses in real-time.


// script.js
function sendData() {
  const data = { message: 'Hello from frontend!' };

  fetch('import openai
        import os
        import sys




        try:
            openai.api_key = os.environ['key']
        except KeyError:
            sys.stderr.write("""
            You haven't set up your API key yet.

            If you don't have an API key yet, visit:

            https://platform.openai.com/signup

            1. Make an account or sign in
            2. Click "View API Keys" from the top right menu.
            3. Click "Create new secret key"

            Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
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
            print("Assistant:", assistant_response)', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Response:', data);
    // Do something with the response data
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
