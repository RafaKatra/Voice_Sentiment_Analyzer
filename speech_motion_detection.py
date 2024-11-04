import speech_recognition as sr
from textblob import TextBlob
from googletrans import Translator
import numpy as np
import time
import librosa
import io

from colorama import init, Fore, Style
print("*******************************************************\n")
def display_instructions():
    # Αρχικοποίηση του colorama
    init()

    # Το μήνυμα που θα εμφανιστεί
    message = """Δοκιμαστικό πρόγραμμα ανάλυσης συναισθήματος.
Τα συμπεράσματα δεν αποτελούν επίσημα αποτελέσματα.
Η ηχογράφηση κρατάει για 30sec, εάν επιθυμείτε να συνεχίσετε ακολουθήστε τις οδηγίες. Developer : Κατραμάδος Ραφαήλ"""

    # Εμφάνιση του μηνύματος με μπλε χρώμα
    print(Fore.BLUE + message + Style.RESET_ALL)
    print("*******************************************************\n")
if __name__ == "__main__":
    display_instructions()

# Developer: Κατραμάδος Ραφαήλ

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Η ηχογράφηση θα ξεκινήσει σε 10 δευτερόλεπτα...")
        time.sleep(10)
        print("Ηχογράφηση θα πραγρατοποιηθεί για 15 δευτερόλεπτα απο τώρα...")
        audio = r.record(source, duration=15)
    return audio

def speech_to_text(audio):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio, language="el-GR")
        return text
    except sr.UnknownValueError:
        print("Δεν μπόρεσα να καταλάβω τι είπατε.")
    except sr.RequestError:
        print("Υπήρξε πρόβλημα με την υπηρεσία αναγνώρισης ομιλίας.")
    return None

def translate_to_english(text):
    translator = Translator()
    try:
        translation = translator.translate(text, src='el', dest='en')
        return translation.text
    except Exception as e:
        print(f"Σφάλμα κατά τη μετάφραση: {e}")
        return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_percentage = (blob.sentiment.polarity + 1) / 2 * 100
    return sentiment_percentage

def interpret_sentiment(percentage):
    if percentage > 60:
        return f"Θετικό συναίσθημα ({percentage:.2f}%)"
    elif percentage < 40:
        return f"Αρνητικό συναίσθημα ({percentage:.2f}%)"
    else:
        return f"Ουδέτερο συναίσθημα ({percentage:.2f}%)"

def analyze_voice_tone(audio):
    wav_data = io.BytesIO(audio.get_wav_data())
    y, sr = librosa.load(wav_data, sr=None)
    
    pitch, _ = librosa.piptrack(y=y, sr=sr)
    energy = np.mean(librosa.feature.rms(y=y))
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    intensity = "Υψηλή" if energy > 0.1 else "Χαμηλή"
    speed = "Γρήγορη" if tempo > 120 else "Αργή"
    pitch_desc = "Υψηλή" if np.mean(pitch) > 150 else "Χαμηλή"
    
    return intensity, speed, pitch_desc

def combined_sentiment_analysis(text_sentiment, voice_intensity, voice_speed, voice_pitch):
    # Δίνουμε βάρη στην ένταση, ταχύτητα και τονικότητα για το τελικό αποτέλεσμα
    score = text_sentiment
    
    if voice_intensity == "Υψηλή":
        score += 10  # Ενισχύει το συναίσθημα αν η ένταση είναι υψηλή
    if voice_speed == "Γρήγορη":
        score += 5  # Ενισχύει ελαφρώς το συναίσθημα αν η ταχύτητα είναι γρήγορη
    if voice_pitch == "Υψηλή":
        score += 5  # Ενισχύει ελαφρώς το συναίσθημα αν η τονικότητα είναι υψηλή
    
    # Οριοθέτηση του score μεταξύ 0 και 100
    score = min(max(score, 0), 100)
    
    return interpret_sentiment(score)

def main():
    while True:
        audio = record_audio()
        if audio:
            greek_text = speech_to_text(audio)
            if greek_text:
                print(f"Κείμενο: {greek_text}")
                english_text = translate_to_english(greek_text)
                if english_text:
                    text_sentiment = analyze_sentiment(english_text)
                    sentiment_result = interpret_sentiment(text_sentiment)
                    print(f"Ανάλυση συναισθήματος κειμένου: {sentiment_result}")
                    
                    voice_intensity, voice_speed, voice_pitch = analyze_voice_tone(audio)
                    print(f"Χαρακτηριστικά φωνής: Ένταση: {voice_intensity}, Ταχύτητα: {voice_speed}, Τονικότητα: {voice_pitch}")
                    
                    # Συνδυασμένη ανάλυση
                    final_sentiment = combined_sentiment_analysis(text_sentiment, voice_intensity, voice_speed, voice_pitch)
                    print(f"Συνδυασμένο συμπέρασμα συναισθήματος: {final_sentiment}")
                else:
                    print("Δεν ήταν δυνατή η ανάλυση συναισθήματος λόγω σφάλματος μετάφρασης.")
            
        choice = input("Πατήστε Enter για να συνεχίσετε ή 'q' για έξοδο: ")
        if choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()
