import random

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#The key is randomly generated on each iteration of the program
key = ''.join(random.sample(alpha,len(alpha)))

#Function to print the menu
def menu():
    choice = input('''SECRET DECODER MENU
    0) Quit
    1) Encode
    2) Decode
    3) Generate key\n''')
    return choice

#Function to encode
def encode(plain):
    coded = ""
    for i in range(len(plain)):
        if plain[i] in alpha:
            coded += key[alpha.index(plain[i])]
        else:
            coded += plain[i]
    return coded

#Function to decode
def decode(coded):
    plain = ""
    for i in range(len(coded)):
        if coded[i] in alpha:
            plain += alpha[key.index(coded[i])]
        else:
            plain += coded[i]
    return plain

#Function to generate new key
def generate_key(alpha):
    return ''.join(random.sample(alpha,len(alpha)))

#main function
def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = (input("Text to be encoded: ")).upper()
      print (encode(plain))
    elif response == "2":
      coded = (input("Code to be decyphered: ")).upper()
      print (decode(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    elif response == "3":
        global key
        key = generate_key(alpha)
        print("Your new key is ")
        for i in range(len(alpha)):
            print(alpha[i] + " : " + key[i])
    else:
      print ("Please enter a valid input!")



if __name__ == '__main__':
    main()
