import speech_recognition as sr
import time

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
word = ""
while word != 'dayan':
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            word = r.recognize_google(audio_text, language="az-AZ")
            print("Text: " + word)
        except:
            print("Sorry, I did not get that")

        audio_text = None
        time.sleep(1)