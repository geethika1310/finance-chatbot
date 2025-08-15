#voice input or output
import whisper
from gtts import gTTS
from pydub import AudioSegment
import os

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    audio_path = f"temp_audio.{audio_file.name.split('.')[-1]}"
    with open(audio_path, "wb") as f:
        f.write(audio_file.read())
    result = model.transcribe(audio_path)
    os.remove(audio_path)
    return result["text"]

def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    audio = AudioSegment.from_mp3("response.mp3")
    audio.export("response.wav", format="wav")
    os.system("start response.wav")  # Use 'afplay' on Mac or 'xdg-open' on Linux
