'''
Implements a spam filter as described in this blog post:
http://www.paulgraham.com/spam.html
Uses a statistical, Bayesian approach.

Created by: Tyler Poel, for homework02 in CS 344 at Calvin University
Date: March10, 2020
'''


def build_hash(corpus):
    """This function build a hashtable of occurrences for each word in a corpus"""
    table = {}
    for email in corpus:
        for token in email:
            if token not in table:
                count = 0
                for spam in corpus:
                    for word in spam:
                        if token == word:
                            count += 1
                # lowercase for consistency across the two hash tables
                table.update({token.lower(): count})
    return table


def spam_probability(token, good, bad, ngood, nbad):
    """Calculates the probability a given word is from a spam email or not"""
    g = 2 * (good.get(token) or 0)
    b = (bad.get(token) or 0)
    if g + b >= 1:
        return max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
    else:
        return 0


if __name__ == '__main__':
    spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
    ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

    # number of emails in each corpus
    nbad = len(spam_corpus)
    ngood = len(ham_corpus)

    spam = build_hash(spam_corpus)
    ham = build_hash(ham_corpus)

    print(spam)
    print(ham)

    probabilities = {}
    for word in ham:
        probabilities.update({word: spam_probability(word, ham, spam, ngood, nbad)})
    for word in spam:
        if word not in probabilities:
            probabilities.update({word: spam_probability(word, ham, spam, ngood, nbad)})

    print(probabilities)
