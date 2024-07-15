import speech_recognition as sr
import pyttsx3
import datetime
import requests
from bs4 import BeautifulSoup

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a voice command and return the recognized text"""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None

def handle_command(command):
    """Handle the recognized command"""
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_web(search_query)

def search_web(query):
    """Perform a web search and provide the first result"""
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('div', class_='BNeawe').text
    speak(f"Here is what I found for {query}: {result}")

if __name__ == "__main__":
    speak("Voice assistant initialized")
    while True:
        command = listen()
        if command:
            handle_command(command)
