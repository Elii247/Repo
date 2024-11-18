from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'  # Cambia esto a una clave secreta más segura en producción

# Simulando una base de datos simple
usuarios = {
    "usuario1": {"password": "12345", "email": "usuario1@ejemplo.com"},
    "usuario2": {"password": "abcde", "email": "usuario2@ejemplo.com"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios[username]['password'] == password:
        return f"Bienvenido, {username}!"
    else:
        flash("Usuario o contraseña incorrectos, intente de nuevo.")
        return redirect(url_for('login_page'))

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if username in usuarios:
        flash("Este nombre de usuario ya existe.")
        return redirect(url_for('signup'))
    else:
        usuarios[username] = {"password": password, "email": email}
        flash("Cuenta creada exitosamente.")
        return redirect(url_for('login_page'))

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form['email']

    # Verificar si el correo está registrado
    for user, info in usuarios.items():
        if info['email'] == email:
            return f"Se ha enviado un enlace para restablecer la contraseña a {email}"
    flash("Correo no encontrado, intente de nuevo.")
    return redirect(url_for('forgot_password'))

if __name__ == '__main__':
    app.run(debug=True)
