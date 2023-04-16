from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    check_marks.config(text="")
    label_timer_text.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps in {1, 3, 5, 7}:
        count_down(work_sec)
        label_timer_text.config(text="Work", fg=GREEN)
    if reps ==8 :
        count_down(long_break_sec)
        label_timer_text.config(text="Break", fg=RED)
    if reps in {2, 4, 6}:    
        count_down(short_break_sec)
        label_timer_text.config(text="Break", fg=PINK)

    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    timer_min = math.floor(count / 60)
    timer_sec = count % 60

    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"
    
    if timer_min < 10:
        timer_min = f"0{timer_min}"

    canvas.itemconfig(timer_text, text= f"{timer_min}:{timer_sec}")
    if count > 0 : 
        global timer
        timer = window.after(1000, count_down, count-1 )
    else: 
        start_timer()
        if reps % 2 == 0:
            new_text = check_marks["text"] + "✓"
            check_marks.config(text= new_text)

        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro GUI App")
window.config(padx=100, pady=50, bg=YELLOW)


label_timer_text = Label(text="Timer", font=(FONT_NAME, 35,"bold"), fg=GREEN, bg=YELLOW)
label_timer_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #highlightthickness ==> border
tomato_img = PhotoImage(file="pomodoro-gui-app/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(foreground=GREEN, background=YELLOW, font=(FONT_NAME, 20,"bold"))
check_marks.grid(row=3, column=1)

window.mainloop()