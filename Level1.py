import random

with open("notes.txt","a") as f:
    f.write(random.choice(["fun","cool","wow"])+"\n")