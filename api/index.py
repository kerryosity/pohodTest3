from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, Vercel! Flask работает! 🚀"

if __name__ == "__main__":
    app.run()
