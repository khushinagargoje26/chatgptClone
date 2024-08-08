The flask_app.py file sets up and configures the Flask framework for the ChatGPT clone application. It initializes the Flask application, defines the main routes, and manages the server-side logic required to handle user interactions and API requests.

Key Components:
Flask Initialization: Sets up the Flask app instance and configures essential settings.
Routes: Defines the HTTP routes for rendering the chat interface and processing user messages.
API Integration: Manages communication with the OpenAI API to fetch responses based on user input.


from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key for GPT-3.5
api_key =  os.environ['key']

@app.route('/generate_chat_response', methods=['POST'])
def generate_chat_response():
    data = request.get_json()
    prompt = data['prompt']
    response = generate_response(prompt)
    return jsonify({'response': response})

def generate_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the GPT-3.5 engine
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)
