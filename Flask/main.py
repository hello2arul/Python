from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def main(asdf):
    return f'hello {asdf}'


app.run(port=8080, debug=True)
