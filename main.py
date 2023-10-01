import os

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.0")
    while True:
        s = input("Say something : ")

        if s == "q":
            break
        command = (
            f"PowerShell -Command "
            f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
        )
        os.system(command)
