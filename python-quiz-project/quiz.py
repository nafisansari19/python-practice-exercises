class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0

        #q_list will represent the question bank when called from quiz-main.py
        self.question_list = q_list

    def next_question(self):
        # set current_question to question bank index
        current_question = self.question_list[self.question_number]
        # add 1 to question_number to cycle to next question
        self.question_number += 1
        # Get user answer using format to input current question number and question
        user_answer = input(f"{self.question_number}: {current_question.question} (True/False): ")
        # check to see if answers match
        self.check_answer(user_answer, current_question.answer)

    def remaining_questions(self):
        # check to see if the current question number is less than the amount of questions
        return self.question_number < len(self.question_list)

    # checking answers and keeping score
    def check_answer(self, user_answer, answer):
        # use .lower() to lowercase all letters
        if user_answer.lower() == answer.lower():
            # if correct add 1 to score and print message
            self.score += 1
            print("Awesome, You got it right!")
        else:
            print("Oops, you got it wrong!")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")