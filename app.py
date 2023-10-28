from flask import Flask, render_template

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')


@app.route('/')
def entry_point():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
