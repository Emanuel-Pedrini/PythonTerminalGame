import speech_recognition as sr
import time

vInt_RecordingTimeSeconds : int = 20
vPath_DefaultOutputFile = 'fl_Output.txt'

vRecognizer_MainSpeakRecognizer = sr.Recognizer()

def main():
    print("Hello, starting now...")
    with sr.Microphone() as mic:
        vRecognizer_MainSpeakRecognizer.adjust_for_ambient_noise(mic, duration=1)
        start_time = time.time()
        print("Adjusting ambient sound...")
        act = time.time() - start_time
        while (act) < vInt_RecordingTimeSeconds:
            act = time.time() - start_time
            rmn = vInt_RecordingTimeSeconds - act
            print(f"Remaining : {rmn}", end='\r')
            try:
                audio = vRecognizer_MainSpeakRecognizer.listen(mic, timeout=5, phrase_time_limit=10)
                text = recognize_speech(audio)
                save(text)
            except sr.WaitTimeoutError:
                print("Error don't listened anything.")
            except Exception as e:
                print(f"Error : {e}")
                time.sleep(0.5)
    print("Finished")
                
def recognize_speech(audio):
    try:
        text = vRecognizer_MainSpeakRecognizer.recognize_google(audio)
        time_stamp = time.strftime("[%H:%M:%S]", time.localtime())
        print(f"Recog : {text}")
        return time_stamp + text
    except sr.UnknownValueError:
        print("Fuck")
    except sr.RequestError as re:
        print(f"Speech Recognition failed : {re}")
    return None

def save(b):
    if b:
        with open(vPath_DefaultOutputFile, "a", encoding="utf-8") as file:
            file.write(b + '\n')

if __name__ == "__main__":
    main()