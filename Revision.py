import random

add = random.choice(["happy","sad","angry","dissapointed"])
with open("Quiz.txt","a") as f:
    f.write(f"\n{add}")