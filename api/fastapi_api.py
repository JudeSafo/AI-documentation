import os
from fastapi import FastAPI, HTTPException
import requests
MAX_INPUT_LENGTH = 32

app = Flask(__name__)

# Set the API key
api_key = os.environ['OPEN_AI'] 

@app.route('/gpt', methods=['POST'])
def generate_response():
    # Get the prompt from the request body
    prompt = request.json['prompt']

    # Make the API call
    response = requests.post("https://api.openai.com/v1/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
    	    "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 200,
            "stop": None,
            "temperature": 0.5,
        }
    )

    # Get the response text
    response_text = response.json()["choices"][0]["text"]

    # Return the response text as JSON
    return jsonify(response_text)

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.",
        )
if __name__ == '__main__':
    app.run(debug=True)

