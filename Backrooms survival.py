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

        # Base menu (always shown)
        print("[1] Check Inventory", end="")
        if len(self.actions) > 0:
            print(f"-------------------------------[4] {self.actions[0][0]}")
        else:
            print()

        print("[2] Check Status", end="")
        if len(self.actions) > 1:
            print(f"----------------------------------[5] {self.actions[1][0]}")
        else:
            print()

        print("[3] Check Enviroment", end="")
        if len(self.actions) > 2:
            print(f"------------------------------[6] {self.actions[2][0]}")
        else:
            print()

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
            
            #Game Over
            def Game_Over():
                print("L")

            def Status_Check():
                if self.Status[0] == 100:
                    self.Status[0] = 100
                
                if self.Status[1] == 100:
                    self.Status[1] = 100

                if self.Status[0] == 0:
                    Game_Over()

                if self.Status[1] == 0:
                    Game_Over()

            #Use item
            if item_choice.lower() == "almond water":
                menu.Status[1] += 20
                print("You drink the Almond Water. Sanity restored by 20!")
                Status_Check()
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

        #Determine if choice is in hardcoded actions
        if choice in base_actions:
            base_actions[choice]()
            finished = input("Finished? [x] ")
            if finished.lower() == "x":
                return
            else:
                print("Continuing...")
        #Handle the actions that are unique to the situation
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
    #Update environment
    menu.Enviroment = ["Level 0", "Empty Hallways as far as the eye can see"]
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Go forward", go_forward_L0_1_2),
        ("Go back", go_back_L0_1_2),
        ("Stand still", stand_still)
    ]

def go_right():
    print("You turn right. Yellow wallpaper expands infinitely.")
    time.sleep(2)
    print("As you walk you hear an annoying humming noise.")
    time.sleep(2)

    #Passive Sanity Drop
    menu.Status[1] -= 1

    if not menu.almond_water_taken:
        print("You notice a bottle of Almond Water on the floor")
        time.sleep(1)

        menu.Enviroment = [
            "Level 0",
            "The same hallways you are starting to get used to. There is a Bottle of Almond Water on the Ground"
        ]

        def pick_up_almond_water():
            print("You pick up the Almond Water.")
            menu.Inventory.append("Almond Water")
            menu.almond_water_taken = True

            #Remove pickup option
            menu.actions = [
                #Read as Action_Level_Branch_ActionNumber
                ("Go back", go_back_L0_2_2),
                ("Stand still", stand_still)
            ]

            menu.Enviroment[1] = (
                "The same hallways you are starting to get used to. "
                "The bottle of Almond Water is gone."
            )

        menu.actions = [
            #Read as Action_Level_Branch_ActionNumber
            ("Pick up almond water", pick_up_almond_water),
            ("Go back", go_back_L0_2_2),
            ("Stand still", stand_still)
        ]

    else:
        #Almond Water already taken
        menu.Enviroment = [
            "Level 0",
            "The same hallways you are starting to get used to. The floor is empty."
        ]

        menu.actions = [
            #Read as Action_Level_Branch_ActionNumber
            ("Go back", go_back_L0_2_2),
            ("Stand still", stand_still)
        ]


def stand_still():
    print("The choice is overwhelming. You stand paralyzed, unable to decide.")
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 5


########################################
#LEVEL 0 ACTION 2
########################################

def go_forward_L0_1_2():
    print("You contiune onwards")
    time.sleep(2)
    print("The halls stretch on")
    time.sleep(2)
    print("You come across a wall that is darker. It is glitching slightly")
    time.sleep(2)
    print("it feels as if you could walk through it")
    time.sleep(2)
    #Update environment
    menu.Enviroment = ["Level 0", "You see a darker Wall glitching slightly"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 1
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Go Through the Wall", level_1),
        ("Go back", go_back_L0_1_3),
        ("Stand still", stand_still)
    ]

