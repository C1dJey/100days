class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_quest(self):
        current = self.question_list[self.question_number]
        self.question_number +=1
        u_answer = input(f"Q.{self.question_number} {current.text} (True or False)? ")
        self.check_answer(u_answer, current.answer)
        
    def has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,u_answer, answer):
        if answer.lower() == u_answer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {answer}.")
        print(f"Your currrent score is: {self.score}/{self.question_number}. \n \n")
        

        
        