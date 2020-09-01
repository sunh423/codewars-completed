#https://www.codewars.com/kata/586a933fc66d187b6e00031a/train/python
import random

def generateName():
    name_generated = ""
    char_s = ["A", "B", "C", "D", "E", "F", "G","H","I","J","K","L","M","N","O","P","Q","R","S",
                         "T","U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g","h","i","j","k","l",
                         "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while True:
        name_generated = random.choice(char_s) + random.choice(char_s) + random.choice(char_s) + random.choice(char_s) + random.choice(char_s) + random.choice(char_s)
        if not photoManager.nameExists(name_generated):
            return name_generated
