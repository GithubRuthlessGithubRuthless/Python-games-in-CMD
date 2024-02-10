import time
print("The most realistic bank robbery 2.0 (Not like GTA)")
time.sleep(2)
print("Loading - 12%")
time.sleep(2)
print("Loading - 20%")
time.sleep(2)
print("Loading - 36%")
time.sleep(1)
print("Loading - 63%")
time.sleep(2)
print("Loading - 85%")
time.sleep(1)
print("Successful loading!")
time.sleep(1)
firstaction = input("You are near the impregnable wall of the bank. 1.Use explosives to blow up a wall \n2.Make a dig under the bank and dig according to the building plan to the vault. Your actions: ")
if firstaction == "1":
    print("After the explosion you were noticed and detained. You received 4 years in prison. Restarting the game.")
    time.sleep(1)
if firstaction == "2":
    print("You have dug under the bank and are under the vault.")
secondaction = input("1.Dig into the storage, 2.Blow up the floor of the vault. Your action: ")
if secondaction == "1":
    print("You dug up and saw a hard iron floor and your shovel couldn’t break it.")
if secondaction == "2":
    print("You walked away and pressed the detonator button.\nAn explosion thundered and the guards heard it,\nyou had 2 minutes until they opened the massive, heavy, iron door. You ran towards the explosion")
thirdaction = input("1.Fill your bags with money and run away before the police arrive.\n2.Take all the gold bars and run away before the police arrive. Your action: ")
if thirdaction == "1":
    print("You quickly put everything you could carry into your bags and ran to the van.")
if thirdaction == "2":
    print("This is not GTA, so you couldn’t take away the gold bars because\nthey weigh too much and while you were walking through the tunnel like turtles,\nthe police already caught you. Wasted")
fourthaction = input("1. Drive the van to the shelter.\n2. Drive into the forest in a van and divide the amount there.")
if fourthaction == "1":
    print("You have been tracked. FBI, OPEN UP DOOR!!!")
if fourthaction == "2":
    print("You have divided everything successfully.")
pentaethism = input("1.Go to your home and buy a Tesla, a mega computer, donate to Dragon Lore in CS2,\nbuy a house of the future, buy out SpaceX,\nand announce that you are a multi-billionaire.\n2.Go to another country and live there. Buy a house there and live in peace without robbery.")
if pentaethism == "1":
    print("Your identity has been established! FBI, OPEN UP DOOR")
if pentaethism == "2":
    print("Mission Complete! (Gta SA music)")
time.sleep(2)
print("Thanks for playing, good luck and don't rob banks!")
exit()