# 🤖🎙️ AI Voice Assistant with Flask UI

This is my **Mega Python Project** where I built an **AI Voice Assistant** that can listen 🎤, speak 🔊, and also has a **Flask-based web interface 🌐**.  
The assistant can open websites 🌍, play music 🎶, fetch live news 📰, and respond to commands with speech output 💬.  

I created this project to practice **Python 🐍, Flask 🌐, APIs 🔑, and Voice Technologies 🎤** together in one complete application. 🚀

---

## ✨ Features

- 🎤 **Voice Input** → Listens to microphone input using SpeechRecognition  
- 🔊 **Voice Output** → Responds using Windows SAPI text-to-speech  
- 🌍 **Web Browsing** → Opens Google, YouTube, Instagram, LinkedIn, etc.  
- 🎶 **Music Player** → Plays songs from a custom music library  
- 📰 **Live News** → Fetches top headlines from **NewsAPI**  
- 💻 **Flask UI** → Simple web interface to control the assistant  

Basically, this is a mini **Jarvis (Iron Man AI) 🦾** built with Python 😃  

---

## 📂 Project Structure

SmartAssistant/  
│── Demo.py             # 🎙️ Main entry point for running AssistantAI without using UI interface
│── main.py             # 🚀 Flask app to run the web interface  
│── assistant.py        # 🧠 Core class for voice assistant logic  
│── musicLibrary.py     # 🎶 Dictionary for songs to be played  
│── Social_media.py     # 📱 Social media links (YouTube, Instagram, etc.)  
│  
│── templates/  
│   └── index.html      # 🖥️ Flask HTML page  
│  
│── static/             # 🎨 Static files (CSS, JS, images if needed)  
│  
│── requirements.txt    # 📦 List of Python libraries  
│── .env                # 🔑 Stores API keys (not pushed to GitHub)  
│── README.md           # 📝 Project documentation  

---

## 🗣️ Example Commands

Here are some sample voice commands you can try with **AssistantAI**:

- 🖐️ **"assistant"** → Wakes up the assistant  
- 🌍 **"Open Google"** → Opens Google in browser  
- 📺 **"Open YouTube"** → Opens YouTube site  
- 📸 **"Open Instagram"** → Opens Instagram  
- 🎶 **"Play song_name"** → Plays songs from `musicLibrary.py`  
- 📰 **"News"** → Reads latest 5 headlines aloud  

---

## 🔑 API Keys

This project uses **NewsAPI** to fetch live news 📰.  

### Steps:
1. 📝 Create an account on [NewsAPI](https://newsapi.org/) and generate a free API key.  
2. 🔐 Add the key inside `.env` file:  

``` env
NEWS_API_KEY=your_api_key_here
```

---

## 🛠️ Technologies Used

- 🐍 **Python 3.10+**  
- 🌐 **Flask** → for the web UI  
- 🎤 **SpeechRecognition** → for voice-to-text  
- 🔊 **PyWin32 (SAPI)** → for text-to-speech  
- 📰 **NewsAPI** → for fetching news  
- 🎨 **HTML/CSS** → for UI  

---
## 📚 What I Learned  

From this project, I learned how to:  

- ✅ Use speech recognition 🎤 and text-to-speech 🔊 in Python  
- ✅ Work with external APIs 🔑 (NewsAPI)  
- ✅ Build a Flask app 🌐 with templates  
- ✅ Organize a project into multiple files/modules 📂  
- ✅ Use .env files to secure API keys 🔒  

## 📜 License  

This project is for educational purposes only 🎓.  
You are free to use, modify, and improve it. ✨  

---

## 👨‍💻 Author  

Made with ❤️ by **Ashish Deep Sen**  




