import speech_recognition as sr
from googletrans import Translator
import pyttsx3 
 
r = sr.Recognizer() 
engine = pyttsx3.init()
translator = Translator()

flag = 1

lang_dict = {
    "Afrikaans" : "af",
    "Albanian" : "sq",
    "Amharic"  : "am",
    "Arabic" : "ar",
    "Armenian" : "hy",
    "Azerbaijani" : "az",
    "Basque" : "eu",
    "Bengali" : "bn",
    "Bosnian" : "bs",
    "Bulgarian" : "bg",
    "Burmese" : "my",
    "Catalan" : "ca",
    "Chinese" : "zh",
    "Croatian" : "hr",
    "Czech" : "cs",
    "Danish" : "da",
    "Dutch" : "nl",
    "English" : "en",
    "Estonian" : "et",
    "Flipino" : "fil",
    "Finnish" : "fi",
    "French" : "fr",
    "Galician" : "gl",
    "Georgian" : "ka",
    "German" : "de",
    "Gujarathi" : "gu",
    "Hebrew" : "iw",
    "Hindi" : "hi",
    "Hungarian" : "hu",
    "Icelandic" : "is",
    "Indonesian" : "id",
    "Italian" : "it",
    "Japanese" : "ja",
    "Javanese" : "jv",
    "Kanada" : "kn",
    "Kazakh" : "kk",
    "Khmer" : "km",
    "Korean" : "ko",
    "Lao" : "lo",
    "Latvian" : "lv",
    "Lithunaian" : "lt",
    "Macedonian" : "mk",
    "Malay" : "ms",
    "Malayalam" : "ml",
    "Marathi" : "mr",
    "Mangolian" : "mn",
    "Nepali" : "ne",
    "Norwegian" : "no",
    "Persian" : "fa",
    "Polish" : "pl",
    "Portuguese" : "pt",
    "Punjabi" : "pa",
    "Romanian" : "ro",
    "Russian" : "ru",
    "Serbian" : "sr",
    "Sinhala" : "si",
    "Slovak" : "sk",
    "Slovenian" : "sl",
    "Spanish" : "es",
    "Sundanese" : "su",
    "Swahili" : "sw",
    "Swedish" : "sv",
    "Tamil" : "ta",
    "Telugu" : "te",
    "Thai" : "th",
    "Turkish" : "tr",
    "Ukranian" : "uk",
    "Urdu" : "ur",
    "Uzbek" : "uz",
    "Vietnamese" : "vi",
    "Zulu" : "zu"
}
d_lang = input("Select Default Language: ")
c_lang = input("Input Language: ")
def SpeakText(command):
    engine.say(command) 
    engine.runAndWait()

def TransText(text,lang):
    op = translator.translate(text, dest = lang)
    print(op.text)
    return str(op.text)

def recognise():
     try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening.......")
            audio = r.listen(source)
            result = r.recognize_google(audio , language = lang_dict[c_lang])
            print("Translating.......")
            return result
     except sr.UnknownValueError:
        print("unknown error occured")
    
def main():

    while(flag):
        recognised_text = recognise()
        trans_text = TransText(recognised_text,lang_dict[d_lang])
        SpeakText(trans_text)

if __name__ == "__main__":
    main()
