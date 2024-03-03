# 5. User input 2
# Using the following dictionary (or a similar one you found on the internet),
# ask the user for a word, and compute the Scrabble word score for that word
# (Scrabble is a word game, where players make words from letters, each letter is worth a point value),
# steal this code from the internet, format it and make it work:
#
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }

# scrabble letter dictionary and input scrabble word
letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}


# Calculate the scrabble score of the word input

def calculate_score(word):
    score = 0
    for letter in word:
        for char in letter_scores:
            if letter in char:
                score += letter_scores[char]
                break
    return score


# Ask user to input scrabble word
scrabble_word = input("Enter your scrabble word here to calculate score:")

# calculate score of input
score = calculate_score(scrabble_word)
print("Your word has a scrabble score of", score)