def go_back_L0_1_2():
    print("You head back")
    #Update Enviroment
    menu.Enviroment = ["Level 0", "Endless hallways lined with yellow wallpaper"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 1
    #Update Actions
    menu.actions = [
        ("Go left", go_left),
        ("Go right", go_right),
        ("Stand still", stand_still)
    ]
def go_back_L0_2_2():
    print("You head back")
    #Update Enviroment
    menu.Enviroment = ["Level 0", "Endless hallways lined with yellow wallpaper"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 1
    #Udpate Actions
    menu.actions = [
        ("Go left", go_left),
        ("Go right", go_right),
        ("Stand still", stand_still)
    ]

########################################
#LEVEL 0 ACTION 2
########################################
def go_back_L0_1_3():
    print("You Retrace your steps")
    #Update environment
    menu.Enviroment = ["Level 0", "Empty Hallways as far as the eye can see"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 1
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Go forward", go_forward_L0_1_2),
        ("Go back", go_back_L0_1_2),
        ("Stand still", stand_still)
    ]

########################################
#LEVEL 1 Entrance
########################################

def level_1():
    print("You walk through the wall")
    time.sleep(2)
    print("-")
    time.sleep(2)
    print("-")
    time.sleep(2)
    print("-")
    time.sleep(2)
    print("The enviroment is different")
    time.sleep(2)
    print("Replacing the yellow wallpaper. Concrete walls surround you")
    time.sleep(2)
    print("The floor is damp, The lights flicker more and areas are shrouded in darkness")
    time.sleep(2)
    print("it looks like an empty carpark")
    time.sleep(2)
    print("-")
    time.sleep(2)
    print("A pit forms in your stomach")
    time.sleep(2)
    print("you feel this place is more dangerous")
    time.sleep(2)
    print("you should look for a weapon")
    time.sleep(2)
    #Update environment
    menu.Enviroment = ["Level 1", "An empty carpark. You feel uneasy"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 5
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Go left", go_left_L1_1_1),
        ("Go right", go_right_L1_2_1),
        ("Stand still", stand_still_L1)
    ]

########################################
#LEVEL 1 Action 1
########################################

def go_left_L1_1_1():
    print("You head left")
    time.sleep(2)
    print("In the Distance you hear a noise that doesn't sound human")
    time.sleep(2)
    #Update environment
    menu.Enviroment = ["Level 1", "An eerie Carpack. You heard an inhuman noise in the distance"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 4
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Head towards the noise", go_forward_L1_1_2),
        ("Get away from the noise", go_away_L1_2_2),
        ("Stand still", stand_still_L1)
    ]

def go_right_L1_2_1():
    print("You go right")
    time.sleep(2)
    print("You hear a distant noise")
    time.sleep(2)
    print("It's not nearby")
    time.sleep(2)
    #Update environment
    menu.Enviroment = ["Level 1", "An eerie carpack. You heard a noise in the distance. Whatever it was it was not nearby"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 2
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Contiune Onwards", go_forward_L0_1_2),
        ("Go back and find the source of the noise", go_back_L0_1_2),
        ("Stand still", stand_still_L1)
    ]

def stand_still_L1():
    print("You feel a looming danger nearby. You don't know what to do.")
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 5
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Go left", go_left_L1_1_1),
        ("Go right", go_right_L1_2_1),
        ("Stand still", stand_still_L1)
    ]
   
########################################
#LEVEL 1 Action 2
########################################

#Entiy encouter happens here
def go_forward_L1_1_2():
    print("You go right")
    print("You hear a distant noise")
    print("It's not nearby")
    #Update environment
    menu.Enviroment = ["Level 1", "An eerie carpack. You heard a noise in the distance. Whatever it was it was not nearby"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 2
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Contiune Onwards", go_forward_L0_1_2),
        ("Go back and find the source of the noise", go_back_L0_1_2),
        ("Stand still", stand_still_L1)
    ]

#go back to the go right branch. Will join the path in the next action
def go_away_L1_2_2():
    print("You go right")
    print("You hear a distant noise")
    print("It's not nearby")
    #Update environment
    menu.Enviroment = ["Level 1", "An eerie carpack. You heard a noise in the distance. Whatever it was it was not nearby"]
    #Update Saatus (Decreases Sanity)
    menu.Status[1] -= 2
    #Update actions
    menu.actions = [
        #Read as Action_Level_Branch_ActionNumber
        ("Contiune Onwards", go_forward_L0_1_2),
        ("Go back and find the source of the noise", go_back_L0_1_2),
        ("Stand still", stand_still_L1)
    ]

#Sets up the variables
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



#Item Tracker
menu.almond_water_taken = False

#Game Loop
while True:
    print(f"\nCurrent Location: {menu.Enviroment[0]}")
    print(f"{menu.Enviroment[1]}")
    choice = menu.action_menu()
    menu.handle_action(choice)
    time.sleep(1)

    if choice.lower() == "x":
        print("Exiting the game. Goodbye!")
        break
