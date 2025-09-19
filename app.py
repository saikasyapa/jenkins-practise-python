from flask import Flask

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! Flask is running 🚀"

if __name__ == "__main__":
    # Run the app on localhost:5000
    app.run(host="0.0.0.0", port=5000)
