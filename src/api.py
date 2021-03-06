from flask import Flask, jsonify, request,session
from flask.json import JSONEncoder

app = Flask(__name__)
app.secret_key = 'qwer1234'

@app.route('/user',methods=['POST'])
def signup():
    user = []
    user.append({
        'id' : 'wnajsldkf',
        'password' : '1234'        
    })
    return{'StatusCode' : 200, 'message' : 'User Account successfully created'}
    
# 접속시 session에 id 유무 확인
@app.route('/')
def index():
    if 'id' in session:
        return ('이미 로그인된 상태입니다.')
    else:
        return ('로그인 되지 않았습니다.')  

@app.route('/signin',methods=['POST'])
def signin():
    try:
        # 로그인 성공
        session['id'] = 'wnajsldkf'
        return {'StatusCode' : 200, 'message':'User login in completed.'}
    except:
        # 잘못된 비밀번호
        return {'StatusCode' : 409, 'message':'You entered wrong password.'}
        # 아이디가 없을 때
    else:
        return {'StatusCode' : 404, 'message':'There is no ID'}
    
@app.route('/user/signout')
def signout():
    try:    
        session.pop('id',None)
        return {'StatusCode' : 200, 'message' : 'User Logout is completed'}
    except:
        return {'StatusCode' : 400, 'message' : 'This ID had not been logged in'}

if __name__ == '__main__':
    app.run(debug=True)