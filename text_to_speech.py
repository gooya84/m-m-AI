import whisper
from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")  # This will play the audio on Windows
    # For macOS, use os.system("afplay output.mp3")
    # For Linux, use os.system("mpg321 output.mp3")

def main():
    text = "Hello, world! This is a test of the text-to-speech system."
    text_to_speech(text)

if __name__ == "__main__":
    main()
