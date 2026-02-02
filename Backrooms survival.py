#Adds time to space out text for readability
import time

#Character Class
#Contains User's Inventory, Health and Current location
class character:
    def __init__(self, Inventory, Status, Enviroment):
        self.Inventory = Inventory
        self.Status = Status
        self.Enviroment = Enviroment

#Action Class
#Contains placeholders for actions the user may take
class action(character):
    def __init__(self, Inventory, Status, Enviroment, actions):
        super().__init__(Inventory, Status, Enviroment)
        self.actions = actions

    #The action menu
    #There are two indexs by the actions as one is for the description and one is for the action itself
    def action_menu(self):
        print("\nWhat would you like to do?")
        print(f"[1] Check Inventory-------------------------------[4] {self.actions[0][0]}")
        print(f"[2] Check Status----------------------------------[5] {self.actions[1][0]}")
        print(f"[3] Check Enviroment------------------------------[6] {self.actions[2][0]}")
        print("[x] To Exit the Game")
        return input("> ")

    #This handles all the actions
    def handle_action(self, choice):
        #these handle the hardcoded actions
        base_actions = {
            "1": lambda: print("Inventory:", self.Inventory),
            "2": lambda: print(f"Health: {self.Status[0]}, Sanity: {self.Status[1]}"),
            "3": lambda: print("Enviroment:", self.Enviroment),
        }

        #this detrimes if the input is in the hardcoded actions
        if choice in base_actions:
            base_actions[choice]()
            finished = print("Finished? [x]")
            if finished == "x":
                return
            else:
                print("invalid input")
        #these handle the actions that are unique to the situation
        try:
            index = int(choice) - 4
            label, func = self.actions[index]
            func()
        except (ValueError, IndexError):
            print("Invalid choice.")

#Menu Screen of sorts
print("-")
print("If you're not careful and you noclip out of reality in the wrong areas, you'll end up in the Backrooms, where it's nothing but the stink of old moist carpet, the madness of mono-yellow, the endless background noise of fluorescent lights at maximum hum-buzz, and approximately six hundred million square miles of randomly segmented empty rooms to be trapped in.")

time.sleep(1)
print("-")
time.sleep(1)

print("God save you if you hear something wandering around nearby, because it sure as hell has heard you…")
print("-")
time.sleep(1)

#asking if you'd like to contiune.
#Confirmation is only here so the user has a chance to read the intro
print("Contiune [y/n]")
contiune = input()
if contiune == "y":
    print("----------------------------------")
    print("---------------ACT I--------------")
    print("----------------------------------")
    time.sleep(2)
else:
    quit() 

time.sleep(1)

#Le story
print("You were falling. Falling from what? you don't know.")
time.sleep(3)
print("It doesn't matter though. The result is the same.")
time.sleep(3)
print("Endless Hallways expanding Infinitely, yellow wallpaper lines the walls and an annoying buzz sound that you are sure will get on your nerves.") 
time.sleep(5)
print("The perfect enviroment to go insane in.")
time.sleep(3)
print("There is not much you can do other then explore")
time.sleep(1)

########################################
#LEVEL 0 ACTION 1
########################################
def go_left():
    print("You turn left. It's a labyrinth of hallways and walls.")
    # Update environment
    menu.Enviroment = ["Level 0", "Empty Hallways Lined with Yellow Wallpaper"]
    # Update actions
    menu.actions = [
        ("Go forward", go_forward_1),
        ("Go back", go_back_1),
        ("Stand still", stand_still)
    ]

def go_right():
    print("You turn right. Yellow wallpaper expands infinitely.")
    menu.Enviroment = ["Level 0", "As you walk you hear an annoying humming nosie. You notice a bottle of almond water on the floor."]
    menu.Status[1] = menu.Status - 1

    
    # Add a action to pick up Almond water
    def pick_up_almond_water():
        print("You pick up the Almond Water.")
        menu.Inventory.append("Almond Water")
    
    # Update available actions
    menu.actions = [
        ("Pick up almond water", pick_up_almond_water),
        ("Go back", go_back_2),
        ("Stand still", stand_still)
    ]

def stand_still():
    print("The choice is overwhelming. You stand paralyzed, unable to decide.")
    menu.Status[1] = menu.Status - 5

########################################
#LEVEL 0 ACTION 2
########################################

#sets up the variables
menu = action(
    Inventory=["-", "-", "-", "-", "-", "-"],
    Status=[100, 100],
    Enviroment=["Level 0", "Endless hallways lined with yellow wallpaper"],
    actions=[
        ("Go left", go_left),
        ("Go right", go_right),
        ("Stand still", stand_still)
    ]
)

#game loop
while True:
    print(f"\nCurrent Location: {menu.Enviroment[0]}")
    print(f"{menu.Enviroment[1]}")
    choice = menu.action_menu()
    menu.handle_action(choice)
    time.sleep(1)

    if choice.lower() == "x":
        print("Exiting the game. Goodbye!")
        break
