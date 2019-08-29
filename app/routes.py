from app import app

@app.route('/')
@app.route('/index')
def inder():
    return "hello"