####################################################
     #The Multilingual Self-Learning Chatbot
####################################################
import json
from difflib import get_close_matches #helps get best responses for my inputs
#from functions import HappyQuiz, GenderQuiz, AnimalQuiz, NumberGuessGame
from functions import * #do to import every function if you want to 

##########################################
#Type annotations are similar to java:
    #example in java - String jsonFile
    #example in python - jsonFile: str
##########################################
# Load the knowledge base from a JSON file
def load_chatbot_datafile(jsonFile):#parameter variable of type 'string'
    with open(jsonFile, 'r') as file: #'r' for read mode, opening in read mode
        data = json.load(file) #'data' variable of type 'dict'
    return data #return a dictionary containing the data from the JSON file.


# Save the updated knowledge base to the JSON file
def save_chatbot_datafile(jsonFile, data):
     #The with statement is used to ensure that the file is properly closed after writing the data, even if an exception occurs. The opened file object is assigned to the variable file.
    with open(jsonFile, 'w') as file: #opening in 'w' for write mode
        json.dump(data, file, indent=2)
    #data is the data (dictionary) that you want to write to the file. file is the file object opened in write mode where the data will be written. indent=2 specifies that the JSON data should be formatted with an indentation level of 2 spaces.

# Find the closest matching statement
#returns a string or nothing
def find_best_match(user_statement: str, statements: list[str]):
    """
    Find the closest matching statement in the JSON data file.
    Parameter - user_statement: The user's input statement.
    Parameter - statements: A list of statements from the JSON data file.
    Returns the closest matching statement or else nothing if no match is found
    """
    matches: list = get_close_matches(user_statement, statements, n=1, cutoff=0.6) #a function that given from the difflib import
    if matches:
      return matches[0] 
    else:
      None


def get_answer_for_statement(statement: str, chatbot_datafile: dict):
    """
    Retrieve the answer for a given statement from the knowledge base.
    :param statement: The matched statement from the knowledge base.
    :param chatbot_datafile: A dictionary containing the knowledge base data.
    :return: The answer to the statement or None if the statement is not found.
    """
   # if "you" in statement.lower():
   #   for q in chatbot_datafile["personal"]:
   #       if q["statement"] == statement:
    #          return q["answer"]
   # else:
    for q in chatbot_datafile["statements"]:
        if q["statement"] == statement:
            return q["answer"]
    return None

##########################################
# Other Languages for the Chatbot to handle 
##########################################

#Main Spanish function to handle user input and respond 
def chatbot_spanish():
    chatbot_datafile: dict = load_chatbot_datafile('spanish.json') 
    while True:
        user_input: str = input("Tu: ")
        best_match: str | None = find_best_match(user_input, [q["statement"] for q in chatbot_datafile["statements"]])
        if user_input.lower() == 'abandonar':
            break
        if best_match:
            answer: str = get_answer_for_statement(best_match, chatbot_datafile)
            print(f"ChatBot: {answer}")
        else:
            print("ChatBot: No sé la respuesta. ¿Puedes enseñarme?")
            new_answer: str = input("Escriba la respuesta o 'saltar' para saltar: ")

            if new_answer.lower() != 'saltar':
                chatbot_datafile["statements"].append({"statement": user_input, "answer": new_answer})
                save_chatbot_datafile('spanish.json', chatbot_datafile)
                print("ChatBot: Gracias! He aprendido algo nuevo.")


# Main Telugu function to handle user input and respond
def chatbot_telugu():
    chatbot_datafile: dict = load_chatbot_datafile('telugu.json') 
    while True:
        user_input: str = input("Nuvvu: ")

        if user_input.lower() == 'vidichipettu':
            break

        best_match: str | None = find_best_match(user_input, [q["statement"] for q in chatbot_datafile["statements"]])
  
        if best_match:
            # If there is a best match, return the answer from the knowledge base
            answer: str = get_answer_for_statement(best_match, chatbot_datafile)
            print(f"ChatBot: {answer}")
        else:
            print("ChatBot: Nakku telidu samadhanam. Nuvvu nakku cheputava?")
            new_answer: str = input("Samadhanam ni rayi lakapote 'skipu' rayi skip cheyatamki: ")

            if new_answer.lower() != 'skipu':
                chatbot_datafile["statements"].append({"statement": user_input, "answer": new_answer})
                save_chatbot_datafile('telugu.json', chatbot_datafile)
                print("ChatBot: Dhanyavadalu. Nennu okati kotadi nerchukunanu.")


# Main English function to handle user input and respond
def chatbot_english():
    """
    Run the chatbot to interact with the user, answer statements, and learn new information.
    The chatbot does the following:
    1. Load the knowledge base from a JSON file.
    2. Continuously prompt the user for statements.
    3. Find the closest matching statement in the knowledge base.
    4. If a match is found, return the answer. Otherwise, ask the user to teach the chatbot.
    5. If the user provides a new answer, add it to the knowledge base and save the updated knowledge base to the JSON file.
    6. Exit the chatbot when the user types 'quit'.
    """
    chatbot_datafile: dict = load_chatbot_datafile('english.json') 
    #the 'dict' is a type annotation that tells us that the 'chatbot_datafile' variable will be a variable of the type 'dict' or dictionary
    while True:
        user_input: str = input("You: ")

        if user_input.lower() == 'quit':
            break
        #Manage different languages
        if "spanish" in user_input.lower():
            chatbot_spanish()

        if "telugu" in user_input.lower():
            chatbot_telugu()

        #Manage playing games
        if "game" in user_input.lower():
          print("ChatBot: Sure! Choose a game to play: \n1. Number Guessing Game\n2. Rock Paper Scissors Game\n3. Word Typer Game")
          playgame_input: str = input("You: ")
          #Call a game
          if "num" in playgame_input.lower() or "1" in playgame_input:
            NumberGuessGame()
          if "rock paper scissors" in playgame_input.lower() or "2" in playgame_input:
            RockPaperScissorsGame()
          if "word" in playgame_input.lower() or "3" in playgame_input:
            WordTyperGame()

        #Manage doing quizzes
        if "quiz" in user_input.lower():
          print("ChatBot: Sure! Choose a quiz to do: \n1. Happiness Quiz\n2. Gender Quiz\n3. Which Animal Are You Quiz")
          playquiz_input: str = input("You: ")  
          #Call a quiz
          if "happ" in playquiz_input.lower() or "1" in playquiz_input:
              HappyQuiz()
          if "gender" in playquiz_input.lower() or "2" in playquiz_input:
              GenderQuiz()
          if "animal" in playquiz_input.lower() or "3" in playquiz_input:
              AnimalQuiz()

        # Finds the best match, otherwise returns None
        best_match = find_best_match(user_input, [q["statement"] for q in chatbot_datafile["statements"]])
  
        if best_match:
            # If there is a best match, return the answer from the knowledge base
            answer: str = get_answer_for_statement(best_match, chatbot_datafile)
            print(f"ChatBot: {answer}")
        else:
            print("ChatBot: I don't know the answer. Can you teach me?")
            new_answer: str = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != 'skip':
                chatbot_datafile["statements"].append({"statement": user_input, "answer": new_answer})
                save_chatbot_datafile('english.json', chatbot_datafile)
                print("ChatBot: Thank you! I've learned something new.")

#Start of the Chatbot!
print("*************************************************************\nFYI: This chatbot's default language is English.\nTo switch to other languages, simply include the name of the language somewhere in your input as you talk to the chatbot.\n*************************************************************")
chatbot_english()
