from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

#need to install numpy and matplotlib
#terminal commands
    #pip install numpy
    #pip install matplotlib

root = Tk()
root.title('plots')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(2000000, 25000, 5000)
    plt.pie(house_prices, 50) #50 bins
    plt.show() 

my_button = Button(root, command=graph, text="graph")
my_button.pack()


root.mainloop()