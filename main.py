# Write Morse Code
# Write all the alphabets Number with there Morse Code in a dictionary
# Advance use Google translator api to translate any language in english and give there Morse Code
# how the Project work
# ask user to Write something
# split user text in words and convert them with the dictionary and give Morse Code


morseCode = {"a": "▄ ▄▄▄", "b": "▄▄▄ ▄ ▄ ▄", "c": "▄▄▄ ▄ ▄▄▄ ▄", "d": "▄▄▄ ▄ ▄", "e": "▄", "f": "▄ ▄ ▄▄▄ ▄",
             "g": "▄▄▄ ▄▄▄ ▄", "h": "▄ ▄ ▄ ▄", "i": "▄ ▄", "j": "▄ ▄▄▄ ▄▄▄ ▄▄▄",
             "k": "▄▄▄ ▄ ▄▄▄", "l": "▄ ▄▄▄ ▄ ▄", "m": "▄▄▄ ▄▄▄", "n": "▄▄▄ ▄", "o": "▄▄▄ ▄▄▄ ▄▄▄", "p": "▄ ▄▄▄ ▄▄▄ ▄",
             "q": "▄▄▄ ▄▄▄ ▄ ▄▄▄", "r": "▄ ▄▄▄ ▄", "s": "▄ ▄ ▄", "t": "▄▄▄", "u": "▄ ▄ ▄▄▄", "v": "▄ ▄ ▄ ▄▄▄",
             "w": "▄ ▄▄▄ ▄▄▄", "x": "▄▄▄ ▄ ▄ ▄▄▄", "y": "▄▄▄ ▄ ▄▄▄ ▄▄▄", "z": "▄▄▄ ▄▄▄ ▄ ▄", "1": "▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
             "2": "▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄", "3": "▄ ▄ ▄ ▄▄▄ ▄▄▄",
             "4": "▄ ▄ ▄ ▄ ▄▄▄", "5": "▄ ▄ ▄ ▄ ▄", "6": "▄▄▄ ▄ ▄ ▄ ▄", "7": "▄▄▄ ▄▄▄ ▄ ▄ ▄", "8": "▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄",
             "9": "▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄", "0": "▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄", }

textInput = input("What is Your Name: ")
