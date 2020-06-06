import re
import plotly
from plotly.graph_objs import *
import plotly.graph_objects as go

#Q5,6----------------Remove stopwords ---------------#
def search(pat, txt, q):
    listNum = []
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    d=256
    txt= str(txt)
    # The value of h would be "pow(d, M-1)% q"
    for i in range (M - 1):
        h = (h * d) % q
        # Calculate the hash value of pattern and first window of text

        # ord unicode for char

    for i in range(M):
            p = (d * p + ord(pat[i])) % q #sum of the pattern unicode
            t = (d * t + ord(txt[i])) % q #sum of the text unicode

    #print("Current t=",t,"Current p=",p,"Current h=",h)
        # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and pattern if the hash values match then only check for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break

            j += 1

            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                listNum.append(i)

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < N - M:
            #(if x -ve) value mod q use formula qc+r = x
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            #print("Next window t = ",t,"h=",h)
            # We might get negative values of t, converting it to positive
            if t < 0:
                print("t<0",t)
                t = t + q
    return listNum

def stripNonAlphaNum(text):

    text = re.compile(r'\W+', re.UNICODE).split(text)
    saveNum = ''.join(i for i in text if i.isdigit())
    store = []
    for w in text:
        if w not in saveNum:
            store.append(w)

    return store

def removeStopWords(stopwordsInText,strippedText):
    stopfreq = []
    storefreq = []
    for i in strippedText:
        if i not in stopwordsInText:
            storefreq.append(i)
        else:
            stopfreq.append(i)
    print("Text after removing words:",storefreq)
    return storefreq,stopfreq

def calculateWordFrequency(text):
    wordfreq = []
    for w in text:
        wordfreq.append(text.count(w))

    freq = dict(zip(text,wordfreq))

    return freq

def sortWordFreq(wordfreq):
    temp = [(wordfreq[key], key) for key in wordfreq]
    temp = []

    for key in wordfreq:
        temp.append([(wordfreq[key],key)])
    temp.sort()
    print("Sorted dictionary :", temp)
    return temp

def removeStopWriteText(input,t):

    f = open(input, 'a', encoding='utf-8')
    for i in t:
        f.write(i+" ")
    f.close()

def drawLine(freq,place):
    plotly.offline.plot({
        "data": [Scatter(x=list(freq.keys()), y=list(freq.values()))],
        "layout": Layout(title="Word Count "+place)

    })

def stopwords(readFiles):
    f = open("stopwords.txt",'r',encoding = 'utf-8')
    stopWords = f.read().split()
    stopwordsInText = []

    for s in stopWords:
        index = search(s, readFiles, 101)

        if index != []:
            stopwordsInText.append(readFiles[index[0]:index[0] + len(s)])

    print("Stopwords found in text: ", stopwordsInText)
    return stopwordsInText

def main():
    textfiles = ["Tjakarta.txt","Tbangkok.txt","Ttaipei.txt","Thk.txt","Ttokyo.txt","Tbeijing.txt","Tseoul.txt"]
    places = ["!Jakarta.txt","!Bangkok.txt","!Taipei.txt","!Hong_Kong.txt","!Tokyo.txt","!Beijing.txt","!Seoul.txt"]
    for input in textfiles:
        readFile = open(input, 'r', encoding='utf-8')
        readFiles = readFile.read().lower()
        print("<==", input, "==>")
        readFile.close()

        stopWordInText = stopwords(readFiles)
        removeNonAlpha = stripNonAlphaNum(readFiles)
        txtNoStopWords,stopfreq = removeStopWords(stopWordInText,removeNonAlpha)
        i = 0;
        #removeStopWriteText(places[i], txtNoStopWords);
        freqAfterRemoveStopWord = calculateWordFrequency(txtNoStopWords)
        freqOfStopWords = calculateWordFrequency(stopfreq)
        print("After remove stopword frequency: ", freqAfterRemoveStopWord)
        print("Stopword frequency: ", freqOfStopWords)
        sort = sortWordFreq(freqAfterRemoveStopWord)

        arr = [freqAfterRemoveStopWord,freqOfStopWords]
        for a in arr:
            drawLine(a,places[i])

        #i += 1
#####################################################

