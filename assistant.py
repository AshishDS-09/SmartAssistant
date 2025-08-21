import speech_recognition as sr
import webbrowser
import requests
import win32com.client
import SmartAssistant.musicLibrary as musicLibrary
import SmartAssistant.Social_media as Social_media

# Initialize Windows Speech API voice
speaker = win32com.client.Dispatch("SAPI.SpVoice")
recognizer = sr.Recognizer()
newsapi = "1b456fa3a25241de8bbc2a9d789afffa"

def speak(text):
    """Speak out the given text using Windows SAPI voice"""
    print(f"AssistantAI says: {text}")
    speaker.Speak(text)
    return text

def listen():
    """Listen from microphone and return text"""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)
    return recognizer.recognize_google(audio)

def process_command(c):
    """Process user command"""
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        return speak("Opening Google...")

    elif c.lower().startswith("open"):
        name_1 = c.lower().split(" ")[1]
        if name_1 in Social_media.account:
            webbrowser.open(Social_media.account[name_1])
            return speak(f"Opening {name_1}...")
        else:
            return speak("Account not found.")

    elif c.lower().startswith("play"):
        name_1 = c.lower().split(" ")[1]
        if name_1 in musicLibrary.music:
            webbrowser.open(musicLibrary.music[name_1])
            return speak(f"Playing {name_1}...")
        else:
            return speak("Song not found.")

    elif c.lower().startswith("news"):
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            headlines = [article['title'] for article in articles[:5]]
            for h in headlines:
                speak(h)
            return " | ".join(headlines)

    else:
        return speak("I'm sorry, I didn't understand that.")
