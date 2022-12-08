from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="web/static", template_folder="web/templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookbus')
def bookbus():
    return render_template('bookbus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app