import random

#List of Knock knock jokes
names_list = ["P", "Paine", "Pat", "Luke", "Paul", "Poker", "Canoe", "Harry", "Lettuce", "Noah"]
knock_jokes = {'Canoe': 'Canoe help me with my homework?', 'Lettuce': 'Lettuce in it’s cold out here!', 'Noah': 'Noah good place we can get something to eat?', 'Harry': 'Harry up, it’s cold out here!', 'P': 'P Nuts are an elephants favorite treat!', 'Paine': 'Paine in the neck!', 'Pat': 'Pat yourself on the back!', 'Luke': 'Luke through the keyhole and you\'ll find out!', 'Paul': 'Paul hard, the door\'s stuck', 'Poker': 'Poker and see if she\'s awake'}

def main():
    print("Hi, what's your name?")
    name = input().strip()

    print("Here's a joke, %s!" %name)
    print("Knock knock")
    input()

    num = random.randint(0, len(names_list)-1)
    print(names_list[num])
    input()
    print(knock_jokes[names_list[num]])


if __name__ == '__main__':
    main()