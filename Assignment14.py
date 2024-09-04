# text_utils.py
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

# mood_responses.py
def mood_response(mood):
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. Things will get better!",
        "excited": "Awesome! Enjoy your excitement!",
        "angry": "Take a deep breath, it will help.",
    }
    return responses.get(mood.lower(), "I don't know that mood, but I hope you have a good day!")

# main.py
import text_utils as tu
import mood_responses as mr

# Task 1: Mood Response
mood = input("How are you feeling today? ")
print(mr.mood_response(mood))

# Task 2: String Manipulation with Aliases
text = input("Enter a string to manipulate: ")
print("Reversed:", tu.reverse_string(text))
print("Capitalized:", tu.capitalize_string(text))
