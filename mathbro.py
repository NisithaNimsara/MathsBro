#import modules
import random
from datetime import datetime
import demo
import easy
import medium
import hard
import sys

#creat variables/File Object
FileObject=None
filename=None
HtmlObject=None
htmlname=None
mode=None
session=0
intell=None
GameData=None
OtherData=None
now=None
nowtime=None
nowdate=None
text0=None
text1=None
Qnumber=None
question=None
answer=None
correct=None
accuracy=None
text2=None
tryagain=None
argulength=None
SavedText=None
details=None

#get current time and date
now=datetime.now()
nowtime=now.strftime("%H:%M") #convert to 24-hour format
nowdate=datetime.now().date()

#creating filename
filename = now.strftime(f"{now.date()}_{now.time().strftime('%H%M')}_{random.randint(100, 999)}.txt")
htmlname = now.strftime(f"{now.date()}_{now.time().strftime('%H%M')}_{random.randint(100, 999)}.html")

#open file object
FileObject=open(filename,"w",encoding="utf-8")

#store Time and date details
text0=f"Date : {nowdate} \nTime : {nowtime}\n"

FileObject.write(text0)
#-----------------------------------------------------Main program----------------------------------------------------
#getting commands from CMD
print("\nWellcome to Mathbro...")
if len(sys.argv)==2:
    mode=str(sys.argv[1])
else:
    mode=str(sys.argv[0])

#creat loop for multiple rounds
while True:
    #Creat directions
    if mode=="-e":
        intell=easy.easygame()
    elif mode=="-m":
        intell=medium.mediumgame()
    elif mode=="-h":
        intell=hard.hardgame()
    else:
        mode="demo"
        intell=demo.demogame()

    #seperating return arguments
    GameData=intell[0]
    OtherData=intell[1]

    #session count
    session+=1

    #------------------------File handling PART----------------------------------------------------------------------
    text1=f"\nSession {session}\nResult sheet\n"
    FileObject.write(text1)

    #store Game data to file
    for x in range(len(GameData)):
        Qnumber=x+1
        question=GameData[x]['Question']
        answer=GameData[x]['user']
        correct=GameData[x]['com']
        accuracy=GameData[x]['sta']
        
        if answer==correct:
            text2= f"✓ {question} = {answer}"
        else:
            text2= f"✕ {question} = {answer} correct answer is {correct}"

        FileObject.write(text2+"\n")

    #store overoll data
    TotalQuestions=OtherData[0]['total']
    CorrectQuestions=OtherData[0]['corr']
    Marks=OtherData[0]['pre']
    Level=OtherData[0]['mod']

    text3=f"\nTotal questions : {TotalQuestions}\nCorrect questions : {CorrectQuestions}\nMarks : {Marks}\nLevel : {Level}"

    FileObject.write(text3+"\n")

    tryagain=input("\nDo you want to Try Again (Yes/No)?").lower()
    
    # Chance to escape from loop
    if (tryagain == str("no")):
        print("\nThank you for playing mathbro...")
        FileObject.close()
        break

    elif(tryagain == str("yes")):
        continue    
    
    else:
        # detecting value error and ignore
        print("\nAssume you want to try again.")
        continue

#----------------------------HTML file--------------------------------------------------------------------------------
#open Html file 
HtmlObject=open(htmlname,"w",encoding="utf-8")

#inport from text file
with open(filename, "r", encoding="utf-8") as SavedText:
    details= SavedText.read()

#Writing HTML file without harm to the structure
HtmlObject.write("<!DOCTYPE html>\n")
HtmlObject.write("<html lang='en'>\n")
HtmlObject.write("<head>\n")
HtmlObject.write("</head>\n")
HtmlObject.write("<body>\n")
HtmlObject.write("<pre>\n")            # Preserve structure of the main text file
HtmlObject.write(details)              # Write copyed details
HtmlObject.write("</pre>\n")
HtmlObject.write("</body>\n")
HtmlObject.write("</html>\n")

#closed Html file
HtmlObject.close()