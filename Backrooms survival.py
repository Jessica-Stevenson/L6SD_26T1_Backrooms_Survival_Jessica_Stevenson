import time


class action:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(self.make + " engine has started")
    
    def __del__(self):
        print(f"The car {self.year} {self.make} {self.model} has been deleted.")

def action_menu():

    return

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
    time.sleep(1)
    print("-")
    time.sleep(1)
    print("-")
    time.sleep(1)
    print("-")
    time.sleep(1)
else:
    quit() 

print("----------------------------------")
print("---------------ACT I--------------")
print("----------------------------------")
time.sleep(1)

print("you were falling. Falling from what? you don't know.")
time.sleep(5)
print("It doesn't matter though. The result is the same.")
time.sleep(5)
print("Endless Hallways expanding Infinitely, yellow wallpaper lines the walls and an annoying buzz sound that you are sure will get on your nerves.") 
time.sleep(5)
print("The perfect enviroment to go insane in.")
time.sleep(5)
print("There is not much you can do other then explore")
time.sleep(2)
print("Go left or right")


