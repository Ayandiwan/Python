from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def login_form():
    return '''
    <html>
    <body>
    <h2>Login Form</h2>
    <form action="/login" method="post">
        <table>
            <tr>
                <td>Enter UserName:</td>
                <td><input type="text" name="txtname"></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><input type="password" name="txtpass"></td>
            </tr>
            <tr>
                <td colspan="2" align="center">
                    <input type="submit" value="Login">
                </td>
            </tr>
        </table>
    </form>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    # Get form values from the request
    username = request.form.get('txtname')
    password = request.form.get('txtpass')

    if username == "ad" and password == "123":
        return "<h3>✅ Login successful!</h3>"
    else:
        return "<h3>❌ Invalid username or password!</h3>"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
