import random
from datetime import datetime

print("Welcome to Story logger game")
print("Commands: /create | /quit | /read | /filter")

templates = [
    "Once {name} went to {place} and {adjective}ly {action}",
    "In {place}, {name} {action} with a {adjective} {twist}",
    "{name} {action} in {place}, feeling {adjective}"
]
while True:
    command = input("What is your command: ").lower().strip()
    if command == "/quit":
        print("See you next tale")
        break
    elif command == "/create":
        name = input("Enter a name: ").strip()
        place = input("Enter a place: ").strip()
        action = input("Enter an action: ").strip()
        adjectives = ["silly","crazy","wild","brave","joyfull"]
        print(adjectives)
        template = random.choice(templates)
        story = template.format(
            name = name,
            place = place,
            action = action,
            adjective = random.choice(adjectives)
        )
        print("Your story is: ")
        print(story)
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with open("stories.txt","a") as f:
            f.write(f"[{timestamp}] {story} \n")
        print("Story saved")
    elif command == "/read":
        try:
            with open("stories.txt","r") as f:
                stories = f.read()
            if stories:
                print("\n Past stories")
                print(stories)
            else:
                print("No stories yet")
        except FileNotFoundError:
            print("No stories file created yet")
    elif command.startswith("/filter"):
        keyword = command[8:].strip()
        if not keyword:
            print("Please provide a keyword")
        else:
            try:
                with open("stories.txt","r") as f:
                    lines = f.readlines()
                print("\n Matching stories: ")
                found = False
                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True
                if not found:
                    print("No stories match that keyword")
            except FileNotFoundError:
                print("No story file yet")
    else:
        print("Invalid command. Please enter a valid command.")