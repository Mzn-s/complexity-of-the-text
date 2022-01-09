import re
import math
from app.resultCalculation import calculateIndex

def toFixed(numObj, digits=0):
    if not isinstance(numObj, str):
        return f"{numObj:.{digits}f}"
    else:
        return numObj

def GetWordsCount(Sentences):
    result = 0
    for x in Sentences:
        result += len(x.split())
    return result


def GetDifficultWordsCount(Text):
    count = 0
    file = open('static/DaleChallEasyWordList.txt','r')
    text = file.read()

    words = re.split(' ', Text)
    for w in words:
        if w.lower() not in text:
            count += 1
    return count


def DaleChallIndexCheck(Text, WordsCount, SentencesCount):
    DifficultWordsCount = GetDifficultWordsCount(Text)
    result = 0.1579 * (DifficultWordsCount / WordsCount * 100) + 0.0496 * (WordsCount / SentencesCount)
    if result > 5:
        result += 3.6
    return result


def SyllablesCount(CleanText):
    text = CleanText.split()
    count = 0
    for word in text:
        count += len(
            re.findall('(?!e$)[aeiouy]+', word, re.I) +
            re.findall('^[^aeiouy]*e$', word, re.I)
        )
    return count


def FleschKincaidIndexCheck(ASL, ASW):
    return 206.835 - 1.015 * ASL - 84.6 * ASW

def ClearPunctSymbols(Text):
    return re.sub('[^a-zA-Z0-9]+', ' ', Text)

def GetSentencesList(Text):
    resultSentences = []
    t = re.sub(' +', ' ', Text)


    Sentences = re.split('\n|\\?|\\!|\\;|\\.', t.strip())
    for i in Sentences:
        if len(i) > 0 and not i.isspace() and not re.match('^[\d.]+$', i):
            resultSentences.append(i)
    return resultSentences

def ColemanLiauIndexCheck(WordsCount, CleanText, Text):
    if WordsCount > 100:
        HundredWords = ' '.join(Text.split()[:100])
        ClearHundredWords = CleanText.split()[:100]
        L = len(''.join(ClearHundredWords))
        S = len(GetSentencesList(HundredWords))

        return 0.0588 * L - 0.296 * S - 15.8
    else:
        return "---"


def ARIIndexCheck(CleanText, WordsCount, SentencesCount):
    SymbolCount = len(CleanText.replace(' ', ''))
    return 4.71 * (SymbolCount / WordsCount) + 0.5 * (WordsCount / SentencesCount) - 21.43


def SMOGIndexCheck(text, SentencesCount):
    PolysyllablesWordsCount = 0
    #if SentencesCount > 30:
    for word in text.split():
        SyllablesCount = len(
              re.findall('(?!e$)[aeiouy]+', word, re.I) +
              re.findall('^[^aeiouy]*e$', word, re.I)
        )
        if SyllablesCount >= 3:
           PolysyllablesWordsCount += 1
    return 1.0430 * math.sqrt(30 * (PolysyllablesWordsCount / SentencesCount)) + 3.1291



def runDetermine(Text):
    CleanText = ClearPunctSymbols(Text)
    Sentences = GetSentencesList(Text)
    WordsCount = GetWordsCount(Sentences)
    SentencesCount = len(Sentences)
    ASL = WordsCount / SentencesCount
    ASW = SyllablesCount(CleanText) / WordsCount

    DaleChallIndexResult = DaleChallIndexCheck(CleanText,  WordsCount, SentencesCount)
    FleschKincaidIndexResult = FleschKincaidIndexCheck(ASL, ASW)
    ColemanLiauIndexResult = ColemanLiauIndexCheck(WordsCount, CleanText, Text)
    ARIIndexResult = ARIIndexCheck(CleanText, WordsCount, SentencesCount)
    SMOGIndexResult = SMOGIndexCheck(CleanText, SentencesCount)

    """print("Result Dale Chall Index : ", DaleChallIndexResult)
    print("Result Flesch Kincaid Index : ", FleschKincaidIndexResult)
    print("Result Coleman Liau Index : ", ColemanLiauIndexResult)
    print("Result ARI Index : ", ARIIndexResult)
    print("Result SMOG Index : ", SMOGIndexResult)"""

    resultContent = {
        "Dale Chall Index"    : {"value": toFixed(DaleChallIndexResult, 2),
                       "index": calculateIndex("DC", DaleChallIndexResult)},
        "Flesch Kincaid Index": {"value": toFixed(FleschKincaidIndexResult, 2),
                       "index": calculateIndex("FK", FleschKincaidIndexResult)},
        "Coleman Liau Index"  : {"value": toFixed(ColemanLiauIndexResult, 2),
                       "index": calculateIndex("CL", ColemanLiauIndexResult)},
        "ARI Index" : {"value": toFixed(ARIIndexResult, 2),
                       "index": calculateIndex("ARI", ARIIndexResult)},
        "SMOG Index": {"value": toFixed(SMOGIndexResult, 2),
                 "index": calculateIndex("SMOG", SMOGIndexResult)},
    }

    if SentencesCount < 30 : resultContent['SMOG Index']['index'] += " | Для более точной оценки необходим текст длиной минимум 30 предложений."
    return resultContent