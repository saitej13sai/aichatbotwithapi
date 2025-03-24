# aichatbotwithapi

This project is a voice-enabled AI chatbot that listens to user queries, provides predefined responses for specific questions, and leverages the Google Gemini API for AI-generated responses when needed. The chatbot converts speech to text, processes the input, generates a response, and then converts it back to speech for a seamless interaction.

Key Features & Findings:
Speech Recognition: Uses speech_recognition to capture and convert voice input into text.
Predefined Responses: Provides direct answers to specific questions like life story, superpower, and areas of growth.
AI-Powered Responses: Uses Google Gemini API to generate intelligent replies for general queries.
Text-to-Speech Output: Converts responses into speech using pyttsx3 for a natural conversation flow.
Exit Handling: Recognizes commands like "bye," "quit," and "exit" to gracefully terminate the session.

This chatbot ensures a smooth, interactive, and intelligent voice experience, making it adaptable for real-world AI voice applications.

Setup Instructions
Prerequisites
Ensure you have the following installed before running the chatbot:

Python 3.10+

Required dependencies (install via pip)

Installation Steps
Clone the Repository:

git clone https://github.com/saitej13sai/aichatbotwithapi.git
cd aichatbotwithapi


Install Dependencies:


pip install -r requirements.txt

Set Up Google Gemini API Key:



How to Use:

The bot will listen for your voice.

Ask predefined questions (e.g., "What’s your #1 superpower?") or general queries.

The bot will respond with either a predefined answer or an AI-generated one.

Say "bye," "exit," or "quit" to end the conversation.


