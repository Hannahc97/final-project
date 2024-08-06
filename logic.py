import random # shuffle questions 
from data import quizzes # importing quiz data from py file 
import json
import ast

QUIZZES = quizzes.QUIZZES #Holds the list of quizzes imported from the quizzes.py

NON_ADAPTIVE_LIMIT = 10 # max no of questions that can be asked in non-adaptive

def calculateDifficulty(current_difficulty, results):
    score = 0
    for result in ast.literal_eval(results):
        if "'isTrue': True" in str(result):
            score += 1
    
    if score <= 3:
        if current_difficulty == 1 or current_difficulty == 2:
            return 1
        if current_difficulty == 3:
            return 2

    if score <= 6:
        if current_difficulty == 1:
            return 1
        if current_difficulty == 2 or current_difficulty == 3:
            return 2
    if score >= 7 and score < 10:
        if current_difficulty == 1:
            return 2
        if current_difficulty == 2 or current_difficulty == 3:
            return 3
    if score == 10:
        if current_difficulty == 1:
            return 2
        if current_difficulty == 2 or current_difficulty == 3:
            return 3

    

    


class quiz(): # class named quiz 
    def __init__(self, quiz_id = None, difficulty_level = None) -> None: # these arg will generates quiz with that quiz id and difficulty level 
        self.difficulty_level = difficulty_level
        self.quiz_id = quiz_id
        self.QUESTIONS = [] # initializes an empty list QUESTIONS to hold the questions for the quiz.

    def jsFormat(self):
        QUESTIONS = []
        for questions in self.QUESTIONS:
            QUESTIONS.append({
                "question":questions["text"],
                "options":[option["text"] for option in questions["answers"]],
                "correct":[option["text"] for option in questions["answers"] if option["is_correct"]][0],
            })
        
        return json.dumps(QUESTIONS)

    def generateAdaptive(self): # generates a quiz based on the specified difficulty level
        for quizzez_json in QUIZZES: # loops through each quiz in QUIZZES to find the one matching the quiz_id
            if quizzez_json["quiz_id"] == self.quiz_id:
                self.title = quizzez_json["title"] # If a matching quiz is found, it retrieves the quiz title and description.
                self.description = quizzez_json["description"]
                for question in quizzez_json["questions"]: # loop over questions to find the difficulty level we want
                    if question["difficulty_level"] == self.difficulty_level:
                        self.QUESTIONS.append(question) # appends them to the QUESTIONS list on line 15 
                random.shuffle(self.QUESTIONS) # After gathering the questions, it shuffles them using random.shuffle.
                return {
                    "success": True, # means quiz has been generated, returns a success response containing the quiz details and the selected questions
                    "title": self.title,
                    "description": self.description,
                    "quiz_id": self.quiz_id,
                    "difficulty_level": self.difficulty_level,
                    "questions": self.QUESTIONS
                }
        return {
            "success": False, # quiz with not same id/difficult level will return false, no matching quiz is found, returns a failure response with an error message.
            "message": f"Quiz id {self.quiz_id} or difficulty level {self.difficulty_level} not found." # error message 
        }
    
    def generateNonAdaptive(self): # generates non-adaptive quiz, questions are selected randomly without regard to difficulty.
        for quizzez_json in QUIZZES:
            if quizzez_json["quiz_id"] == self.quiz_id: # checks for a matching quiz_id.
                self.title = quizzez_json["title"] # If found, it retrieves the title and description
                self.description = quizzez_json["description"]
                self.all_questions = quizzez_json["questions"] # goes through questions json file 
                random.shuffle(self.all_questions) # shuffles questions

                index = 0 
                for non_adaptive_question in self.all_questions: # loops over all of the randomly shuffled questions 
                    if index == NON_ADAPTIVE_LIMIT: # checks if its same as limit of whatever I set it to, selects questions up to the NON_ADAPTIVE_LIMIT
                        break
                    self.QUESTIONS.append(non_adaptive_question)  # then appends them to QUESTIONS.
                    index += 1 
                    

                return {
                    "success": True, # means quiz has been generated 
                    "title": self.title,
                    "description": self.description,
                    "quiz_id": self.quiz_id,
                    "difficulty_level": self.difficulty_level,
                    "questions": self.QUESTIONS
                }
        return {
            "success": False, # quiz with not same id/difficult level will return false
            "message": f"Quiz id {self.quiz_id} not found." # error message 
        }
    

