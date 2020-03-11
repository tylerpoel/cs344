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


def build_probability_table(good, bad, ngood, nbad):
    """Builds the probability table for each token from the bad and good corpuses"""
    probs_table = {}
    for word in good:
        probs_table.update({word: spam_probability(word, good, bad, ngood, nbad)})
    for word in bad:
        if word not in probs_table:
            probs_table.update({word: spam_probability(word, good, bad, ngood, nbad)})
    return probs_table


def new_mail_probability(mail, probs_table):
    """Given an email and the probabilities of each token, calculates the probability the individual email is spam."""
    prod = 1
    complements = 1
    # finds product of all the elements, and complements of the elements
    for token in mail:
        prob = probs_table.get(token.lower())
        prod *= prob
        complements *= (1 - prob)

    return prod / (prod + complements)


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

    probabilities = build_probability_table(ham, spam, ngood, nbad)

    print(probabilities)

    spam_prob = new_mail_probability(spam_corpus[0], probabilities)
    print("spam_corpus[0]: " + str(spam_prob))
    spam_prob = new_mail_probability(spam_corpus[1], probabilities)
    print("spam_corpus[1]: " + str(spam_prob))
    spam_prob = new_mail_probability(ham_corpus[0], probabilities)
    print("ham_corpus[0]: " + str(spam_prob))
    spam_prob = new_mail_probability(ham_corpus[1], probabilities)
    print("ham_corpus[1]: " + str(spam_prob))