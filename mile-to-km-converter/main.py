from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.config(height=120, width=120, padx=30, pady=30)

def button_clicked():
    new_text = int(int(entry.get())*1.6)
    result_label.config(text=str(new_text))

#Entry
entry = Entry(width=20)
print(entry.get())
entry.grid(row=0, column=1)

#Label
miles_label = Label(text="Miles", font=("Arial", 10, "italic"))
miles_label.grid(row=0, column=2)

equal_text = Label(text="is equal to", font=("Arial", 10, "italic"))
equal_text.grid(row=1, column=0)

result_label = Label(text="-", font=("Arial", 10, "italic"))
result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 10, "italic"))
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()