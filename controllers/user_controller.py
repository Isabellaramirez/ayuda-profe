from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_bcrypt import Bcrypt 

# Inicialización de bcrypt
bcrypt = Bcrypt()

# Blueprint para usuarios
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    connection = current_app.connection

    if request.method == 'POST':
        print("Datos recibidos:", request.form)
        
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        
        # Validación de campos
        if not (nombre and apellido and correo and contraseña):
            flash("Todos los campos son obligatorios.")
            return redirect(url_for('user_bp.registro'))
        
        hashed_password = bcrypt.generate_password_hash(contraseña).decode('utf-8')

        try: 
            with connection.cursor() as cursor:
                # Verifica si el correo ya existe
                cursor.execute("SELECT COUNT(*) FROM usuario WHERE correo = %s", (correo,))
                if cursor.fetchone()[0] > 0:
                    flash("El correo ya está en uso.")
                    return redirect(url_for('user_bp.registro'))

                # Inserta el nuevo usuario
                cursor.execute(
                    "INSERT INTO usuario (nombre, apellido, correo, contraseña) VALUES (%s, %s, %s, %s)", 
                    (nombre, apellido, correo, hashed_password)
                )
                connection.commit() 
            return redirect(url_for('bruno_bp.bruno'))  # Redirige a la página principal
        except Exception as e:
            print(f"Error: {str(e)}")  # Imprime el error en la consola
            flash(f"Error: {str(e)}")
            return redirect(url_for('user_bp.registro'))

    return render_template('registro.html')

@user_bp.route('/inicio_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        correo = request.form['correo']  
        contraseña = request.form['contraseña']

        connection = current_app.connection

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT contraseña FROM usuario WHERE correo=%s", (correo,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result['contraseña'], contraseña):  
                    session['persona_correo'] = correo
                    return redirect(url_for('bruno_bp.bruno'))  # Redirige a la página principal
                else:
                    return "Algo está mal"
        except Exception as e:
            return str(e)
            print(f"Error: {str(e)}")  # Imprime el error en la consola
            return f"Error: {str(e)}"  # También puedes mostrar el error en la respuesta
        
    return render_template('inicio_sesion.html')
