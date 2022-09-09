from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(TIMER)
    canvas.itemconfig(counter, text="00:00")
    timer_label.config(text="TIMER")
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="BREAK", fg=RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="BREAK", fg= PINK)
    else:
        count_down(WORK_MIN*60)
        timer_label.config(text="WORK", fg= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(start):
    global TIMER
    count_min = start // 60
    count_sec = start % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if start > 0:
        canvas.itemconfig(counter, text=f"{count_min}:{count_sec}")
        TIMER = window.after(1000, count_down, start-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            checkmark = "☕" * (REPS//2)
            check.config(text=checkmark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Soujodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
counter = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer")
timer_label.grid(column=1, row=0)
timer_label.config(font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)

check = Label(text="")
check.grid(column=1, row=4)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=3, row=3)

window.mainloop()
