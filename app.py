from flask import Flask, render_template, request

from services.chats import HueChat

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')
chat = HueChat()


@app.route('/')
def entry_point():
    return render_template("index.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    human_input = request.form["human_input"]
    llm = "gpt-3.5-turbo-0301"  # "gpt-3.5-turbo"
    message = chat.send_instructions(human_input, llm=llm).get_response(llm=llm)
    chat.apply()
    return message.response


if __name__ == '__main__':
    app.run()
