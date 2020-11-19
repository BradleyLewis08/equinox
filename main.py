import speech_recognition as sr, pyaudio, keyboard, pyttsx3, time, nltk
from nltk.tokenize import word_tokenize
import subprocess
from spotify_local import SpotifyLocal
import webbrowser
from spotify import *
from schedule import *


r = sr.Recognizer()
mic = sr.Microphone()

def get_path(program):
    paths = {
        "spotify": 'C:\\Users\\bradl\\AppData\\Roaming\\Spotify\\Spotify.exe',

    }
    zoom_links = {
        
    }
def open_program(transcript):
    if 'spotify' in transcript:
        subprocess.call('C:\\Users\\bradl\\AppData\\Roaming\\Spotify\\Spotify.exe')
    else:
        if 'chrome' in transcript:
            webbrowser.open('www.google.com')
        else:
            if 'visual' in transcript or 'studio' in transcript:
                subprocess.call('C:\\Program Files\\Microsoft VS Code\\Code.exe')
            else:
                if 'zoom' or 'xoom' in transcript:
                    if 'for' in transcript:
                        if 'computer' in transcript:
                            webbrowser.open('https://yale.zoom.us/j/92895080985?pwd=d1ZUSklyZmhmbmpubUZidUNKZmRrZz09')
                        else:
                            if 'economics' in transcript:
                                webbrowser.open('https://yale.zoom.us/j/95168673640?pwd=Q2JFWVJwV0dOakxnWHMwd2plZGszQT09')
                            else:
                                if 'seminar' in transcript:
                                    webbrowser.open('https://yale.zoom.us/j/96841696944')
                                else:
                                    if 'maths' in transcript:
                                        webbrowser.open('https://yale.zoom.us/j/96841696944')
                    subprocess.call('C:\\Program Files (x86)\\Zoom\\bin\\Zoom.exe')
                else:
                    if 'notes' in transcript:
                        if 'computer' in transcript:
                            webbrowser.open('https://drive.google.com/drive/u/0/folders/1S1mexq86JRPoP30l0-aEuEIW_RA3A65o')
                        else:
                            if 'economics' in transcript:
                                webbrowser.open('https://drive.google.com/drive/u/0/folders/1m9eLHk5xWHUwAppz5jLnrxnWpCeMnAHI')
                            else:
                                if 'seminar' in transcript:
                                    webbrowser.open('https://drive.google.com/drive/u/0/folders/1K8zSp9BA6n9_rsDvGotwCEQfShfWvd69')

def google_search(speech_search):
    print('Searching...')
    query = 'https://www.google.com/search?q='
    if speech_search[0] == 'google':
        speech_search.pop(0)
    for item in speech_search:
        query += item + ' '
    else:
        webbrowser.open(query)


def record_audio():
    with mic as (source):
        print("Listening")
        r.adjust_for_ambient_noise(source, duration=0.5)
        raw_speech = r.listen(source)
        try:
            transcript = r.recognize_google(raw_speech)
            return transcript
        except sr.UnknownValueError:
            print("I didn't quite catch that. Try again:")
            record_audio()

def get_schedule(transcript):
    if 'today' in transcript:
        get_today_events()
    else:
        if 'tomorrow' in transcript:
            get_tomorrow_events()

def play_song(transcript):
    track_name = ''
    for item in transcript:
        track_name += item + ' '
    else:
        play_track(track_name)

def process_output():
    raw_transcript = word_tokenize(record_audio())
    question_words = ['who', 'what', 'where', 'when', 'how', 'why']
    transcript = [x.lower() for x in raw_transcript]
    print(transcript)
    if transcript[0] == 'play':
        play_song(transcript[1:])
    else:
        if transcript[0] == 'open' or transcript[0] == 'join':
            open_program(transcript[1:])
        else:
            if 'schedule' in transcript:
                get_schedule(transcript)
            else:
                if transcript[0] == 'google' or len([i for i in transcript if i in question_words]) > 0:
                    google_search(transcript)
                else:
                    print("I'm sorry, I don't know how to do that.")
    detect_keyword()

def detect_keyword():
    with mic as (source):
        r.adjust_for_ambient_noise(source, duration=0.5)
        raw_speech = r.listen(source)
        try:
            speech = r.recognize_google(raw_speech)
            tokenised_speech = word_tokenize(speech)
        except sr.UnknownValueError:
            tokenised_speech = []

    if 'Equinox' in tokenised_speech:
        process_output()
    else:
        if 'stop' in tokenised_speech:
            exit()
        else:
            detect_keyword()


detect_keyword()