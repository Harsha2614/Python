questions=("Which planet is known as the Red Planet?",
           "Who wrote “The Discovery of India”?",
           "The largest ocean in the world is:",
           "Which gas do plants absorb during photosynthesis?",
           "Which country is known as the “Land of the Rising Sun?"
           )
options=(
 ("A. Venus","B. Mars","C. Jupiter","D. Saturn"),
 ("A. Mahatma Gandhi","B. Jawaharlal Nehru","C. Rabindranath Tagore","D. Dr. B. R. Ambedkar"),
 ("A. Atlantic Ocean","B. Indian Ocean","C. Pacific Ocean","D. Arctic Ocean"),
 ("A. Nitrogen","B. Carbon dioxide","C. Oxygen","D. Hydrogen"),                                
 ("A. China","B. Japan","C. South Korea","D. Australia")                                       
)


answers = ["B", "B", "C", "B", "B"]
guesses=[]

question_number=0
score=0
for question in questions:
        print("-------------")
        print(question)
        for option in options[question_number]:
                print(option)
        guess=input("Enter A or B or C or D : ").upper()
        guesses.append(guess)
        if guess==answers[question_number]:
            score+=1
            print("Correct")
        else:
                print("INCORRECT")
                print("Correct answer is ",answers[question_number])
        question_number+=1
print("Guesses: ",end=" ")
for x in guesses:
       print(x,end=" ")
print()
print("Answers: ",end=" ")
for x in answers:
       print(x,end=" ")
score=(score/5)*100
print()
print(score)

