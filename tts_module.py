import pyttsx3
import builtins

# Initialize the TTS engine as a static object
engine = pyttsx3.init()

def speak(text, rate=300):
    """
    Convert text to speech.
    
    Parameters:
    text (str): The text to be spoken.
    rate (int): The speaking rate (words per minute).
    """
    # Set the speaking rate
    engine.setProperty('rate', rate)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

def override_print(rate=300):
    """
    Override the built-in print function to use the speak function.
    
    Parameters:
    rate (int): The speaking rate (words per minute).
    """
    original_print = builtins.print

    def new_print(*args, **kwargs):
        text = ' '.join(map(str, args))
        original_print(*args, **kwargs)
        speak(text, rate=rate)

    builtins.print = new_print

# Automatically override print when the module is imported
override_print(rate=300)