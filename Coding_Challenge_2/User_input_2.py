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
def calculate_score(word):
    score = 0
    for letter in word:
        for key in letter_scores:
            score += letter_scores[key]
            print(score)
            break
    return score
scrabble_word = input('Type your scrabble word to calculate its score:').lower()
score = calculate_score(scrabble_word)
print('The scrabble score of ' + str(scrabble_word) + ' is ' + str(score))