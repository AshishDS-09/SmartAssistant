import speech_recognition as sr
import webbrowser
import SmartAssistant.musicLibrary as musicLibrary
import SmartAssistant.Social_media as Social_media
import requests  # type: ignore
import time
import win32com.client  # pyttsx3 is synchronous so  not using in this code 

# Initialize Windows Speech API voice
speaker = win32com.client.Dispatch("SAPI.SpVoice")

newsapi = "1b456fa3a25241de8bbc2a9d789afffa"
r = sr.Recognizer()


def speak(text):
    """Speak out the given text using Windows SAPI voice"""
    print(f"AssistantAI says: {text}")   # Debug print
    speaker.Speak(text)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif c.lower().startswith("open"):
        name_1 = c.lower().split(" ")[1]
        webbrowser.open(Social_media.account[name_1])

    elif c.lower().startswith("play"):
        name_1 = c.lower().split(" ")[1]
        webbrowser.open(musicLibrary.music[name_1])

    elif c.lower().startswith("news"):
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # only speak first 5 to avoid being too long
                speak(article['title'])

    else:
        speak("I'm sorry, I didn't understand that.")


if __name__ == "__main__":
    speak("Initializing AssistantAI....")

    while True:
        print("Waiting for wake word...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print("Heard:", word)

            if "assistant" in word.lower() or "assistantai" in word.lower():
                speak("Hello, I am AssistantAI. How can I help you?")
                time.sleep(1)

                # Listen for command
                with sr.Microphone() as source:
                    print("AssistantAI Active... Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    print("Command:", command)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
