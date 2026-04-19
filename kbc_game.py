print("💰💰💰💰KON BANEGA CORERPATI💰💰💰💰💵💵".center(60))
print("Welcome to the game of kon banega corerpati!!!".center(70))
print("Test your knowledge and win prizes💰💰".center(70))
name=str(input("Enter Your Name:"))
age=int(input("Enter your age:"))
questions = [

   {
       "question": "What is the abbreviation of API?",
       "options": [
        "Application Programming Interface",
        "App Producing Interface",
        "Application Programmable Interface",
        "Advertisements Producing Interface"
       ],
       "answer": 0
   },

  {
       "question": "What does CPU stand for?",
        "options": [
        
        "Computer Processing Unit",
        "Central Programming Unit",
        "Central Processing Unit",
        "Control Processing Unit"
       ],
       "answer": 2
  },

  {
    "question": "Which data structure uses FIFO?",
    "options": [
        
        "Stack",
        "Tree",
        "Graph",
        "Queue"
    ],
    "answer": 3
},

{
    "question": "Which of the following is a programming language?",
    "options": [
        
        "HTML",
        "python",
        "HTTP",
        "FTP"
    ],
    "answer": 1
},

{
    "question": "What is the brain of the computer?",
    "options": [
        "CPU",
        "RAM",
        "Hard Disk",
        "Monitor"
    ],
    "answer": 0
},

{
    "question": "Which protocol is used to transfer web pages?",
    "options": [
        
        "FTP",
        "SMTP",
        "HTTP",
        "TCP"
    ],
    "answer": 2
},

{
    "question": "Which keyword is used to define a function in Python?",
    "options": [
        "def",
        "function",
        "fun",
        "define"
    ],
    "answer": 0
},

{
    "question": "Which memory is temporary?",
    "options": [
         
        "ROM",
        "Hard Disk",
        "RAM",
        "CD"
    ],
    "answer": 2
},

{
    "question": "What does SQL stand for?",
    "options": [
        "Structured Query Language",
        "Simple Query Language",
        "Standard Query Logic",
        "System Query Language"
    ],
    "answer": 0
},

{
    "question": "Which one is an operating system?",
    "options": [
        
        "Python",
        "HTML",
        "MySQL",
        "Windows"
    ],
    "answer":3
}

]
i=0
for q in questions:
    print(q["question"])
    print("O.",q["options"][0])
    print("1.",q["options"][1])
    print("2.",q["options"][2])
    print("3.",q["options"][3])
    levels = [1000, 2000, 5000, 10000, 20000, 40000,
          80000, 160000, 320000, 640000]
   
    user_answer=int(input("Enter the option :"))
    if user_answer==q["answer"]:
        print("CORRECT ANSWER")
        print(f"CONGRATULATIONS YOU WON!!!!{levels[i]}")
        i+=1
    else:
        print("SORRY YOU DID A MISTAKE SO YOU ARE OUT OF THE GAME")
        break
print(f"Name of player of Kon Banega corerpati is {name} and got the price of {levels[i-1]}🏆🏆🏆🏆🏆🏆")

price=int(input("Enter the prize money you wonn:"))
if price==640000:
    print("CONGARTULATIONS YOU ARE THE FIRST MEMBER TO WIN THE ENTIRE PRIZE MONEY OF KON BANEGA CORERPATIIIII🏆🏆🏆🏆🏆🏆")
else:
    print("😌OHH YOU MISSED IT TRY AGAIN YOU CAN WIN ANY ONE DAY {GOOD LUCK}💛")
print("Thank You For Playing Kon Banega Corerpati Game🏆💵💰")
    
    
    