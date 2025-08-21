from flask import Flask, render_template, request, jsonify
import SmartAssistant.assistant as assistant

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    user_input = data.get("command", "")
    if user_input.strip() == "":
        return jsonify({"response": "Please say something"})
    
    response = assistant.process_command(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    assistant.speak("Initializing AssistantAI Web...")
    app.run(debug=True)
