from flask import Blueprint, render_template
from flask import request
from flask import session
import openai
from .models import db, Resultado, Profile
from datetime import datetime
import plotly.express as px
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import bcrypt

openai.api_key = 'INSERT_YOUR_OPENAI_API_KEY_HERE'
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
    elif len(user_input) > 600:
        ChatResponse = "Remember that your essay should not overpass 600 words."
    else:
        ChatResponse = "Please enter a valid answer before submitting the form."

    user_email = session.get('user_email')
    time=datetime.now().strftime('%Y-%m-%d')
    gContent=grades_list[0]
    gOrganization=grades_list[1]
    gLanguage=grades_list[2]
    gGrammar=grades_list[3]
    new_result=Resultado(time=time,
                          gradeContent=gContent,
                          gradeOrganization=gOrganization,
                          gradeLanguage=gLanguage,
                          gradeGrammar=gGrammar,
                          user_email=user_email)
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
        # Generar una nueva sal y hashear la contraseña
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Crear un nuevo perfil con hasheo y salteo de la contraseña
        new_profile = Profile(name=name, lastname=lastname, email=email, password=hashed_password, salt=salt)
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

    # Consultar la base de datos para obtener el usuario por su correo electrónico
    user = Profile.query.filter_by(email=email).first()

    if user:
        # Obtener la sal almacenada
        salt = user.salt

        # Hashear la contraseña ingresada con la sal almacenada
        entry_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        if entry_password == user.password:
            # Si las contraseñas coinciden, almacenar la información del usuario en la sesión
            session['user_id'] = user.id
            session['user_email'] = user.email
            session['user_name'] = user.name

            # Redirigir a home.html u otra página
            return render_template('home.html')

    # Si las credenciales no son válidas, puedes redirigir a una página de error o mostrar un mensaje
    return render_template('error.html', message='Invalid email or password')

@main.route('/my_profile')
def my_profile():
    # Obtener información del usuario desde la sesión
    user_id = session.get('user_id')
    user_email = session.get('user_email')
    user_name = session.get('user_name')

    # Realizar una consulta a la base de datos para obtener los resultados del usuario
    user_results = Resultado.query.filter_by(user_email=user_email).all()

    # Obtener todos los resultados de la base de datos
    all_results = Resultado.query.all()
    # Calcular calificaciones promedio para cada rubro
    avg_grade_content = sum(result.gradeContent for result in user_results) / len(user_results) if user_results else 0
    avg_grade_organization = sum(result.gradeOrganization for result in user_results) / len(user_results) if user_results else 0
    avg_grade_language = sum(result.gradeLanguage for result in user_results) / len(user_results) if user_results else 0
    avg_grade_grammar = sum(result.gradeGrammar for result in user_results) / len(user_results) if user_results else 0
    # Redondear las calificaciones promedio a dos decimales
    avg_grade_content = round(avg_grade_content, 2)
    avg_grade_organization = round(avg_grade_organization, 2)
    avg_grade_language = round(avg_grade_language, 2)
    avg_grade_grammar = round(avg_grade_grammar, 2)

    # Crear gráficos con Plotly
    fig_content = create_plot(all_results, 'gradeContent', avg_grade_content, 'Content')
    fig_organization = create_plot(all_results, 'gradeOrganization', avg_grade_organization, 'Organization')
    fig_language = create_plot(all_results, 'gradeLanguage', avg_grade_language, 'Language')
    fig_grammar = create_plot(all_results, 'gradeGrammar', avg_grade_grammar, 'Grammar')

    # Crear gráfica en 3D para los clusters
    fig_clusters, user_cluster = create_clusters(all_results, avg_grade_content, avg_grade_organization, avg_grade_language)

    return render_template(
        'my_profile.html',
        user_id=user_id,
        user_email=user_email,
        user_name=user_name,
        user_results=user_results,
        avg_grade_content=avg_grade_content,
        avg_grade_organization=avg_grade_organization,
        avg_grade_language=avg_grade_language,
        avg_grade_grammar=avg_grade_grammar,
        fig_content=fig_content,
        fig_organization=fig_organization,
        fig_language=fig_language,
        fig_grammar=fig_grammar,
        fig_clusters=fig_clusters,
        user_cluster=user_cluster,
    )

def create_plot(results, column, user_avg, title):
    df = pd.DataFrame([(result.id, getattr(result, column)) for result in results], columns=['id', 'grade'])
    fig = px.histogram(df, x='grade', title=f'{title} Grades Distribution')

    # Agregar la línea vertical para la calificación promedio del usuario
    fig.add_vline(x=user_avg, line_dash="dash", line_color="#F56E28", annotation_text="Your Average")

    # Modificar la forma de la distribución a una curva suave con relleno naranja
    fig.update_traces(marker=dict(color='#007e83', opacity=0.7), selector=dict(type='histogram'))

    # Convertir la figura a HTML
    fig_html = fig.to_html(full_html=False)

    return fig_html

def create_clusters(all_results, avg_grade_content, avg_grade_organization, avg_grade_language):
    # Extraer características relevantes para el clustering
    features = np.array([[result.gradeContent, result.gradeOrganization, result.gradeLanguage, result.gradeGrammar] for result in all_results])

    # Aplicar el algoritmo K-medias
    kmeans = KMeans(n_clusters=3, random_state=0)
    clusters = kmeans.fit_predict(features)

    # Asignar los resultados del clustering a cada registro
    for i, result in enumerate(all_results):
        result.cluster = clusters[i]

    # Crear un DataFrame para Plotly Express
    df = pd.DataFrame(features, columns=['Content', 'Organization', 'Language', 'Grammar'])
    df['Cluster'] = clusters

    # Crear un DataFrame para el usuario
    user_df = pd.DataFrame([[avg_grade_content, avg_grade_organization, avg_grade_language, 0]], columns=['Content', 'Organization', 'Language', 'Grammar'])
    user_df['Cluster'] = 'Your grades'

    # Concatenar el DataFrame del usuario con el DataFrame principal
    df = pd.concat([df, user_df], ignore_index=True)

    # Calcular la distancia del centroide de cada clúster al vector de calificaciones promedio del usuario
    distances = []
    for i in range(3):
        cluster_center = kmeans.cluster_centers_[i][:3]  # Tomar solo las tres primeras dimensiones del centroide
        user_vector = np.array([avg_grade_content, avg_grade_organization, avg_grade_language])
        distance = np.linalg.norm(cluster_center - user_vector)
        distances.append(distance)

    # Obtener el número de clúster al que pertenece el usuario
    user_cluster = np.argmin(distances)

# Crear gráfica en 3D con colores específicos para cada cluster
    fig = px.scatter_3d(df, x='Content', y='Organization', z='Language',
                    color='Cluster',
                    color_discrete_map={0: 'yellow', 1: 'red', 2: 'green', 'Your grades': 'black'},
                    labels={'Cluster': 'Group'})

    return fig.to_html(full_html=False), user_cluster