from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
bot = ChatBot("JBOT")

conver = [
    'hi',
    'Hello',
    'What is your name?',
    'I am JBOT',
    'How are you?',
    'Im fine',
    'which language you talk?',
    'english'
]
trainer = ListTrainer(bot)
trainer.train(conver)

main = Tk()
main.geometry("500x650")
main.title("Chatbot")
img = PhotoImage(file="bot1.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF = Entry(main, font=("verdana", 20))
textF.pack(fill=X, pady=20)


def ask_bot():
    query = textF.get()
    answer_bot = bot.get_response(query)
    msg.insert(END, "you:" + query)
    msg.insert(END, "bot:" + str(answer_bot))
    textF.delete(0, END)
    msg.yview(END)


btn = Button(main, text="Enter", font=("verdana", 15), command=ask_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)

main.mainloop()


