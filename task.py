# مصطفي محمد مصطفي محمد عبد الفتاح ابوعمر 
#سكشن 3 
from tkinter import *
import webbrowser
root = Tk()
root.geometry('300x300')
root.title('My Links App')
def open_link(url):
    webbrowser.open(url)
btn1 = Button(root, text='Python', width=20, height=2, 
              bg='blue', fg='white', font=15, 
              command=lambda: open_link('https://www.python.org'))
btn2 = Button(root, text='OpenAI', width=20, height=2, 
              bg='green', fg='white', font=15, 
              command=lambda: open_link('https://www.openai.com'))
btn3 = Button(root, text='YouTube', width=20, height=2, 
              bg='red', fg='white', font=15, 
              command=lambda: open_link('https://www.youtube.com'))
btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)

root.mainloop()
