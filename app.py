from flask import Flask, render_template

app = Flask(__name__, template_folder="Level1", static_folder="static")

@app.route('/')
def level1():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
