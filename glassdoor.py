from flask import Flask, render_template

app = Flask(GlassDoor Jobs)

@app.route('/')
def home():
    message = "Hello, Flask World!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
