import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import csv




def create_label(root, text, row, column, column_span=1, row_span=1, font_size = 10, put = "NSEW"):
    label = ttk.Label(root, text=text, font=("default", font_size))
    label.grid(row=row, column=column, columnspan=column_span, rowspan=row_span, sticky = put)
    return label

def create_entry(root, width, row, column):
    entry = ttk.Entry(root, width=width)
    entry.grid(row=row, column=column, padx=5)
    return entry

def create_button(root, text, command, row, column, row_span = 1, column_span = 1, padx = 0):
    button = ttk.Button(root, text=text, command=command)
    button.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, ipadx=padx)
    return button

def create_option_menu(root, options, row, column):
    clicked = tk.StringVar()
    clicked.set(options[0])
    drop = ttk.OptionMenu(root, clicked, *options)
    drop.grid(row=row, column=column)
    return clicked

def create_date_entry(root, row, column):
    calendar = DateEntry(root, selectmode='day')
    calendar.grid(row=row, column=column, padx=5)
    return calendar


