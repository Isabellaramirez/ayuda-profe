from flask import Flask
import pymysql.cursors
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
        
    )

    from app.controllers.user_controller import user_bp
    app.register_blueprint(user_bp)

   # from app.controllers.user_controller import user_bp
   # app.register_blueprint(user_bp, url_prefix='/inicio_sesion')

    from app.controllers.bruno_controller import bruno_bp
    app.register_blueprint(bruno_bp, url_prefix='/bruno')

    from app.controllers.rifa_controller import rifa_bp
    app.register_blueprint(rifa_bp, url_prefix='/rifa')

    from app.controllers.conoceme_controller import conoceme_bp
    app.register_blueprint(conoceme_bp, url_prefix='/conoceme')

    from app.controllers.donar_controller import donar_bp
    app.register_blueprint(donar_bp, url_prefix='/donar')


    app.connection = connection

    return app