from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Hello, {name}! Welcome to the Flask app."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
