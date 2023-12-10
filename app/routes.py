from flask import Blueprint, render_template
from flask import request
from flask import session
import openai
from .models import db, Resultado, Profile
from datetime import datetime

openai.api_key = 'API-KEY'
messages = [{"role": "system", "content": "You are an English language instructor who prepares people for the TOEFL certification exam"}]
this_user = ""

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    return render_template('home.html')

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

@main.route('/about_us')
def about_us():
    return render_template('about_us.html')

@main.route('/submit_writing_form', methods=['POST'])
def submit_writing_form():
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
        messages.append({"role": "user", "content": "From your response, tell me which was my evaluation from 0 to 10 in 'Content and relevance', 'Organization and structure', 'Language use and vocabulary' and 'Grammar and mechanics'. Reply to this message only with the 4 grades that my essay got, one for each of the evaluated skills, each number must be separated with ','. Make sure to not write anything else different from those 4 numbers separated by comas."})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= messages
        )
        Grades = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": Grades})
        grades_list = [grade for grade in Grades.split(',')]
    if len(user_input) > 600:
        ChatResponse = "Remember that your essay should not overpass 600 words."
    else:
        ChatResponse = "Please enter a valid answer before submitting the form."

    time=datetime.now().strftime('%Y-%m-%d')
    gContent=grades_list[0]
    gOrganization=grades_list[1]
    gLanguage=grades_list[2]
    gGrammar=grades_list[3]
    new_result=Resultado(time=time,
                          gradeContent=gContent,
                          gradeOrganization=gOrganization,
                          gradeLanguage=gLanguage,
                          gradeGrammar=gGrammar)
    db.session.add(new_result)
    db.session.commit()

    return render_template('writing_results.html', results=ChatResponse, gradeContent=gContent, gradeOrganization=gOrganization, gradeLanguage=gLanguage, gradeGrammar=gGrammar)

@main.route('/go_index', methods=['POST'])
def go_index():
    return render_template('index.html')    

@main.route('/see_results')
def see_results():
    resultados=Resultado.query.all()
    return render_template('see_results.html',
                           resultados=resultados)

@main.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@main.route('/submit_signup_form', methods=['POST'])
def submit_signup_form():
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    # Verificar si el correo ya está registrado
    existing_user = Profile.query.filter_by(email=email).first()

    if existing_user:
        # Si ya existe un usuario con el mismo correo, redirigir a la página de error
        return render_template('error.html', message='Email already registered, try log in.')
    else:
        # Si el correo no está registrado, crear un nuevo perfil
        new_profile = Profile(name=name, lastname=lastname, email=email, password=password)
        db.session.add(new_profile)
        db.session.commit()

        # Redirigir a la página de éxito
        return render_template('success.html')

@main.route('/login_form')
def login_form():
    return render_template('login.html')

@main.route('/submit_login_form', methods=['POST'])
def submit_login_form():
    email = request.form.get('email')
    password = request.form.get('password')

    # Consultar la base de datos para verificar las credenciales
    user = Profile.query.filter_by(email=email, password=password).first()

    if user:
        # Si las credenciales son válidas, almacenar la información del usuario en la sesión
        session['user_id'] = user.id
        session['user_email'] = user.email
        session['user_name'] = user.name

        # Redirigir a home.html o cualquier otra página
        return render_template('home.html')
    else:
        # Si las credenciales no son válidas, puedes redirigir a una página de error o mostrar un mensaje
        return render_template('error.html', message='Invalid email or password')

@main.route('/my_profile')
def my_profile():
    # Obtener información del usuario desde la sesión
    user_id = session.get('user_id')
    user_email = session.get('user_email')
    user_name = session.get('user_name')

    # Realizar otras operaciones según sea necesario
    return render_template('my_profile.html', user_id=user_id, user_email=user_email, user_name=user_name)
