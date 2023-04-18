from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0) # highlight-thickness ==> border
loge_png = PhotoImage(file="C:/Users/kkes-/OneDrive/Masaüstü/githubprojects/python-workspace/intermediate-level-python exercises/password-manager-start/logo.png")
canvas.create_image(100, 100, image=loge_png)
canvas.pack()

window.mainloop()
