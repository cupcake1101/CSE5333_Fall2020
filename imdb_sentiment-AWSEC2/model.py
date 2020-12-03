import ast
from nltk.corpus import stopwords
from string import punctuation
from math import log

def predict(posiwords,negawords,allwords,review):
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
        if((i in punctuation) or (i in stop_words)):
            continue
        if (i in posi_words):
            p = p + log(posi_words[i]/pn)
        else:
            p = p + log(100) - log(pn+(100*len(all_words)))
        if (i in nega_words):
            n = n + log(nega_words[i]/nn)
        else:
            n = n + log(100) - log(nn+(100*len(all_words)))
        p = p + log(pn/(pn + nn))
        n = n + log(nn/(pn + nn))    
    if(p>=n):
        pred = 1
    else:
        pred = -1
    return pred,p,n


pred,p,n = predict("posiwords.txt","negawords.txt","allwords.txt","The Night Listener is probably not one of William's best roles, but he makes a very interesting character in a somewhat odd but very different movie. I can guarantee you that you have never seen this kind of movie before. Some people maybe won't like the slow pacing of this movie, but I think it's the great plus of the movie. It is definitely one of the top movies that have come out the year 2006. It has a intriguing performance in a movie with a great content, dramatic feeling. This is no americanized movie. Neither is it a predictable movie. You just feel that it is a movie that has secrets which you have a hard time to determine what the outcome of it may be. This is no excellent movie that has everything, but hell, it's a damn good and very original movie.")

print(pred)