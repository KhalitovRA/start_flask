from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['О нас', 'support', 'contacts']


@app.route('/index')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная страница', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О нашем сайте')


@app.route('/profile/<username>')
def profile(username):
    return f'user {username}'


if __name__ == '__main__':
    app.run(debug=True)
