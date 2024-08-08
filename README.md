ChatGPT Clone
This project is a ChatGPT clone developed as a final year college project. It leverages OpenAI's API to deliver an interactive conversational AI experience. The application is built using Python with Flask for the backend, and HTML, JavaScript, and CSS for the frontend.

Features
Interactive Chat Interface: A user-friendly web interface that allows for real-time conversation with the ChatGPT model.
Secure Authentication: Login page for user authentication and session management.
Real-Time Responses: Utilizes OpenAI's API to generate and display responses dynamically based on user input.
Responsive Design: Optimized for various devices to ensure a seamless user experience.
Technologies Used
Backend: Python, Flask
Frontend: HTML, JavaScript, CSS
API: OpenAI API
Installation
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/chatgpt-clone.git
Navigate to the Project Directory:
bash
Copy code
cd chatgpt-clone
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Set Up API Key:
Create a .env file in the root directory and add your OpenAI API key:
makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
Run the Flask Application:
bash
Copy code
python main.py
Access the Application:
Open your web browser and navigate to http://localhost:5000 to interact with the chat interface.
Usage
Login: Use the login page to authenticate and access the chat feature.
Chat: Enter your queries in the chat input field and press "Send" to receive responses from the ChatGPT model.
File Descriptions
main.py: Contains the Flask application setup, routes, and API integration.
script.js: Manages client-side interactions, including sending messages and updating the chat window.
chat.html: Provides the HTML structure for the chat interface.
log.html: Contains the HTML code for the login page.
style.css: Styles the login page and chat interface, including layout, typography, and color scheme.
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenAI for providing the ChatGPT model and API.
Flask for the web framework.
