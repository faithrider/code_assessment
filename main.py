from tkinter import *



'''
Section One: Functions/Main Code Action

'''

# Current numerical input gets put to the entry box
def user_click(input_number):
    current_value = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current_value) + str(input_number))

# When user clicks 'clear', it clears the current entry box
def user_click_clear():
    entry.delete(0, END)

# When user clicks a cell, it sends the current entry box to said cell
def user_click_grid(clicked_button):
    # If the user doesn't input anything, it auto sets to 0.
    if window.title() == "Stage One: Setting Grid Values":
        if entry.get() == '':
            clicked_button.configure(text = '0')
        else:
            clicked_button.configure(text = entry.get())
        entry.delete(0, END)
    else:
        interpolate(clicked_button)

# When clicked, switches to interpolation phase.
def switch_to_interpolation():
    # Changes window title.
    window.title("Stage Two: Grid Interpolation")

    # Deletes the entry box value, then the box itself.
    entry.delete(0, END)
    entry.grid_forget()

    # Deletes the numerical input/clear/mode switch buttons.
    button_0.grid_forget()

    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()

    button_4.grid_forget()
    button_5.grid_forget()
    button_6.grid_forget()

    button_7.grid_forget()
    button_8.grid_forget()
    button_9.grid_forget()

    button_clear.grid_forget()
    ready_to_interpolate.grid_forget()

    # Changes the purpose of the grid button to interpolate upon user click.
    instructions.configure(text="Press the cells you would like to interpolate.")

# Creates array of the current grid values.
def create_values_array():

    arr =   [[int(row0_col0['text']), int(row0_col1['text']), int(row0_col2['text']), int(row0_col3['text'])],
            [int(row1_col0['text']), int(row1_col1['text']), int(row1_col2['text']), int(row1_col3['text'])],
            [int(row2_col0['text']), int(row2_col1['text']), int(row2_col2['text']), int(row2_col3['text'])],
            [int(row3_col0['text']), int(row3_col1['text']), int(row3_col2['text']), int(row3_col3['text'])]]

    return arr



# Interpolates the selected cell value using its neighbors
def interpolate(clicked_button):
    row = clicked_button.grid_info()['row']
    col = clicked_button.grid_info()['column']
    
    # Creates a 4x4 array of the grid values
    array_of_values = create_values_array()
    
    num_neighbors = 0
    new_value = -1 * array_of_values[row][col]               #Accounts for the value itself being included in the sum
    for x_ in range(-1, 1):
        for y_ in range(-1,1):
            try:
                new_value += array_of_values[row+x_][col+y_] #Adds value to sum
                num_neighbors += 1
            except IndexError:
                new_value = new_value
    
    new_value //= num_neighbors

    clicked_button.configure(text = new_value)



# Section One -> END





'''
Section Two: Creating and placing the GUI.

'''

# Creates GUI window and title.
window = Tk()
window.title("Stage One: Setting Grid Values")


row0_col0 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row0_col0))
row0_col1 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row0_col1))
row0_col2 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row0_col2))
row0_col3 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row0_col3))

row1_col0 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row1_col0))
row1_col1 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row1_col1))
row1_col2 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row1_col2))
row1_col3 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row1_col3))

row2_col0 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row2_col0))
row2_col1 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row2_col1))
row2_col2 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row2_col2))
row2_col3 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row2_col3))

row3_col0 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row3_col0))
row3_col1 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row3_col1))
row3_col2 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row3_col2))
row3_col3 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click_grid(row3_col3))

instructions = Label(window, text = "Press the bottom buttons or type to enter a value, the press the corresponding table cell to change it! When you're ready to interpolate, press the \"Ready to Interpolate\" button.")


row0_col0.grid(row=0, column=0)
row0_col1.grid(row=0, column=1)
row0_col2.grid(row=0, column=2)
row0_col3.grid(row=0, column=3)

row1_col0.grid(row=1, column=0)
row1_col1.grid(row=1, column=1)
row1_col2.grid(row=1, column=2)
row1_col3.grid(row=1, column=3)

row2_col0.grid(row=2, column=0)
row2_col1.grid(row=2, column=1)
row2_col2.grid(row=2, column=2)
row2_col3.grid(row=2, column=3)

row3_col0.grid(row=3, column=0)
row3_col1.grid(row=3, column=1)
row3_col2.grid(row=3, column=2)
row3_col3.grid(row=3, column=3)

instructions.grid(row=4,column=0, columnspan=10)


# Creates the entry/showcase box.
entry = Entry(window, width=35, borderwidth=5)
entry.grid(row=5,column=0, columnspan=10, padx=10, pady=10)

# 0-9 Buttons for the user to input values, the clear button, and the button to change to interpolation mode.
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: user_click(0))

button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: user_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: user_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: user_click(3))

button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: user_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: user_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: user_click(6))

button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: user_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: user_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: user_click(9))

button_clear = Button(window, text="Clear Cell", padx=200, pady=20, command=user_click_clear)
ready_to_interpolate = Button(window, text="Ready to Interpolate", padx=170, pady=20, command=switch_to_interpolation)

# Puts input buttons to window.
button_0.grid(row=6, column=0)

button_1.grid(row=6, column=1)
button_2.grid(row=6, column=2)
button_3.grid(row=6, column=3)

button_4.grid(row=6, column=4)
button_5.grid(row=6, column=5)
button_6.grid(row=6, column=6)

button_7.grid(row=6, column=7)
button_8.grid(row=6, column=8)
button_9.grid(row=6, column=9)

button_clear.grid(row=7, column=0, columnspan=5)
ready_to_interpolate.grid(row=7, column=5, columnspan=5)



# Runs the GUI.
window.mainloop()



# Section Two -> END