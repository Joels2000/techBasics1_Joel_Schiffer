import time
import webbrowser

# I wanted to include music, but had trouble with it  at first. I tried to find a way to play
# an MP3 file, but it didn't work, so I found the solution to use webbrowser.open
# instead and it actually works very nice.
print("Opening the game soundtrack...")
webbrowser.open("https://www.youtube.com/watch?v=7lKasOVQqpY&list=PLZNLZTgNre8OXpI5D_w3kI5tPdG_SNhie")
time.sleep(2)

print("--- WELCOME TO THE DEEP SEA RESCUE ---")
time.sleep(1)

# REQUIREMENT: User Input 1
start_choice = input("You are in a submarine. Do you DIVE deeper or SURFACE? ")

# REQUIREMENT: Branching point
if start_choice == "dive" or start_choice == "DIVE":
    print("\nYou descend into the dark water...")
    time.sleep(2)

    # REQUIREMENT: User Input 2 (Number in a range)
    oxygen_level = 0
    # PROBLEM I HAD: At first, my loop didn't work because I forgot to
    # update the oxygen_level variable inside the loop, so it went forever.
    # I fixed it by making sure 'val' is converted to an int every time.
    while oxygen_level < 1 or oxygen_level > 100:
        val = input("Set oxygen flow level (1 to 100): ")

        # I realized I had to use int() here or the > and < math wouldn't work
        oxygen_level = int(val)

        # REQUIREMENT: Verify if input is within range
        if oxygen_level < 1 or oxygen_level > 100:
            print("Error! That is not a safe level. Please try again.")

    # REQUIREMENT: Nested Conditional
    if oxygen_level > 50:
        print("\nThe submarine is powered up and ready!")
        time.sleep(1)

        # REQUIREMENT: User Input 3
        action = input("You see a giant squid! Do you TAME it or FIGHT it? ")

        # I had a bug here where the game would end no matter what I typed.
        # I realized I needed to nest this IF inside the oxygen check.
        if action == "tame":
            print("The squid is friendly! It guides you to a treasure. YOU WIN!")
        else:
            print("The squid was too strong. Your sub was crushed. Game Over.")

    else:
        print("\nOxygen is too low. You had to return to the surface. Failed mission.")

# Part of the branching point
elif start_choice == "surface":
    print("\nYou went back up, but a storm hit the submarine!")
    time.sleep(2)

    rescue = input("Do you call for HELP or try to SWIM? ")

    # I debated making a 3rd choice here but kept it simple to avoid errors
    if rescue == "help":
        print("A helicopter saw your flare! You are safe. YOU WIN!")
    else:
        print("The waves were too big. Game Over.")

# REQUIREMENT: 5th Conditional
# I added this because I noticed the game just closed if I had a typo.
# This catches any weird inputs at the very start.
else:
    print("You didn't type a valid direction, so you just floated away.")

print("\n--- End of Game ---")
