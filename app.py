# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# @app.route('/home')
# def home():
#     return 'Hello, World!'
# @app.route('/user')
# def user():
#     return 'Hello, User!'
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# @app.route('/home')
# def home():
#     return '''
#     <h1>이건 h1 제목</h1>
#     <p>이건 p 본문 </p>
#     <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
#     '''
# @app.route('/user/<user_name>/<int:user_id>')
# def user(user_name, user_id):
#     return f'Hello, {user_name}({user_id})!'
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, url_for, flash, redirect
# from forms import RegistrationForm
# app = Flask(__name__)
# app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'
# @app.route('/')
# def home():
#     return render_template('layout.html')
# @app.route('/register', methods=["GET", "POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger) 
#         flash(f'{form.username.data} 님 가입 완료!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', form=form)
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['POST','GET'])
def login():
    if  request.method == 'POST':
        user = request.form['myName']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('myName')
        return redirect(url_for('success', name=user))
        # postman 
        # Set POST
        # Set Address -> 0.0.0.0:8080/login
        # Set Body - form-data -> key / value (myName / ned)
        # Click send

@app.route('/json_test')
def hello_json():
    data = {'name' : 'Aaron' , 'family' : 'Byun'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = {'server_name' : '0.0.0.0' , 'server_port' : '8080'}
    return jsonify(data)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
