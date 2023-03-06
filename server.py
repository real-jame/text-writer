from flask import Flask, current_app, request, render_template

app = Flask(__name__, template_folder="./")

def serve_page():
    text_file = open("text.txt", "r")
    rendered_template = render_template("index.html", text=text_file.read())
    text_file.close()
    return rendered_template

@app.get("/")
def serve():
    return serve_page()

@app.post("/")
def write():
    input_text = request.form["input"]
    if input_text != "":
        text_file = open("text.txt", "a")
        text_file.write(input_text + "\n")
        text_file.close()
    return serve_page()