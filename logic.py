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