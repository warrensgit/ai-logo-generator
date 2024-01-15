from flask import Flask, request, render_template, jsonify
from openai import OpenAI
import os


app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

@app.route('/')
def index():
    return render_template('logo_generator.html')

@app.route('/generate_logo', methods=['POST'])
def generate_logo():
    user_input = request.form['logo_description']
    logo_prompt = f"Create a logo that {user_input}"

    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=logo_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        print("Raw OpenAI API Response:", response)  # Log the raw response
        # Assuming the response structure is as expected
        image_url = response.data[0].url
        return jsonify({'image_url': image_url})
    except Exception as e:
        print("Error:", e)  # Log any errors
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)