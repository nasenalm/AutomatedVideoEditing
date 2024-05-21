import speech_recognition as sr

def convert_wav_to_text(wav_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(wav_file_path) as audio_file:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(audio_file)

        # Read the audio file
        audio_data = recognizer.record(audio_file)

        try:
            # Use Google Web Speech API to convert speech to text
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

    return None


