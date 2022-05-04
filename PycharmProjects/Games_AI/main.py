from Dinosaur_Game_AI import main_Dinosaur_AI
from FlappyBird import main_Flappy_AI
from tkinter import *

if __name__ == '__main__':
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Games implemented by NEAT - Artificial Intelligence")

    # set the configuration of GUI window
    gui.geometry("270x500")

    button1 = Button(gui, text=' Dinosaur Game ', fg='black', bg='red',
                     command=lambda: main_Dinosaur_AI.start_main(), height=1, width=8)

    button2 = Button(gui, text=' Flappy Bird Game ', fg='black', bg='red',
                     command=lambda: main_Flappy_AI.start_main(), height=1, width=8)

    button1.grid(columnspan=4, ipadx=70, row=4)
    button2.grid(columnspan=4, ipadx=70)

    gui.mainloop()
