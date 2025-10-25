def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 12", "C. 13", "D. 11"],
            "answer": "B"
        },
        {
            "question": "Which language is this program written in?",
            "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
            "answer": "C"
        }
    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == q["answer"]:
            score += 1

    print(f"\nYour total score: {score} out of {len(questions)}")
    return score

if __name__ == "__main__":
    run_quiz()
