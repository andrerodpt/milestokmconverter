from tkinter import *

#
# Entry (0,1)
# Label "Miles" (0, 2)
# Label "is equal to" (1, 0)
# Label result (1, 1)
# Label "Km" (1, 2)
# Button "Calculate" (2, 1)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


# Entry
entry = Entry(width=15)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

# Labels
label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(row=1, column=0)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

label_Km = Label(text="Km")
label_Km.grid(row=1, column=2)

#Buttons
def convert():
    converted_miles = round(float(entry.get()) * 1.609344, 2)
    label_result.config(text=converted_miles)

#calls action() when pressed
button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)



window.mainloop()