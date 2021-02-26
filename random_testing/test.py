##While loop

i = 1
while i <= 10:
    print(i)
    i +=1
print("we done")


#true/false calc
i = int(input("Give me a number yo"))

if i % 2 == 0:
    print("this is even")
else:
    print("that do be odd doe")



#guess game with limit of 3 

secret = "secret"
guess = ""
count = 0

while guess != secret:
    guess = input("Gimme a guess: ")
    count += 1
    if count >= 3:
        print("You Lose!")

print("you ween!")


#exponent calc without **
def exp(num1, num2):
    result = 1
    for num in range(num2):
        result = result * num1
    return result

print(exp(232, 500))


#nested lists
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

user_num = int(input("What number are you looking for: "))
notfound = True
for row in grid:
    for col in row:
        if col == user_num:
            print("this is what you need:" + str(col))
            notfound = False
            break
if notfound:
    print("tough luck")




#translate



def translate(phrase):
    translation = "b"
    for letter in phrase:
        if letter in "g":
            translation = translation + "b"
        else:
            translation = translation + letter
    return translation

translate(input("What do you want to translate: "))

#error catching

#attempt following action
try:
    num = int(input("give a number yo: "))
    print(num)
    #this will fail
    value = 10/0

#if this throws an error return this instead of an error code, and continue running program
#this will currently be returned if any type of error is found during try clause
except: #(ZeroDivisionError - this will limit to zerodivisionerror #
    print("cant divide by zero yo")
#this will print the actual error instead, and continue program
except ValueError as err:
    print(err)



#external file reading
file = open('FinalTemplate.txt', 'r')
for line in file.readlines():
    print(line)
file.close()

for 
#or 
with open('TestTemplate.txt', 'r') as file:
    #some actions with the file
    print(file.readlines())
    file.close()

#reading a file in remote dir:
with open("YAML\\" + "newfile.txt", 'r') as file:
    print(file.readlines()) #DONT FORGET () TO ACTUALLY CALL FUNCTION
    file.close()

file = open("YAML\\" + "newfile.txt", 'r+') #a = append to the end of the file
file.write("\nthis is a new line")
print(file.readlines())
file.close()

#W will overwrite not add/replace to file by default, r+ seems to append


#class = the datatype of whatever youre defining, object is the actual object 
#defined by the class params
class new:

    def__init__(self, name, size, age, is_dead):
        self.name = name 
        self.size = size
        self.age = age
        self.is_dead = is_dead 



#multiple choice quiz
from defclass import Question
question_prompts = [
    "what is 2 * 5: \n(a) 12 \n(b) 54 \n(c) 10\n\n",
    "what is 12 - 5: \n(a) 10 \n(b) 7 \n(c) 14\n\n",
    "what is 13 * 3: \n(a) 39 \n(b) 524 \n(c) 154\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

