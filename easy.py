#importing modules
import random
import time

def easygame( ):
    "This function is will work as Easy Mode for mathbro"
    #creating variables
    mode=None 
    arithmeticoperator={}
    numbers=[]
    pro_question=''
    real_answer=''
    user_answer=''
    roundcount=None
    chances=None
    count=None
    status=None
    answercount=None
    presentage=None
    gameData=[]
    otherData=[]
    resulttext=None
    Question=None
    Uanswer=None
    Canswer=None


    #assigning as specification
    mode='Easy'
    arithmeticoperator={'operaton':['+','-',]}
    numbers=[0,1,2,3,4,5,6,7,8,9,10]
    roundcount=int(1)
    answercount=int(0)
    chances=5
    count=0

    # print Mode
    print("\n",mode," Mode")

    #creat loop for generate questions
    while count<chances:
        
        # Generating questions
        num1=(random.choice(numbers))
        operator=random.choice(arithmeticoperator['operaton'])
        num2=int(random.choice(numbers))

        #print round count
        time.sleep(1)
        print (f"\nQ {roundcount})")

        #Display question
        pro_question=f"{num1} {operator} {num2}"
        print("Question : ",pro_question,'?')

        #real answer to question
        real_answer=eval(pro_question)

        #getting answer from user
        #detect value errors and repert untill correct format enters
        while user_answer!=ValueError:
            try:
                user_answer=int(input("Your answer :"))
                break
            except:
                print("\nInvalid format! Try again.")

        time.sleep(1)

        #Find is answer correct or not and print correct or not with correct answer
        if real_answer==user_answer:
            print("correct")
            status="Correct"
            
            #Recode for answer count
            answercount=answercount+1
        else:
            print("Incorrect")
            status="Incorrect"
        
        # store Game Data
        gameData.append({'Question':pro_question,'user':user_answer,'com':real_answer,'sta':status,})

        #chance to break form loop
        count+=1
        roundcount+=1

    #Print Game data
    print("\nResult sheet")
    for y in range(len(gameData)):
        Question=gameData[y]["Question"]
        Uanswer=gameData[y]["user"]
        Canswer=gameData[y]["com"]

        if Uanswer==Canswer:
            resulttext = f"✓ {Question} = {Uanswer}"
        else:
            resulttext = f"✕ {Question} = {Uanswer} correct answer is {Canswer}"

        print(resulttext)

    #calculation presentage
    presentage=format(answercount/chances*100,'.1f')+"%"

    time.sleep(1)
    
    #print other details
    print("\nTotal Questions : ",chances)
    print("Correct questions : ",answercount)
    print("Presentage : ",presentage) 
    print("Level :",mode)   
        
    otherData.append({"total":chances,'corr':answercount,'pre':presentage,'mod':mode})
    return gameData,otherData