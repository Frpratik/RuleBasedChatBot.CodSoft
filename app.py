from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm a chatbot, I'm always functioning as expected!"
    elif "name" in user_input:
        return "I'm a Python-powered chatbot. What's your name?"
    elif "weather" in user_input:
        return "I can't check the weather, but you can try a weather website!"
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "day" in user_input:
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a wonderful day!"
    elif "help" in user_input:
        return "I can assist you with general inquiries and provide information!"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "favorite color" in user_input:
        return "As a chatbot, I don't have preferences, but I think blue is nice!"
    elif "created" in user_input:
        return "I was created by a Python programmer to assist you!"
    elif "fun facts" in user_input:
        return "Did you know honey never spoils? Archaeologists found pots of it in ancient tombs!"
    elif "recommend a book" in user_input:
        return "I recommend 'To Kill a Mockingbird'—it's a classic!"
    elif "productivity" in user_input:
        return "Try using the Pomodoro technique: work for 25 minutes, then take a 5-minute break."
    elif "recipe" in user_input:
        return "How about trying a simple pasta recipe? It's quick and delicious!"
    elif "motivational quote" in user_input:
        return "Believe you can and you're halfway there. -Theodore Roosevelt"
    elif "latest news" in user_input:
        return "I can't browse the internet, but you can check a news website for the latest updates!"
    elif "get started" in user_input:
        return "To get started, just ask me anything or let me know how I can help you!"
    elif "learn a new language" in user_input:
        return "I recommend using language apps like Duolingo or Babbel for effective learning."
    elif "travel destinations" in user_input:
        return "Some popular destinations are Paris, Bali, and Tokyo. Where would you like to go?"
    elif "opinion on AI" in user_input:
        return "AI is a powerful tool that can help in many fields, but it should be used responsibly."
    elif "workout routine" in user_input:
        return "How about a simple routine: 20 push-ups, 30 squats, and a 10-minute jog?"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"


# Route to serve the chatbot page
@app.route("/")
def home():
    return render_template("index.html")

# API route to handle chatbot input and return response
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
