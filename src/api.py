from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)
api = Api(app)

# MySQL configurations
app.config['MYSQL_DATABASE_ID']='dbuser'
app.config['MYSQL_DATABASE_PASSWORD']='dbuser_password'
app.config['MYSQL_DATABASE_DB']='mysql_db_name'
app.config['MYSQL_DATABASE_HOST']='mysql_host_name'
mysql.init_app(app)

api = Api(app)

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id',type=str)
            parser.add_argument('password',type=str)
            args = parser.parse_args()

            _userId = args['id']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_create_user',(_userId,_userPassword))
            data = cursor.fetchall()

            if(len(data)>0):
                if(str(data[0][2])==_userPassword):
                    return{'status':200,'message':'User Creation success'}
                else:
                    return{'status':100,'message':'Authentication failure'}

        except Exception as e:
            return{'error':str(e)}

api.add_resource(CreateUser,'/user/account/signup')

if __name__ == '__main__':
    app.run(debug=True)