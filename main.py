import google.generativeai as genai
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CONTEXT = 'Responda como um atendente de restaurante'
error_message = ''

try:
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
except Exception as error:
    error_message = f'Erro ao carregar o modelo: {error}'


@app.route('/')
def index():
    if len(error_message) == 0:
        return render_template('index.html')
    else:
        return {'message': error_message}


@app.route('/search')
def search():
    prompt = request.args.get('prompt')
    try:
        input_ia = f'{CONTEXT}: {prompt}'
        output = model.generate_content(input_ia)
        return {'message': output.text}
    except Exception as ex:
        print(f'Erro ao gerar a resposta: {ex}')
        return 'Ocorreu um erro ao processar sua solicitação.'


if __name__ == '__main__':
    app.run(debug=True)
