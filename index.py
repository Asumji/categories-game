import random

end = False
field = ""
count = -1
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = alphabet[random.randrange(0,len(alphabet) - 1)]

subjects = input("Enter subjects (ex. city,country,river): ")
subjectsBase = subjects.split(",")
subjects = subjects.split(",")

for subject in subjects:
    count += 1
    subjects[count] = subject + ": "
    subjectsBase[count] = subject + ": "
count = -1

field = "Your Letter is " + letter
for subject in subjects:
    field = field + "\n" + subject
print(field)

while end == False:
    answer = input("Enter answer to one of the prompts (ex. 2,answer): ")
    answer = answer.split(",")
    
    subjects[int(answer[0]) - 1] = subjectsBase[int(answer[0]) - 1] + answer[1]
    
    field = "Your Letter is " + letter
    for subject in subjects:
        field = field + "\n" + subject
    print(field)

    answered = []
    wrongStart = False
    for subject in subjects:
        if (subject[len(subject) - 1] != " "):
            answered.append(True)
        else:
            answered = []
    if (len(answered) == len(subjects)):
        for subject in subjects:
            count += 1
            if (subject[len(subjectsBase[count])] != letter):
                wrongStart = True
    if (wrongStart == True and len(answered) == len(subjects)):
        print("One or more of your answers start with the wrong character!")
        answered = []
        count = -1
    elif (len(answered) == len(subjects)):
        print("You won!")
        end = True
