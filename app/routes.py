from flask import Blueprint, render_template
from flask import request
import openai

openai.api_key = 'AQUI-TU-CLAVE'
messages = [{"role": "system", "content": "You are an English language instructor who prepares people for the TOEFL certification exam"}]

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/writing')
def writing():
    user_input = "Reply to this message only with a topic suggestion for writing an essay. Your response must have the structure 'Suggested topic: [INSERT HERE THE TOPIC]'"
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
    )
    ChatResponse = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": ChatResponse})
    return render_template('writing.html', topic=ChatResponse)

@main.route('/reading')
def reading():
    return render_template('reading.html')

@main.route('/submit_form', methods=['POST'])
def submit_form():
    user_input=request.form.get('user_input')
    if user_input != "" and len(user_input) > 50:
        messages.append({"role": "user", "content": user_input})
        messages.append({"role": "user", "content": "This is my essay. Evaluate from 0 to 10 the next skills: 1. Content and relevance, 2. Organization and structure, 3. Language use and vocabulary, 4. Grammar and mechanics. Be sure to conclude with an overall rating from 0 to 10."})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= messages
        )
        ChatResponse = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": ChatResponse})
    else:
        ChatResponse = "Please enter a valid answer before submitting the form."

    return render_template('writing_results.html', results=ChatResponse)

@main.route('/go_index', methods=['POST'])
def go_index():
    return render_template('index.html')    
