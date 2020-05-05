#translation function
#changes the letter AEIOUaeiou in a phrase in to the word Worm

def translate(phrase):
    to_translate = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                to_translate = to_translate + "smallworm"
            else:
                to_translate = to_translate + "BIGWORM"

        else:
            to_translate = to_translate + letter
    return to_translate

#print(translate(input("Enter whatever the fuck you want: ")))




