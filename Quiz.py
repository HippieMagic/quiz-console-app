import random


class QuizQuestion:
    def __init__(self, question_text, answers, correct_answer_index):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer_index = correct_answer_index


class Quiz:
    def __init__(self):
        self.questions = []

    def load_questions_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        current_question = None
        is_reading_question = False
        is_reading_answers = False

        for line in lines:
            line = line.strip()
            if not line or line.startswith("*"):
                continue

            if line.startswith("@Q"):
                is_reading_question = True
                current_question = QuizQuestion("", [], -1)
                continue

            if line.startswith("@A"):
                is_reading_question = False
                is_reading_answers = True
                continue

            if line.startswith("@E"):
                is_reading_answers = False
                self.questions.append(current_question)
                continue

            if is_reading_question:
                current_question.question_text += line + " "
            elif is_reading_answers:
                if line.isdigit():
                    current_question.correct_answer_index = int(line) - 1
                else:
                    current_question.answers.append(line)

        random.shuffle(self.questions)

    def start(self, num_of_questions):
        asked_questions = 0
        correct_answers = 0

        for question in self.questions[:num_of_questions]:
            print(question.question_text)
            for idx, answer in enumerate(question.answers):
                print(f"{idx + 1}. {answer}")

            user_answer = int(input("Enter the number of the correct answer: ")) - 1
            if user_answer == question.correct_answer_index:
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect.")

            asked_questions += 1

        accuracy = (correct_answers / asked_questions) * 100 if asked_questions else 0
        print(
            f"Quiz completed. Questions asked: {asked_questions}, Correct answers: {correct_answers}, Accuracy: {accuracy:.2f}%")

    def start_new_quiz(self):
        file_path = input("Please enter your file location: ").strip().replace("\"", "")
        self.load_questions_from_file(file_path)

        num_of_questions = int(input("How many questions would you like to answer? "))
        self.start(num_of_questions)


def main():
    quiz = Quiz()
    quiz.start_new_quiz()


if __name__ == "__main__":
    main()
