###########################################
#other good games and quizzes to make: 
"""
- Dice game 
- Color game 
- Mastermind based text code game 
- wordle/word guessing game 
- Which animal are you quiz
    - We could do machine learning based quizzes that have numbers next to each option and make people type in the number of the option that they like. 
- Hangman game
- Custom text story game (choose a theme, enter characters, enter animals, pre-built stories, etc)
"""
"""
Could also make a utilities list 
- A calculator 
"""
############################################

import pandas
from sklearn.tree import DecisionTreeClassifier
from csv import writer
from random import randint, choice
import time 


def HappyQuiz():
  #Questions to get data 
  Q1 = int(input("ChatBot: On a scale of 1-5, do you have a lot of money? (1 = Broke, 5 = Rich): "))
  print("")
  Q2 = int(input("ChatBot: On a scale of 1-5, do you keep your problems to yourself? (1 = Never, 5 = Always): "))
  print("")
  Q3 = int(input("ChatBot: On a scale of 1-5, do you get sad easily? (1 = Barely, 5 = Very): "))
  print("")
  Q4 = int(input("ChatBot: On a scale of 1-5, do you refuse to give up, no matter how tough things get? (1 = Never, 5 = Always): "))
  print("")
  Q5 = int(input("ChatBot: On a scale of 1-5, can you find something positive in even the most difficult situations? (1 = Never, 5 = Always): "))
  print("")
  
  #initilize reading of the file 
  HappyDataFile = pandas.read_csv("happy.csv")
  
  #Changes Happy to "1" and Unhappy to "2" in the csv file
  #Creation of dictionary 
  HDict = {'Happy': 1, 'Unhappy': 0}
  #Maps the happiness labels in the csv file to 1 and 2 for happy and unhappy respectively
  HappyDataFile ['Happiness'] = HappyDataFile['Happiness'].map(HDict)
  
  
  features = ['Money', 'Problems', 'Depression', 'Toughness', 'Positivity']
  X = HappyDataFile [features]
  y = HappyDataFile ['Happiness']
  
  
  DataTree = DecisionTreeClassifier()
  DataTree.fit(X, y) #X is the sample values, and y is the target value 
  
  #Predicts the happiness result based on the data
  result = DataTree.predict([[Q1, Q2, Q3, Q4, Q5]])
  
  if result == 1:
    print("ChatBot: You're Happy")
    print("😎👌🔥👌😎")
    print("")
    result = "Happy"
  else: 
    print("ChatBot: You're Unhappy")
    print("😭😔💔😔😭")
    result = "Unhappy"
  
  #Appends the new data to the csv file
  List = [Q1, Q2, Q3, Q4, Q5, result]
  
  with open('happy.csv', 'a') as datafile: #puts the csv file in append mode
      HappyWriter = writer(datafile) #makes a writer object 
      HappyWriter.writerow(List) #writes down the results in a new row
      datafile.close() #closes the file 

def GenderQuiz():
  #Questions to get data 
  Q1 = int(input("ChatBot: On a scale of 1-5, do you worry about things that turn out to be unimportant? (1 = Not really, 5 = A lot): "))
  print("")
  Q2 = int(input("ChatBot: On a scale of 1-5, do you get stressed out easily? (1 = Not really, 5 = A lot):  "))
  print("")
  Q3 = int(input("ChatBot: On a scale of 1-5, do you get upset by unpleasant thoughts that come into my mind? (1 = Not really, 5 = A lot):  "))
  print("")
  Q4 = int(input("ChatBot: On a scale of 1-5, do you not easily get disturbed by events? (1 = Not really, 5 = A lot):  "))
  print("")
  Q5 = int(input("ChatBot: On a scale of 1-5, do you show your sadness? (1 = Not really, 5 = A lot):  "))
  print("")
  
  #initilize reading of the file 
  GenderDataFile = pandas.read_csv("gender.csv")
  
  #Changes Happy to "1" and Unhappy to "2" in the csv file
  #Creation of dictionary 
  GDict = {'Male': 1, 'Female': 0}
  #Maps the happiness labels in the csv file to 1 and 2 for happy and unhappy respectively
  GenderDataFile ['Gender'] = GenderDataFile['Gender'].map(GDict)
  
  
  questions = ['Question1','Question2','Question3','Question4','Question5']
  X = GenderDataFile [questions]
  y = GenderDataFile ['Gender']
  
  
  DataTree = DecisionTreeClassifier()
  DataTree.fit(X, y) #X is the sample values, and y is the target value 
  
  #Predicts the happiness result based on the data
  result = DataTree.predict([[Q1, Q2, Q3, Q4, Q5]])
  
  if result == 1:
    print("ChatBot: You're a Male")
    print("👨🏻👌♂👌👨🏻")
    print("")
    result = "Male"
  else: 
    print("ChatBot: You're a Female")
    print("👩🏻👌♀👌👩🏻")
    result = "Female"
  
  #Appends the new data to the csv file
  List = [Q1, Q2, Q3, Q4, Q5, result]
  
  with open('gender.csv', 'a') as datafile: #puts the csv file in append mode
      GenderWriter = writer(datafile) #makes a writer object 
      GenderWriter.writerow(List) #writes down the results in a new row
      datafile.close() #closes the file 

