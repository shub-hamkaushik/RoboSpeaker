import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created By Shubham")
    engine = pyttsx3.init()
    while True:
        x = input("enter what you want to me speak: ")
        if x == "q":
            engine.say("Bye bye Friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
