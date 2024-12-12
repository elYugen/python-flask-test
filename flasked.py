from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from markupsafe import escape

app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8znxec]'

@app.route('/') # défini une route
def index(): # nomme cette route dans une fonction
    if 'username' in session:
        return f'connecté en tant que {session["username"]}'
    return "tu n'es pas co <a href='login'>co toi ici</a>"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/hello")
def hello():
    if 'username' in session:
        username = session['username']
        return render_template('hello.html', username=username)
    return redirect(url_for('index'))

# @app.route("/<name>") # défini une route avec un parametre dans l'url
# def coucou(name): # passe le parametre dans la fonction
#     return f"coucou, {escape(name)}!" # rajoute escape pour éviter les injection dans l'url (avec du js par exemple)    
#                                         # cela va retourner du texte a la place

@app.route("/user/<username>")
def showUserProfile(username):
    return f"Utilisateur : {escape(username)}"

@app.route('/post/<int:post_id>') # passe une variable en parametre 
def showPost(post_id):            # donner le type de variable permet de filtrer les entrée (ex : int ne va prendre que les integer et pas de caractère)
    return f"Publication avec l'id : {post_id}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('hello'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # suppr l'username de la session si il existe
    session.pop('username', None)
    return redirect(url_for('index'))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('showUserProfile', username="Jean"))