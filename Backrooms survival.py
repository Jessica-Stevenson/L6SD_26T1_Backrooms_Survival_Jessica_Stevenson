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
        #Lovely mess of an Inventory
        def use_inventory():
            #Checks if Inventory is empty
            real_items = [i for i in menu.Inventory if i != "-"]
            
            if not real_items:
                print("Your inventory is empty!")
                return

            #Display items
            print("Inventory:")
            for idx, item in enumerate(real_items, start=1):
                print(f"[{idx}] {item}")
            print("[0] Cancel")
            
            #Input
            choice = input("> ").strip()
            
            if choice == "0":
                print("Cancelled.")
                return
            
            try:
                index = int(choice) - 1
                item_choice = real_items[index]
            except (ValueError, IndexError):
                print("Invalid choice.")
                return
            
            if item_choice not in real_items:
                print(f"You don't have {item_choice} in your inventory!")
                return
        
            ########################################
            #Items
            ########################################
            
            #Use item
            if item_choice.lower() == "almond water":
                menu.Status[1] += 20
                print("You drink the Almond Water. Sanity restored by 20!")
                #Remove from inventory (replace with "-")
                for i in range(len(menu.Inventory)):
                    if menu.Inventory[i].lower() == "almond water":
                        menu.Inventory[i] = "-"
                        break
            else:
                print(f"You can't use {item_choice} right now.")

        #These handle the hardcoded actions
        base_actions = {
            "1": use_inventory,
            "2": lambda: print(f"Health: {self.Status[0]}, Sanity: {self.Status[1]}"),
            "3": lambda: print("Enviroment:", self.Enviroment),
        }

        # Determine if choice is in hardcoded actions
        if choice in base_actions:
            base_actions[choice]()
            finished = input("Finished? [x] ")
            if finished.lower() == "x":
                return
            else:
                print("Continuing...")
        # Handle the actions that are unique to the situation
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
        ("Go forward", go_forward_L0_1),
        ("Go back", go_back_L0_1),
        ("Stand still", stand_still)
    ]

def go_right():
    print("You turn right. Yellow wallpaper expands infinitely.")
    time.sleep(2)
    print("As you walk you hear an annoying humming nosie.")
    time.sleep(2)
    print("You notice a bottle of almond water on the floor")
    time.sleep(0.5)
    menu.Enviroment = ["Level 0", "The same Hallways you are starting to get used to. There is a Bottle of Almond Water on the Ground"]
    menu.Status[1] -= 1

    
    # Add a action to pick up Almond water
    def pick_up_almond_water():
        print("You pick up the Almond Water.")
        menu.Inventory.append("Almond Water")
        #removes almond water after you pick it ups
        menu.actions = [action for action in menu.actions if action[0] != "Pick up almond water"]
        menu.Enviroment[1] = "The same hallways you are starting to get used to. The bottle of Almond Water is gone."
    
    # Update available actions
    menu.actions = [
        ("Pick up almond water", pick_up_almond_water),
        ("Go back", go_back_L0_2),
        ("Stand still", stand_still)
    ]

def stand_still():
    print("The choice is overwhelming. You stand paralyzed, unable to decide.")
    menu.Status[1] -= 5


########################################
#LEVEL 0 ACTION 2
########################################

def go_forward_L0_1():
    print("You contiune onwards")

    
def go_back_L0_1():
    print("You head back")
    menu.Enviroment = ["Level 0", "Endless hallways lined with yellow wallpaper"]

def go_back_L0_2():
    print("You head back")
    menu.Enviroment = ["Level 0", "Endless hallways lined with yellow wallpaper"]




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