def AnimalQuiz():
  #Questions to get data 
  print("For the Animal Quiz, you will be asked a series of questions. Type the number of the option that you choose for each question.")
  
  Q1 = int(input("ChatBot: Choose your favorite hobby:\n1. Go to the park\n2. Explore nature\n3. Read\n4. Take naps\n5. Exercise\n6. Swim\nYou: "))
  print("")
  
  Q2 = int(input("ChatBot: What do you like to eat the most:\n1. Salad\n2. Peanuts\n3. Chicken\n4. Tuna\n5. Veggies\n6. Fruit\nYou: "))
  print("")
  
  Q3 = int(input("ChatBot: What's your personality like:\n1. Funny\n2. Sassy\n3. Outgoing\n4. Brave\n5. Caring\n6. Friendly\nYou: "))
  print("")
  
  Q4 = int(input("ChatBot: What type of personality would you like your pet to have:\n1. Caring\n2. Great hearing\n3. Playful\n4. Loves the outdoors\n5. Loves to cuddle\n6. Mean\nYou: "))
  print("")
  
  #initilize reading of the file 
  AnimalDataFile = pandas.read_csv("animal.csv")
  
  #Changes the animals to their respective numbers in the csv file
  #Creation of dictionary 
  ADict = {'Hamster': 0, 'Panda': 1}
  #Maps the animal labels in the csv to their respective animal numbers 
  AnimalDataFile ['Animal'] = AnimalDataFile['Animal'].map(ADict)
  
  features = ['Question1','Question2','Question3','Question4']
  X = AnimalDataFile [features]
  y = AnimalDataFile ['Animal']
  
  
  DataTree = DecisionTreeClassifier()
  DataTree.fit(X, y) #X is the sample values, and y is the target value 
  
  #Predicts which animal you are based on the data
  result = DataTree.predict([[Q1, Q2, Q3, Q4]])
  

  AnimalList = ["Hamster", "Panda"]
  print("ChatBot: You're a ", AnimalList[result[0]])
  
  #Appends the new data to the csv file
  result = AnimalList[result[0]]
  List = [Q1, Q2, Q3, Q4, result]
  
  with open('animal.csv', 'a') as datafile: #puts the csv file in append mode
      AnimalWriter = writer(datafile) #makes a writer object 
      AnimalWriter.writerow(List) #writes down the results in a new row
      datafile.close() #closes the file 


def NumberGuessGame():
  SecretNumber = randint(1,1000)
  print ("ChatBot: Guess a number between 1 and 1000. You get 10 tries.")
  num = int(input())
  tries = 10
 
  while True:
      if num > SecretNumber:
        print ( "ChatBot: Guess a smaller number" )
        tries -= 1
        num = int(input())
   
      if num < SecretNumber: 
        print ( "ChatBot: Guess a larger number" )
        tries -= 1
        num = int(input())
           
      if num == SecretNumber: 
        print ("ChatBot: Nice! You guessed the right number!")
        break

      if tries == 0:
        print("ChatBot: You ran out of tries. The number was", SecretNumber)
        break

def RockPaperScissorsGame():
  print("ChatBot: A game of rock, paper, scissors")
  print("ChatBot: PLAYER V.S. CHATBOT")
  
  play = True
  actions = [
    """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
            ]
  
  while play:
    

    print("")
    print("ChatBot: Choose your number!")
    
    Player = int(input("ChatBot: Choose Rock(1), Paper(2), or Scissors(3): "))
    ChatBot = randint(1,3)

    print("")
    print("Player:\n ", actions[Player - 1])
    print("")
    print("ChatBot:\n ", actions[ChatBot - 1])
    print("")
    
    if Player == ChatBot:
      print("It's a tie!")
    elif Player == 1 and ChatBot == 2:
      print("Paper beats rock! ChatBot wins")
    elif Player == 2 and ChatBot == 1:
      print("Paper beats rock! Player wins")
    elif Player == 2 and ChatBot == 3:
      print("Scissors beats paper! ChatBot wins")
    elif Player == 3 and ChatBot == 2:
      print("Scissors beats paper! Player wins")
    elif Player == 3 and ChatBot == 1:
      print("Rock beats scissors! ChatBot wins")
    elif Player == 1 and ChatBot == 3:
      print("Rock beats scissors! Player wins")
  
    again = input("ChatBot: Play again? (y/n): ")
    if "n" in again.lower():
      break

def WordTyperGame():
  total_time = int(input("Enter a certain amount of time in seconds: "))
  words = ["word", "giraffe", "cat", "dog", "computer", "hello", "hi", "coat", "orange", "mouse", "banana", "chocolate", "dog", "elephant", "fantastic", "guitar", "happiness", "island", "jazz", "kangaroo", "laptop", "mountain", "ninja", "orange", "pineapple", "table", "rainbow", "sunny", "tiger","umbrella", "violet", "watermelon", "xylophone", "yoga", "zebra", "astronaut", "butterfly", "crystal", "dragon", "apple", "happy", "table", "music", "water", "house", "light", "dream", "quick", "fancy", "jumps", "jolly", "grape", "piano", "night"]
  
  start_time = time.time()
  time_elapsed = 0
  counter = 0 
  
  while time_elapsed < total_time: 
    word = choice(words)
    print("The word is: ", word)
    type = input("Type: ")
    if type.lower() == word:
      counter += 1 
    time_elapsed = time.time() - start_time
      
    
  print("TIME'S UP!!!")
  print("You typed", counter, "words in", total_time, "seconds")
