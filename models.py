class answer_class:
    def __init__(self, answerText, isCorrect):
        self.answerText = answerText
        self.isCorrect = isCorrect
class question_class:
    def __init__(self, questionText, questionID):
        self.questionText = questionText
        self.answerOptions = []
class case_class:
    def __init__(self, question_group, question_group_text):
        self.question_group = question_group
        self.question_group_text = question_group_text
        self.ques = []


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
