import ast
from nltk.corpus import stopwords
from string import punctuation
from math import log, exp


def predict(posiwords, negawords, allwords, review):
    file = open(posiwords, "r")
    contents = file.read()
    posi_words = ast.literal_eval(contents)
    file.close()

    file = open(negawords, "r")
    contents = file.read()
    nega_words = ast.literal_eval(contents)
    file.close()

    file = open(allwords, "r")
    contents = file.read()
    all_words = ast.literal_eval(contents)
    file.close()

    stop_words = stopwords.words("english")
    pn = 17500
    nn = 17500

    p = 0
    n = 0
    pred = 0
    for i in review.split():
        i = i.lower()
        if ((i in punctuation) or (i in stop_words)):
            continue
        if (i in posi_words):
            p = p + log(posi_words[i] / pn)
        else:
            p = p + log(100) - log(pn + (100 * len(all_words)))
        if (i in nega_words):
            n = n + log(nega_words[i] / nn)
        else:
            n = n + log(100) - log(nn + (100 * len(all_words)))
        p = p + log(pn / (pn + nn))
        n = n + log(nn / (pn + nn))
        if (p >= n):
            pred = 1
        else:
            pred = -1
        p = exp(p)
        n = exp(n)
        rating = 5 + ((p - n) / p) * 10
        if rating < 0:
            rating = 0
        if rating > 10:
            rating = 10
    return pred, p, n, rating


pred, p, n, rating = predict("posiwords.txt", "negawords.txt", "allwords.txt",
                             "Fresh. Relevant. Heartfelt. I thoroughly enjoyed this film. It was so nice to see LGBTQ characters at the center of this story, rather than side characters or fillers. For those who have already come out, and for those who struggle to find a way, we see you. This will be on my holiday must watch list for years to come.")
print(pred, rating)
