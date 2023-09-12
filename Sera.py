import random

mainlist = [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" ,"W" , "X" , "Y" , "Z" , "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

def main():
  for main in range(times):
    todo = ""
    for generate in range(length):
      randomch = random.choices(mainlist)
      todo += str(randomch)
    print(todo)

print("SERA !!! \n")
print("Hello Sir In Sera , We Here To Create The Serial Numbers You Want ◉⁠‿⁠◉ .")

length = int(input("Enter length of the serial numbers you need : "))

times = int(input("Enter number of the serial numbers you need : "))

main()