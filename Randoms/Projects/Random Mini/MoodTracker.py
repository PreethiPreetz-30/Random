import os
from time import sleep

def heading():
    print("********************************************************")
    print("\t\t\tMOOD TRACKER")
    print("********************************************************")
    print()

def calculate(my_score):
    heading()
    _=os.system('cls')
    print("\n\nCalculating......")
    sleep(5)
    _ = os.system('cls')
    heading()
    if my_score <=100:
        print("You are rather unhappy with your current life. \nYou dont feel complete in who you are .Thats why you often get self-conscious and frustrated.")
        print()
        print("If you really want to find happiness just start looking and do some soul searcing. \nTry to figure out whoyou want to be as a person and strive for that.")
    elif my_score<=140:
        print("You're quite happy in life.\nY You're friendly, laid-back, and spontaneous. \mYou love helping others and spending time with the people you care about most. So, you're basically in the perfect golden middle!")
        print()
        print("You are only steps away from ultimate happiness. Start looking for different perspectives and possible approaches that might broaden your horizon.")
    else:
        print("You certainly know what happiness is! \nYou're one of those rare types that light up the room and make everybody around them feel better. And that’s because you're content with yourself and don't see others as your competition.")
        print()

#array pattern = [question,option1,option2,option3]
questions=[
    ["How would you describe your life?","Fortunate","Unpredictable","Boring"],
    ["How do you feel in the morning?","Awful","A bit tired","Refreshed"],
    ["Do you meditate?","I've been planning on giving it a go","No, I don't really have time for that","Absolutely"],
    ["How much time do you spend on social media?","I'm always online","5 hours more or less","2 hours or less"],
    ["Whats the first thought that comes to your mind whenever you face a serious problem?","Why me?","I got this!","Well it's annoying but no time for whining"],
    ["Do you have a pet?","Yes and I love him/her","No and I, dont plan on it","No but someday"],
    ["How often does your body get exercise?","I wouldn't call it exercise","Regularly","Every now and then"],
    ["What do you usually discuss with your friends?","Our lives and feelings","Just gossip","New ideas, work and adventures"],
    ["Do you try to fit in where ever you go?","Yes.I want to be accepted","Some times I'll make an effort to adapt","If I fit in then I fit in.Not gonna change myself."],
    ["Your friend gifts you a present you dont like.What would you do?","Keep it.They put effort into it.","Gift it to someone else.They might like it","Let them know and try to exchange it at the store"],
    ["Whats your biggest aspiration in life?","To have a loving circle of relationships","To find peace and happily settle down","To own a nice house and be rich"],
    ["Your friend wins a phone where as you get some cash at a loterry. How do you feel","Happy for my frind and to have got some extra cash","A bit dissapointed but still happy","Feel a little jealous"]
    ]
score=[
    [5,10,15],[5,10,15],[10,5,15],[5,10,15],[5,15,10],
    [13,5,10],[5,15,10],[10,5,15],[5,10,15],[15,10,5],
    [15,10,5],[15,10,5]
    ]
my_score=0

heading()
print(" \t\t  Good day to you! \n \t\tLets test your mood today.")
sleep(5)

for i in range(0,len(questions)):
    _ = os.system('cls')
    heading()
    print("Question: ",i,"/",len(questions),"\n")
    print(questions[i][0])
    for j in range(1,len(questions[i])):print(j,": ",questions[i][j])
    print()
    n=int(input("Enter your choice(1/2/3): "))
    my_score+=n

calculate(my_score)

print("***************************************************")
a = input('Press any key to exit')
if a:
    exit(0)
