from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/api/greet')
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}! Welcome to Orincore!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)