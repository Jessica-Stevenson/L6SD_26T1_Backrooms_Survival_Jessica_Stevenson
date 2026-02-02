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
    def __init__(self, Inventory, Status, Enviroment, action1, action2, action3):
        super().__init__(Inventory, Status, Enviroment)
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3

    def action_menu(self):
        print("\nWhat would you like to do?")
        print(f"[1] Check Inventory-------------------------------[4] {self.action1}")
        print(f"[2] Check Status----------------------------------[5] {self.action2}")
        print(f"[3] Check Enviroment------------------------------[6] {self.action3}")
        return input("> ")

    def handle_action(self, choice):
        actions = {
            "1": lambda: print("Inventory:", self.Inventory),
            "2": lambda: print("Status:", self.Status),
            "3": lambda: print("Environment:", self.Enviroment),
            "4": lambda: print("You chose to", self.action1),
            "5": lambda: print("You chose to", self.action2),
            "6": lambda: print("You chose to", self.action3),
        }

        action = actions.get(choice)
        if action:
            action()
        else:
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

#setting uo the first variables
Level_0_action_1 = action(
    Inventory=["-", "-", "-", "-", "-", "-"],
    Status=["Healthy", "Sane"],
    Enviroment=["Level 0", "Endless hallways lined with yellow wallpaper"],
    action1="Go left",
    action2="Go right",
    action3="Stand still"
)

choice = Level_0_action_1.action_menu()
