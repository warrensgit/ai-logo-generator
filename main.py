from flask import Flask, request, render_template
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

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=user_input,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return jsonify({'image_url': image_url})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

