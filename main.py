from tkinter import *
import math;


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None;
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer);
    canvas.itemconfig(timer_label, text=f"00:00")
    title_label.config(text="Timer");
    checkmark_label.config(text='');
    global reps;
    reps = 0;


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps;
    reps += 1
    work_sec = WORK_MIN * 60;
    short_break_sec = SHORT_BREAK_MIN * 60;
    long_break_sec = LONG_BREAK_MIN * 60;

    if reps % 8 == 0:
        count_down(long_break_sec);
        title_label.config(text="Long break", fg=RED)
    
    elif reps % 2 ==0:
        count_down(short_break_sec);
        title_label.config(text="Short break", fg=PINK)
    
    else:
        count_down(work_sec);
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60);
    count_seconds = count % 60;
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_label, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer;
        
        timer = window.after(1000, count_down, count -1);
    else:
        start_time();
        marks = "";
        for _ in range(math.floor(reps/2)):
            marks += "✓";
            checkmark_label.config(text=marks);

# ---------------------------- UI SETUP ------------------------------- #
window = Tk();
window.title("Pomodoro app");
window.config(padx=100, pady=50, bg=YELLOW);
canvas = Canvas(width=200, height=224, bg=YELLOW);
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112, image=tomato_img);
timer_label = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 50))
canvas.grid(column=1,row=1);


title_label= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,25, "bold"));
title_label.grid(column=1, row=0)


start_button = Button(text="Start", command=start_time);
start_button.grid(column=0, row=3);

reset_button = Button(text="Reset", command=reset_timer);
reset_button.grid(column=3, row=3);

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15));
checkmark_label.grid(column=1, row=3);

window.mainloop();