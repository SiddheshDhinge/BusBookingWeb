from flask import Flask

app = Flask(__name__)

@app.route('/')
def h():
    return '<h1>Hello world</h1>'

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app