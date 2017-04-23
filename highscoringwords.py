from collections import Counter
__author__ = 'codesse'


# Python 2.7.13

class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.leaderboard = []  # initialise an empty leaderboard
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)


    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return:
        """
        calculated_scores = []
        for word in self.valid_words:
            if len(word) >= self.MIN_WORD_LENGTH:
                calculated_scores.append((self.score_word(word), word))

        self.build_leaderboad(calculated_scores)



    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return:
        """
        calculated_scores = []
        start_counter = Counter(starting_letters)

        for word in self.valid_words:

            if (len(word) >= self.MIN_WORD_LENGTH and
                    len(word) <= len(starting_letters) and
                    not Counter(word) - start_counter):
                calculated_scores.append((self.score_word(word), word))

        self.build_leaderboad(calculated_scores)


    def build_leaderboad(self, calculated_scores):
        """
        Build leaderboard from dict containing words and their scores.
        :return:
        """
        max_size = min(self.MAX_LEADERBOARD_LENGTH, len(calculated_scores))
        leaderboard_scored = sorted(calculated_scores, key=lambda x: (-x[0], x[1]))
        self.leaderboard = [i[1] for i in leaderboard_scored[0:max_size]]



    def score_word(self, word):
        """
        Score a word corresponding to frequency of letters in it.
        :return: word score
        """
        res = 0
        for char in word:
            res += self.letter_values[char]
        return res




def main():
    test_highscore = HighScoringWords()

    test_highscore.build_leaderboard_for_word_list()
    count = 0
    for word in test_highscore.leaderboard:
        print word + " \t " + str(test_highscore.score_word(word))
        count += 1
    print "\nTotal count " + str(count)
    print "\n************************************\n"

    test_highscore.build_leaderboard_for_letters("test")
    for word in test_highscore.leaderboard:
        print word + "  " + str(test_highscore.score_word(word))


if __name__ == "__main__":
    main()
