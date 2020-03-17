import flask

app = flask.Flask("__main__")

@app.route('/')

def my_index():
    return flask.render_template('index.html', token = 'hello world')

@app.route('/input_data', methods = ['POST','GET'])
def input_data():
    if flask.request.method == 'POST':
        return '<h1> Submitted form</h1>'

    return '''<firn nethod = "POST">
    Input <input type = "test" name = "input">
    '''

app.run(debug = True)