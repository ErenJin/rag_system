from rag_system import app
from flask import Flask, render_template, redirect, url_for, request, jsonify
from forms import LoginForm
from rag.function import process_user_message

@app.route('/',methods=['GET', 'POST'])
    # 登录页面
def index():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('main'))
    return render_template('index.html', form=login_form)


@app.route('/main', methods=['GET', 'POST'])

    # 主功能页面
def main():
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid JSON'}), 400

        user_message = data.get('message')
        if user_message is None:
            return jsonify({'error': 'Missing message key'}), 400

        # Here you can process the message and generate a response.
        # For simplicity, we'll just echo the user's message back.

        bot_response = process_user_message(user_message)


        return jsonify({'response': bot_response})

    return render_template('main.html')


app.run(debug=True)

