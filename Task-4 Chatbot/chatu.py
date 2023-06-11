import os
import random
import tkinter as tk
import warnings
from tkinter import *
from tkinter import filedialog

import nltk
from newspaper import Article
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# import  string
FORMAT = "utf-8"

warnings.filterwarnings('ignore')
text_contents = dict()
nltk.download('punkt', quiet=TRUE)
arc = Article('https://docs.python.org/3/tutorial/datastructures.html')
arc.download()
arc.parse()
arc.nlp()
corpus = arc.text

# tokenization
text = corpus
sentencelist = nltk.sent_tokenize(text)  # list of sentences


def greet_res(text):
    text = text.lower()
    bot_greet = ['hi', 'hello', 'hola', 'hey', 'howdy']
    usr_greet = ['hi', 'hey', 'hello', 'hola', 'greetings', 'wassup', 'whats up']
    for word in text.split():
        if word in usr_greet:
            return random.choice(bot_greet)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


# bot response
def bot_ress(usr_input):
    usr_input = usr_input.lower()
    sentencelist.append(usr_input)
    bot_res = ''
    cm = CountVectorizer().fit_transform(sentencelist)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_res = bot_res + ' ' + sentencelist[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break
    if response_flag == 0:
        bot_res = bot_res + ' ' + 'I am Sorry, I Don\'t Understand.'

    sentencelist.remove(usr_input)
    return bot_res


def widget_get():
    text_widget = root.nametowidget(textcon)
    return text_widget.get('1.0', 'end-1c')


def saveas(event=None):
    global file_path, filename
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    try:
        filename = os.path.basename(file_path)
        root.title(f"Chat Bot - {filename}")
        content = widget_get()
        with open(file_path, "w") as file:
            file.write(content)
            text_contents[str(textcon)] = hash(content)
            print("Operation successful")
    except FileNotFoundError:
        print("Operation not successful")
        return None


file_path = None


def save(event=None):
    global file_path, filename
    try:
        if file_path is None:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        filename = os.path.basename(file_path)
        root.title(f"Chat Bot - {filename}")
        content = widget_get()
        with open(file_path, "w") as file:
            file.write(content)
            text_contents[str(textcon)] = hash(content)
            print("Operation Successful")
    except FileNotFoundError:
        print("Operation not Successful")
        return None


def new(event=None):
    textcon.delete('2.0', 'end-1c')
    global file_path, filename
    file_path = None
    content = widget_get()
    text_contents[str(textcon)] = hash(content)
    filename = None


"""def check_changes(event=None):
    global filename
    current=widget_get()
    content=current.get()
    name =filename
    if hash(current)!=text_contents[str(textcon)]:
        if name[-1]!="*":
            filename=name+"*"

    elif name[-1]=="*":
        filename=name
    root.title(f"Chat Bot - {filename}")
"""


def clear(event=None):
    textcon.delete('2.0', 'end-1c')
    content = widget_get()
    text_contents[str(textcon)] = hash(content)


def fopen(event=None):
    global file_path, filename
    file_path = filedialog.askopenfilename(defaultextension=".txt")
    try:
        filename = os.path.basename(file_path)
        root.title(f"Chat Bot - {filename}")
        text_widget = root.nametowidget(textcon)
        with open(file_path, "r") as file:
            content = file.read()
            textcon.delete('1.0', 'end-1c')
            text_contents[str(textcon)] = hash(content)
            text_widget.insert(END, content)
            print("Operation successful")
    except FileNotFoundError:
        print("Operation not successful")
        return None


exit_list = ['exit', 'break', 'quit', 'See You Later', 'Chat With You Later', 'End the Chat', 'ye', 'ok Bye']


def send(event=None):
    usr_input = message.get()
    usr_input = usr_input.lower()
    textcon.insert(END, f'Nilay: {usr_input}' + '\n', 'usr')
    if usr_input in exit_list:
        textcon.config(fg='yellow')
        textcon.insert(END, "Bot:Ok Bye! Chat With U Later\n")
        return root.destroy()
    else:
        textcon.config(fg='yellow')
        if greet_res(usr_input) is not None:
            lab = f"Chatu: {greet_res(usr_input)}" + '\n'
            textcon.insert(END, lab)
        else:
            lab = f"Chatu: {bot_ress(usr_input)}" + '\n'
            textcon.insert(END, lab)


root = tk.Tk()
filename = "chat.txt"
root.title(f"Nilay's Chat Bot")
root.geometry('900x400')

root.resizable(False, False)
main_menu = Menu(root)
file_menu = Menu(root)
file_menu.add_command(label='Open  <Ctrl+O>', command=fopen)
file_menu.add_command(label='New  <Ctrl+N>', command=new)
file_menu.add_command(label='Save  <Ctrl+S>', command=save)
file_menu.add_command(label='Save as <Ctrl+Shift+S>', command=saveas)
edit_menu = Menu(root)
edit_menu.add_command(label='Clear  <Delete>', command=clear)
edit_menu.add_command(label='Preferences')
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_command(label="Quit", command=root.destroy)
root.config(menu=main_menu)
message = tk.StringVar()
chat_win = Frame(root, bd=1, bg='black', width=50, height=8)
chat_win.place(x=20, y=6, height=300, width=860)
textcon = tk.Text(chat_win, font=("Helvetica", 10, "normal"), bd=1, bg='black', width=50, height=8)
textcon.pack(fill="both", expand=True)
mes_win = Entry(root, width=30, xscrollcommand=True, textvariable=message)
mes_win.place(x=20, y=320, height=60, width=750)
mes_win.focus()
textcon.config(fg='yellow')
textcon.tag_config('usr', foreground='white')
textcon.insert(END, "Chatu: This is Your ChatBot for Data Science Help!\n\n")
mssg = mes_win.get()
button = Button(root, text='SEND', bg='yellow', activebackground='orange', command=send, width=12, height=5,
                font=("Helvetica", 18, "bold"))
button.place(x=780, y=320, height=60, width=100)
scrollbar = tk.Scrollbar(textcon)
scrollbar.pack(fill='y')
scrollbar.place(relheight=1, relx=1)
scrollbar.config(command=textcon.yview)
content = widget_get()
text_contents[str(textcon)] = hash(content)
root.bind('<Control-s>', save, file_menu)
root.bind('<Control-Shift-s>', saveas, file_menu)
root.bind('<Return>', send, button)
root.bind('<Control-n>', new, file_menu)
root.bind('<Delete>', clear, edit_menu)
root.bind('<Control-o>', fopen, file_menu)
root.mainloop()
