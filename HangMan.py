
# Import random function for getting random word
from random import randint

# Import the Tkinter library for graphics
from tkinter import *

class hangman():
    def __init__(self, window,words):
        
        # Set up the inital frame
        self.mainFrame = Frame(window,background='white')
        self.mainFrame.pack()
        self.wordss = words
        
        # Display "HANG MAN" on top
        self.main = Text(self.mainFrame,bd=-1,height=1,width=10, font=('verdana', 20, 'bold'))
        self.main.insert(END, "HANG MAN")
        self.main.pack(pady=(100,25))
        self.main.tag_add("here", "1.0", "1.4")
        self.main.tag_config('here',justify='center')
        
        # Display two buttons
        self.button1 = Button (self.mainFrame, text = "Start Game", bd=3, command = self.single).pack(pady=7)
        self.button3 = Button (self.mainFrame, text = "Quit", bd=3, command = window.destroy).pack(pady=7)
    
    # Start game in single player mode
    def single(self):
    
        # Destroy the previous frame
        self.word,length = self.get_word()
        self.mainFrame.destroy()
        
        # set up some variables 
        self.guess_count = 0
        self.tried = []
        self.dash = ['__']
        for i in range(length - 1):
            self.dash.append(' __')
        
        print(self.word)
        # set up the top frame containing dashes (word to be guessed)            
        self.top = Frame(window,background='white')
        self.top.pack()
        
        self.blank = Text(self.top,bd=-1,height=1,width=2*length,font=('verdana', 12, 'bold'))
        self.blank.insert(END, ''.join(self.dash))
        self.blank.pack(pady=(55,10))
        self.blank.tag_add("here", "1.0", "1.4")
        self.blank.tag_config('here',justify='center') 
        
        
        # set up the middle frame for graphics
        self.middle = Frame(window,background='white')
        self.middle.pack()
        
        self.stand = Canvas(self.middle,bd=0,width=500,height=230,background='#ffffff')
        self.stand.pack()
        self.stand.create_line(0,230,500,230)
        
        
        # set up the bottom frame containing info, entry and the try button
        self.bottom = Frame(window,background='white')
        self.bottom.pack()
        
        self.info = Text(self.bottom,bd=-1,height=1,width=49, font=('verdana', 12, 'bold'))
        self.info.insert(END, "Guess a letter below to see if it's in the word")
        self.info.pack(pady=(20,20))
        self.info.tag_add("here", "1.0", "1.4")
        self.info.tag_config('here',justify='center')
        
        # The entry where letters will be entered to guess
        self.E1 = Entry(self.bottom,bd=5,width=2,justify=CENTER)
        self.E1.pack()

        # try button
        self.trybutt = Button(self.bottom, text='Try', command=self.try_letter)
        self.trybutt.pack(pady=(10,0))
        
        
    def try_letter(self):
        # get the letter in entry
        guess = self.E1.get().strip().lower()
        
        # if no letter is entered then do nothing
        if guess == '':
            return
        
        # remove the letter from entry
        self.E1.delete(0, END)

        # Make sure only one letter is entered at a time
        if len(guess) > 1:        
            self.info.delete('1.0', END)
            self.info.insert(END, "Please enter only one letter at a time.")
            self.info.tag_add("here", "1.0", "1.4")
            self.info.tag_config('here',justify='center')
        
        # Make sure letter has not been used before    
        elif guess in self.tried:
            self.info.delete('1.0', END)
            self.info.insert(END, "You've already tried the letter ' " + guess.upper() + " '")
            self.info.tag_add("here", "1.0", "1.4")
            self.info.tag_config('here',justify='center')
            
        # if letter is in word then revel letters    
        elif guess in self.word:
            index = 0
            while True:
                index = self.word.find(guess,index)
                if index == -1:
                    break
                self.dash[index] = guess.upper()
                index = index + 1
                      
            self.blank.delete('1.0', END)
            self.blank.insert(END, ''.join(self.dash))
            self.blank.tag_add("here", "1.0", "1.4")
            self.blank.tag_config('here',justify='center')
            
        # if letter is not in word then damage    
        elif guess not in self.word:
            self.info.delete('1.0', END)
            self.info.insert(END, "The guessed letter ' " + guess.upper() + " ' is not in word, try again.")
            self.info.tag_add("here", "1.0", "1.4")
            self.info.tag_config('here',justify='center')
            
            self.guess_count = self.guess_count + 1
            
            # draw stand if first wrong guess
            if self.guess_count == 1:
                self.stand.create_line(350,50,350,230)
                self.stand.create_line(250,50,350,50)
                self.stand.create_line(250,50,250,80)
            
            # draw face if second wrong guess
            elif self.guess_count == 2:
                self.stand.create_oval(232, 80, 267, 115,width=2)
            
            # draw one hand if third wrong guess
            elif self.guess_count == 3:
                self.stand.create_line(250,115,220,155,width=2)
            
            # draw second hand if fourth wrong guess
            elif self.guess_count == 4:
                self.stand.create_line(250,115,280,155,width=2)
            
            # draw body if fifth wrong guess
            elif self.guess_count == 5:
                self.stand.create_line(250,115,250,165,width=2)
            
            # draw one leg if sixth wrong guess
            elif self.guess_count == 6:
                self.stand.create_line(250,164,220,204,width=2)
            
            # draw second leg and display game over and buttons if seventh wrong guess
            elif self.guess_count == 7:
                self.stand.create_line(250,164,280,204,width=2)
                
                self.stand.create_text(250, 95, text="X X")
                #canvas.itemconfig(canvas_id, text="this is the text")
                             
                self.info.delete('1.0', END)
                self.info.insert(END, "GAME OVER !")
                self.info.tag_add("here", "1.0", "1.9")
                self.info.tag_config('here',justify='center',foreground='red')
            
                self.E1.destroy()
                self.trybutt.destroy()

                Button(self.bottom, text='Play Again',bd=2, command = self.again).pack(side='left',padx=(10,0),pady=(10,0))            
                Button(self.bottom, text='Quit',bd=2, command = window.destroy).pack(side='left',padx=(335,0),pady=(10,0))
        
        # if the whole word is guessed correctly display you win and show buttons for playing again or exit
        if ' __' not in self.dash and '__' not in self.dash:
            self.info.delete('1.0', END)
            self.info.insert(END, "YOU WON !")
            self.info.tag_add("here", "1.0", "1.9")
            self.info.tag_config('here',justify='center',foreground='green')
            
            self.stand.destroy()
            
            self.cong = Text(self.middle,bd=-1,height=1,width=16, font=('verdana', 20, 'bold'))
            self.cong.insert(END, "CONGRATULATIONS")
            self.cong.pack(pady=(100,25))
            self.cong.tag_add("here", "1.0", "2.9")
            self.cong.tag_config('here',justify='center',foreground='green')
            
            self.E1.destroy()
            self.trybutt.destroy()

            Button(self.bottom, text='Play Again',bd=2, command = self.again).pack(side='left',padx=(10,0),pady=(100,0))            
            Button(self.bottom, text='Quit',bd=2, command = window.destroy).pack(side='left',padx=(335,0),pady=(100,0))

        self.tried.append(guess)
    
    # Destroy all previous stuff for playing again
    def again(self):
        self.top.destroy()
        self.middle.destroy()
        self.bottom.destroy()        
        self.single()
        
    # Chooses a word randomly from the list of words extracted from the input file
    def get_word(self):
        chosen_word = self.wordss[randint(0, len(self.wordss)-1)]
        word_length = len(chosen_word)
        return chosen_word,word_length

# Extract whole list of words from the input file
def populate_wordlist():
    words = []
    try:
        with open('wordlist.txt','r') as fwrdlis:
            data = fwrdlis.read()
            words = data.split('\n')
        return words
    except:
        print ("\n[!] Error: 'wordlist.txt' file not present.\n")
        return False 

# Create a white window
window = Tk()
window.configure(background='white')
window.geometry('500x460')

# Give the window a title
window.title('Hang Man')

hangman(window,populate_wordlist())

# Start the event loop to react to user inputs
window.mainloop()

#------------------------------------------------------------------#