##################### BOYER MOORE ###################
NO_OF_CHARS = 256
def badCharHeuristic(string, size):

    badChar = [-1] * NO_OF_CHARS
    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i;
        # retun initialized list
    return badChar

def BoyerMoore(txt, pat):
    listNum=[]
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while (s <= n - m):
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            listNum.append(s)
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:

            s += max(1, j - badChar[ord(txt[s + j])])

    return listNum
###################################################################
#Q7,8,9------------------postive_negative-------------------------#
def positiveNegative():
    f = open("negative.txt", 'r', encoding='utf-8')
    negativeWords = f.read().lower().splitlines()
    negativeWordsFound = []
    f.close()
    f = open("positive.txt", 'r', encoding='utf-8')
    positiveWords = f.read().lower().splitlines()
    positiveWordsFound = []
    f.close()
    textfiles = ["!Jakarta.txt","!Bangkok.txt","!Taipei.txt","!Hong_Kong.txt","!Tokyo.txt","!Beijing.txt","!Seoul.txt"]
    i=0
    for input in textfiles:
        readFile = open(input, 'r', encoding='utf-8')
        readFiles = readFile.read().lower()
        print("<==", input, "==>")
        for pw in positiveWords:
            index = BoyerMoore(readFiles,pw)
            if index != []:
                positiveWordsFound.append(readFiles[index[0]:index[0] + len(pw)])
        for nw in negativeWords:
            index = BoyerMoore(readFiles,nw)

            if index != []:
                negativeWordsFound.append(readFiles[index[0]:index[0] + len(nw)])
        strip = stripNonAlphaNum(readFiles)
        print("Positve word found in text: ", positiveWordsFound)
        print("Negative word found in text: ", negativeWordsFound)
        posfreq,negfreq,neutral = removePositiveNegative(positiveWordsFound,negativeWordsFound,strip)
        positiveFreq = calculateWordFrequency(posfreq)
        negativeFreq = calculateWordFrequency(negfreq)
        neutralFreq = calculateWordFrequency(neutral)
        print("Positive word frequency:", positiveFreq)
        print("Negative word frequency:", negativeFreq)
        print("Neutral word frequency:", neutralFreq)
        drawHistogram(positiveFreq, negativeFreq, input)
        conclusion(positiveFreq, negativeFreq, neutralFreq, input)
    #i+=1
def removePositiveNegative(pos,neg,txt):
    posfreq = []
    negfreq = []
    neutralfreq = []

    for i in txt:
        if i in pos:
            posfreq.append(i)
        elif i in neg:
            negfreq.append(i)
        else:
            neutralfreq.append(i)

    print("Neutral words = ", neutralfreq)
    # print("Postive words = ", posfreq)
    # print("Negative words = ", negfreq)
    return posfreq, negfreq, neutralfreq


def drawHistogram(pos,neg,t):
    x = []
    y = []
    xn = []
    yn = []
    for keys, values in pos.items():
        x.append(keys)
        y.append(values)
    for keysn,valuesn in neg.items():
        xn.append(keysn)
        yn.append(valuesn)

    fig = go.Figure()
    fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="positive"))
    fig.add_trace(go.Histogram(histfunc="sum", y=yn, x=xn, name="negative"))
    fig.update_layout(
        title = t,
        xaxis_title="Words",
        yaxis_title="Frequency",

    )
    fig.show()

def conclusion(freqp,freqn,neutral,input):

    sump=0
    sumn=0
    sumneutral =0
    for keys,values in freqp.items():
        sump+=values
    for keys,values in freqn.items():
        sumn+=values
    for keys,values in neutral.items():
        sumneutral+=values
    print("Sum of positive words: ",sump)
    print("Sum of negative words: ",sumn)
    print("Sum of neutral words: ",sumneutral)
    conclusionGraph(sump,sumn,input)

    if sump>sumn:
        print("The article is giving a postive sentiment.")
    else:
        print("The article is giving a negative sentiment.")


def conclusionGraph(pos,neg,input):
    labels = ["Positive", "negative"]
    values = [pos, neg]
    colors = ['red', 'blue']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial',title=input
                                 )])
    fig.show()
#main();
positiveNegative()

