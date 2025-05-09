from rag_system import app
from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

@app.route('/',methods=['GET', 'POST'])
    # 登录页面
def index():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('main'))
    return render_template('index.html', form=login_form)


@app.route('/main')
    # 主功能页面
def main():
    return render_template('main.html')


app.run(debug=True)
