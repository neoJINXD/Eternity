import speech_recognition as speech
import pyttsx3
import time

PROMPT_PHRASE = "calculate"  # should be lowercase
EXIT_PHRASE = "quit application"  # should be lowercase
ENGINE = pyttsx3.init()


def print_and_speak(str):
    print(str)
    ENGINE.say(str)
    ENGINE.runAndWait()


def calibrate_listener():
    recognizer = speech.Recognizer()
    microphone = speech.Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print_and_speak(
            "Speech mode is on. Wait a few seconds for calibration. Say quit application to stop listening")
    return recognizer, microphone


def respond(recognizer, audio):
    try:
        raw_query = str(recognizer.recognize_google(audio)).lower()
        if PROMPT_PHRASE in raw_query:
            trimmed_query = raw_query.partition(PROMPT_PHRASE)[2]
            print_and_speak("You said: " + trimmed_query + " which is " + str(numeric(trimmed_query)))
            return True

        elif EXIT_PHRASE in raw_query:
            print_and_speak("Thank you. Now exiting application")
            time.sleep(2)
            return False
        else:
            return True
    except LookupError:
        print_and_speak("Could not understand audio. Please repeat")  # Consider if want to use custom error class
        return True
    except speech.UnknownValueError:
        print_and_speak("Could not understand audio. Please repeat")  # Consider if want to use custom error class
        return True


def numeric(equation):
    x = 0
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0].strip()) + int(y[1].strip())
    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0]) - int(y[1])
    elif '*' in equation:
        y = equation.split('*')
        x = int(y[0]) * int(y[1])
    return x


calibration = calibrate_listener()
listener = calibration[0]
microphone = calibration[1]
keep_listening = True

with microphone as source:
    while keep_listening:
        print("Listening")
        audio = listener.listen(source)
        keep_listening = respond(listener, audio)
