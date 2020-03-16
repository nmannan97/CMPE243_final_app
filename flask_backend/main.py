import flask

app = flask.Flask("__main__")

@app.route('/')
def my_index():
    return flask.render_template('index.html', token = 'hello world')

@app.route('/test', methods = ['GET'])
def test():
    if flask.request.args.get('lat', None):
        return "success"
    else:
        return "Fail"

app.run(debug = True)