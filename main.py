from flask import Flask, render_template, request, flash

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


if __name__ == '__main__':
    app.run(debug=True)
