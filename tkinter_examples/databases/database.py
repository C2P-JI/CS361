#https://www.youtube.com/watch?v=YR3h2CY21-U&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=19
from tkinter import *
from PIL import ImageTk,Image
import sqlite3 #simple database usage
#sqlite3 only has five data types
#text, integer, real(decimal numbers), null(does it or does it not exist)
#and blob(image files, video files)

root = Tk()
root.title('database use example')
root.geometry("400x400")

#databases


#Create a database or connect ot one
conn = sqlite3.connect('address_book.db') #if the '.db' doesn't already exist this
                                            #command will make it in the current
                                            #directory
#create curser
c = conn.cursor()

#create table

c.execute("""CREATE TABLE addresses(
          first_name text,
          last_name text,
          address text,
          city text, 
          zipcode integer
        )""")

#commit changes
conn.commit()

#close connection
conn.close()



root.mainloop()