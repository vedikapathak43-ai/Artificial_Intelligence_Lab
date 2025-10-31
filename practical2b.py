from experta import *

# Define a fact class
class StudentFacts(Fact):
    pass


# Define the expert system
class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Statistics'))
    def ai_ds(self):
        print("Suggested Career Path: Artificial Intelligence and Data Science")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Ai Concepts'))
    def ai_ml(self):
        print("Suggested Career Path: Artificial Intelligence and Machine Learning Engineering")


# Main function
def main():
    engine = CareerExpertSystem()
    engine.reset()

    print("Welcome to the Career Path Expert System!")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')

    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip().title()))

    engine.run()


if __name__ == "__main__":
    main()
