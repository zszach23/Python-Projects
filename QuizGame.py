# Quiz Game - Computer Quiz
# Zach Sally

score = 0

# Start
print("Welcome to Computer Quiz!")

playing = input("Do You Want to Play? ")

if playing.lower() != "yes":
    quit()

print("Time to Play!")

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


#Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# End game display score
print("You finished the Quiz!")
print("You got " + str(score) + "/4 questions correct!")
print("You got a " + str((score / 4) * 100) + "%.")
if (score >= 3):
    print("You passed!")
else:
    print("You didn't pass :(")