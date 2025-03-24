import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import datetime

# Configure API
genai.configure(api_key="AIzaSyD2wwJeg6vIQUTH1TTqUrtQj9DlQaZrrFk")
model = genai.GenerativeModel("gemini-1.5-pro")

# Initialize Speech Recognition & TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 160)

# Predefined responses
predefined_responses = {
    "what should we know about your life story": 
        "I have a strong background in AI, machine learning, and software development. My journey has been about continuous learning and solving real-world problems using technology.",
    
    "what's your number one superpower": 
        "My number one superpower is problem-solving. I love tackling complex challenges and finding efficient solutions, especially in AI and software engineering.",
    
    "what are the top three areas you’d like to grow in": 
        "I want to grow in three key areas: Artificial Intelligence, Machine Learning, and Python for Large Language Models (LLMs). I aim to enhance my expertise in fine-tuning LLMs, optimizing AI models, and deploying scalable ML solutions.",
    
    "what misconception do your coworkers have about you": 
        "A common misconception is that I always prefer automation over manual work. While I love automation, I also understand the importance of human intuition and creativity in problem-solving.",
    
    "how do you push your boundaries and limits": 
        "I push my boundaries by continuously learning, taking on challenging projects, and staying updated with the latest advancements in AI and technology."
}

# Speak function
def say(text):
    engine.say(text)
    engine.runAndWait()

# Voice command recognition
def take_command():
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        print(" Listening...")
        try:
            audio = recognizer.listen(source, timeout=10)
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language="en-in").lower()
            print(f" User said: {text}")
            return text  
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError as e:
            print(f" Request failed: {e}")
            return ""

# Greet the user
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        say("Good morning, sir.")
    elif 12 <= hour < 18:
        say("Good afternoon, sir.")
    else:
        say("Good evening, sir.")

    say("Hello, I am AI Bot, your voice assistant. How can I help you today?")

# Main program
if __name__ == "__main__":
    print(" AI - Voice Assistant")
    wish_me()  

    while True:
        text = take_command()

        # Exit command handling
        exit_commands = ["exit", "quit", "bye"]
        if any(command in text for command in exit_commands):
            say("Goodbye! Have a great day.")
            break 

        # Check for predefined responses
        for key in predefined_responses:
            if key in text:
                response = predefined_responses[key]
                print(f"  AI Response: {response}")
                say(response)
                break
        else:
            # If no predefined response, use AI-generated response
            try:
                response = model.generate_content(contents=[text])
                answer = response.text.strip()
                short_answer = answer[:150]  # ✅ Limit response length
                print(f"  AI Response: {short_answer}...")
                say(short_answer)
            except Exception as e:
                print(f" Error generating response: {e}")
                say("Sorry, I couldn't process that.")
