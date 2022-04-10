from flask import Flask, render_template, request, flash, session, url_for, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiop'
menu = [{'name': 'Главная страница', 'url': '/'},
        {'name': 'О нас', 'url': '/about'},
        {'name': 'Поддержка', 'url': '/support'},]


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Главная страница', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О нашем сайте', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'user {username}'


@app.route('/support', methods=['POST', 'GET'])
def support():

    if request.method == 'POST':
        print(request.form)
        if len(request.form['message']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('support.html', title='Поддержка', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'selfedu@mail.ru' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
