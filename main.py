import pyttsx3
import random
from details import periodic_table, Element  


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change voice
engine.setProperty('rate', 180)  

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
welcome=f"""
 WELCOME TO 
        CHEMISTRY UNVEILED:
                  THE ULTIMATE PERIODIC TABLE!!!
                  """
print(welcome)
speak_text(welcome)

def display_element(element):
    print(" =============================================")
    info = f"""
    Element Name   : {element.name}
    Symbol         : {element.symbol}
    Atomic Number  : {element.atomic_number}
    Atomic Weight  : {element.atomic_weight}
    Group          : {element.group}
    Period         : {element.period}
    Nature         : {element.group_block}
    Block          : {element.block}
    State          : {element.state}
    Year Discovered: {element.year_discovered}
    Inventor       : {element.inventor}
    """
    print(info)
    speak_text(info)
    print(" =============================================")

def search_element(search_term):
    for element in periodic_table:
        if (element.symbol.lower() == search_term.lower() or
            element.name.lower() == search_term.lower() or
            str(element.atomic_number) == search_term):
            return element
    return None

def compare_elements(element1, element2):
    attributes = ['name', 'symbol', 'atomic_number', 'atomic_weight', 'group', 'period', 'group_block', 'block', 'state', 'year_discovered', 'inventor']
    comparison_result = f"Comparison between {element1.name} and {element2.name}:\n"

    for attr in attributes:
        value1 = getattr(element1, attr)
        value2 = getattr(element2, attr)
        comparison_result += f"{attr.capitalize()}: {value1} vs {value2}\n"

    print(comparison_result)
    speak_text(comparison_result)

def quiz():
    score = 0  # Initialize score
    total_questions = 0  # Initialize total questions asked

   
    question_types = [
        ('atomic_number', lambda e: f"What is the atomic number of {e.name}?", lambda e: str(e.atomic_number)),
        ('symbol', lambda e: f"What is the symbol of {e.name}?", lambda e: e.symbol),
        ('atomic_weight', lambda e: f"What is the atomic weight of {e.name}?", lambda e: str(e.atomic_weight)),
        ('group', lambda e: f"What is the group number of {e.name}?", lambda e: str(e.group)),
        ('period', lambda e: f"What is the period number of {e.name}?", lambda e: str(e.period)),
        ('block', lambda e: f"What is the block of {e.name}?", lambda e: e.block),
        ('state', lambda e: f"What is the state of {e.name} at room temperature?", lambda e: e.state),
        ('year_discovered', lambda e: f"In what year was {e.name} discovered?", lambda e: str(e.year_discovered))
    ]
    
    while True:
        element = random.choice(periodic_table)
        attr, question_func, answer_func = random.choice(question_types)
        question = question_func(element)
        correct_answer = answer_func(element)
        
        print(question)
        speak_text(question)
        
        answer = input("Your answer: ").strip()
        speak_text(f"Your answer: {answer}")
        
        if answer.lower() == correct_answer.lower():
            score += 1  
            response = "You gave the correct answer!"
            print(response)
            speak_text(response)
        else:
            response = f"You gave the wrong answer. The correct answer is {correct_answer}."
            print(response)
            speak_text(response)
        
        total_questions += 1  
        
        continue_quiz = input("Do you want to play more? (yes/no): ").strip()
        speak_text(f"Do you want to play more? {continue_quiz}")
    
        if continue_quiz.lower() not in ['yes', 'y']:
            print(f"Your final score is {score} out of {total_questions}.")
            speak_text(f"Your final score is {score} out of {total_questions}.")
            break


def main():
    while True:
        action_text = """
        What would you like to do?
        1. Search for an element
        2. Compare two elements
        3. Play a quiz
        4. Exit
        """
        print(action_text)
        speak_text(action_text)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            search_term = input("Enter element name, symbol, or atomic number: ").strip()
            element = search_element(search_term)
            if element:
                display_element(element)
            else:
                not_found_message = "Element not found!"
                print(not_found_message)
                speak_text(not_found_message)
        
        elif choice == '2':
            term1 = input("Enter the first element name, symbol, or atomic number: ").strip()
            speak_text(f"Enter the first element name, symbol, or atomic number: {term1}")
            element1 = search_element(term1)
            if element1:
                term2 = input("Enter the second element name, symbol, or atomic number: ").strip()
                speak_text(f"Enter the second element name, symbol, or atomic number: {term2}")
                element2 = search_element(term2)
                if element2:
                    compare_elements(element1, element2)
                else:
                    not_found_message = "Second element not found!"
                    print(not_found_message)
                    speak_text(not_found_message)
            else:
                not_found_message = "First element not found!"
                print(not_found_message)
                speak_text(not_found_message)

        elif choice == '3':
            quiz()

        elif choice == '4':
            exit_message = "Thank you for using the periodic table program. Goodbye!"
            print(exit_message)
            speak_text(exit_message)
            break
        
        else:
            invalid_choice = "Invalid choice! Please choose between 1 and 4."
            print(invalid_choice)
            speak_text(invalid_choice)

if __name__ == "__main__":
    main()
