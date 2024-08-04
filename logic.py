# from models import UserPerformance, Question, db 

# def get_next_question(user_id, quiz_id):
#     # Fetch current performance data
#     performance = UserPerformance.query.filter_by(user_id=user_id, quiz_id=quiz_id).all()

#     # Determine current difficulty level based on performance
#     current_difficulty = determine_difficulty(performance)

#     # Fetch a question at the current difficulty level
#     question = Question.query.filter_by(quiz_id=quiz_id, difficulty=current_difficulty).first()
#     return question

# def determine_difficulty(performance):
#     # Example logic to adjust difficulty based on performance
#     if not performance:
#         return 3  # Start at medium difficulty

#     correct_ratio = sum(p.correct_answers for p in performance) / sum(p.total_answers for p in performance)
    
#     if correct_ratio > 0.75:
#         return min(5, max(p.difficulty_level for p in performance) + 1)  # Increase difficulty
#     elif correct_ratio < 0.5:
#         return max(1, min(p.difficulty_level for p in performance) - 1)  # Decrease difficulty
#     else:
#         return max(p.difficulty_level for p in performance)  # Maintain current difficulty

# def record_answer(user_id, quiz_id, question_id, is_correct):
#     # Find or create the performance record for the current difficulty
#     question = Question.query.get(question_id)
#     performance = UserPerformance.query.filter_by(user_id=user_id, quiz_id=quiz_id, difficulty_level=question.difficulty).first()
    
#     if not performance:
#         performance = UserPerformance(user_id=user_id, quiz_id=quiz_id, difficulty_level=question.difficulty)
#         db.session.add(performance)
    
#     # Update the performance record
#     performance.total_answers += 1
#     if is_correct:
#         performance.correct_answers += 1
    
#     db.session.commit()

import random
from data import quizzes
import json

QUIZZES = quizzes.QUIZZES

NON_ADAPTIVE_LIMIT = 10



class quiz():
    def __init__(self, quiz_id = None, difficulty_level = None) -> None: # these arg will generates quiz with that quiz id and difficulty level 
        self.difficulty_level = difficulty_level
        self.quiz_id = quiz_id
        self.QUESTIONS = []

    def generateAdaptive(self):
        for quizzez_json in QUIZZES:
            if quizzez_json["quiz_id"] == self.quiz_id:
                self.title = quizzez_json["title"]
                self.description = quizzez_json["description"]
                for question in quizzez_json["questions"]: # loop over questions to find the difficulty level we want
                    if question["difficulty_level"] == self.difficulty_level:
                        self.QUESTIONS.append(question)
                random.shuffle(self.QUESTIONS)
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
            "message": f"Quiz id {self.quiz_id} or difficulty level {self.difficulty_level} not found." # error message 
        }
    
    def generateNonAdaptive(self):
        for quizzez_json in QUIZZES:
            if quizzez_json["quiz_id"] == self.quiz_id:
                self.title = quizzez_json["title"]
                self.description = quizzez_json["description"]
                self.all_questions = quizzez_json["questions"] # goes through questions json file 
                random.shuffle(self.all_questions) # shuffles questions

                index = 0 
                for non_adaptive_question in self.all_questions: # loops over all of the randomly shuffled questions 
                    if index == NON_ADAPTIVE_LIMIT: # checks if its same as limit of whatever I set it to
                        break
                    self.QUESTIONS.append(non_adaptive_question) 
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
    

