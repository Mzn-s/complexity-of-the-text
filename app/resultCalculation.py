def DaleChallCalculation(value):
    if value < 5.0: result = "Very easy to read (4th Grade and below). Lvl: A1"
    if value >= 5.0 and value < 6.0: result = "Easy to read (5th & 6th Grade). Lvl: A2"
    if value >= 6.0 and value < 7.0: result = "Conversational English (7th & 8th Grade). Lvl: B1"
    if value >= 7.0 and value < 8.0: result = "Conversational English (8th & 10th Grade). Lvl: B2"
    if value >= 8.0 and value < 9.0: result = "Fairly difficult to read (11th & 12th Grade). Lvl: C1"
    if value >= 9.0 and value < 10.0: result = "Difficult to read (College). Lvl: C1-C2"
    if value >= 10.0: result = "Very difficult to read (College Graduate). Lvl: C2"
    return result

def FleschKincaidCalculation(value):
    if value >= 90.0: result = "Very easy to read (4th Grade and below). Lvl: A1"
    if value >= 80.0 and value < 90.0: result = "Easy to read (5th & 6th Grade). Lvl: A2"
    if value >= 70.0 and value < 80.0: result = "Conversational English (7th & 8th Grade). Lvl: B1"
    if value >= 60.0 and value < 70.0: result = "Conversational English (8th & 10th Grade). Lvl: B2"
    if value >= 50.0 and value < 60.0: result = "Fairly difficult to read (11th & 12th Grade). Lvl: C1"
    if value >= 30.0 and value < 50.0: result = "Difficult to read (College). Lvl: C1-C2"
    if value >= 10.0 and value < 30.0: result = "Very difficult to read (College Graduate). Lvl: C1-C2"
    if value < 10.0: result = "Extremely difficult to read (Professional). Lvl: C2"
    return result

def ColemanLiauCalculation(value):
    if value == "---":
        return "Для точной оценки необходим текст длиной минимум 100 слов."
    if value < 5.0: result = "Very easy to read (4th Grade and below). Lvl: A1"
    if value >= 5.0 and value < 7.0: result = "Easy to read (5th & 6th Grade). Lvl: A2"
    if value >= 7.0 and value < 11.0: result = "Conversational English (7th & 9th Grade). Lvl: B1"
    if value >= 11.0 and value < 13.0: result = "Fairly difficult to read (10th & 12th Grade). Lvl: B2"
    if value >= 13.0 and value < 17.0: result = "Difficult to read (College). Lvl: C1"
    if value >= 17.0: result = "Very difficult to read (College Graduate). Lvl: C2"
    return result

def ARICalculation(value):
    if value < 5.0: result = "Very easy to read (4th Grade and below). Lvl: A1"
    if value >= 5.0 and value < 7.0: result = "Easy to read (5th & 6th Grade). Lvl: A2"
    if value >= 7.0 and value < 9.0: result = "Conversational English (7th & 8th Grade). Lvl: B1"
    if value >= 9.0 and value < 10.0: result = "Conversational English (8th & 9th Grade). Lvl: B2"
    if value >= 10.0 and value < 11.0: result = "Conversational English (10th & 11th Grade). Lvl: C1"
    if value >= 11.0 and value < 14.0: result = "Conversational English (11th & 12th Grade). Lvl: C1-C2"
    if value >= 14.0: result = "Difficult to read (College). Lvl: C2"
    return result

def SMOGCalculate(value):
    if value < 3.0: result = "Very easy to read (4th Grade and below). Lvl: A1"
    if value >= 3.0 and value < 12.0: result = "Easy to read (5th & 6th Grade). Lvl: A2"
    if value >= 12.0 and value < 21.0: result = "Conversational English (7th & 8th Grade). Lvl: B1"
    if value >= 21.0 and value < 43.0: result = "Conversational English (8th & 9th Grade). Lvl: B2"
    if value >= 43.0 and value < 57.0: result = "Fairly difficult to read (10th & 11th Grade). Lvl: C1"
    if value >= 57.0 and value < 73.0: result = "Fairly difficult to read (11th & 12th Grade). Lvl: C1-C2"
    if value >= 73.0 and value < 91.0: result = "Fairly difficult to read (12th Grade). Lvl: C1-C2"
    if value >= 91.0 and value < 133.0: result = "Difficult to read (College). Lvl: C1-C2"
    if value >= 133.0 and value < 211.0: result = "Very difficult to read (College Graduate). Lvl: C1-C2"
    if value >= 211.0: result = "Extremely difficult to read (Professional). Lvl: C2"
    return result

def calculateIndex(method, value):
    result = ""
    if method == "DC" : result = DaleChallCalculation(value)
    if method == "FK" : result = FleschKincaidCalculation(value)
    if method == "CL" : result = ColemanLiauCalculation(value)
    if method == "ARI" : result = ARICalculation(value)
    if method == "SMOG" : result = SMOGCalculate(value)
    return result