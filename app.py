from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

def get_bot_response(message):
    # Basic rule-based response, replace this with ML model logic
    if 'hello' in message.lower():
        return 'Hello! How can I help you today?'
    elif 'bye' in message.lower():
        return 'Goodbye! Have a nice day!'
    else:
        return 'I am sorry, I do not understand.'

if __name__ == '__main__':
    app.run(debug=True)
