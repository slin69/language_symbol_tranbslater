from tkinter import *

root=Tk()
text_symbol={
    "`":"a",
    "~":"b",
    "<":"c",
    "@":"d",
    "#":"e",
    "$":"f",
    "%":"g",
    "^":"h",
    "&":"i",
    "*":"j",
    "(":"k",
    ")":"l",
    "_":"m",
    "-":"n",
    "=":"o",
    "+":"p",
    "[":"q",
    "]":"r",
    "{":"s",
    "}":"t",
    "|":"u",
    ";":"v",
    ":":"w",
    "/":"x",
    "😂":"y",
    ">":"z",

}
class Gui:
    def __init__(self):
        #tags with tkinter
        self.entry=Entry(root)
        self.encode=Button(root,text="encode",command=self.encode)
        self.decode=Button(root,text="decode",command=self.decode)
        self.new_string=Label(root,text="None")
        #/////////////////
        #packing tags
        self.entry.pack()
        self.encode.place(x=135,y=22)
        self.decode.place(x=215,y=22)
        #self.new_string.place(x=150,y=50)
        #?////////////////
        #key binding
        #//////////////////////
        root.geometry("400x400")
        root.mainloop()
    def encode(self):
        text=self.entry.get().lower()
        print(text)
        text=list(text)
        values_list=list(text_symbol.values())
        keys_list=list(text_symbol.keys())
        for t in range(len(text)):
            for v in range(len(values_list)):
                if text[t]==values_list[v]:
                    #print(f"{text[t]} : {keys_list[v]}")
                    text[t]=keys_list[v]
        text=''.join(text)
        self.entry.delete(0,END)
        self.entry.insert(0,text)
        print(text)
    def decode(self):
        text=self.entry.get().lower()
        print(text)
        text=list(text)
        values_list=list(text_symbol.values())
        keys_list=list(text_symbol.keys())
        for t in range(len(text)):
            for v in range(len(keys_list)):
                if text[t]==keys_list[v]:
                    #print(f"{text[t]} : {keys_list[v]}")
                    text[t]=values_list[v]
        text=''.join(text)
        self.entry.delete(0,END)
        self.entry.insert(0,text)
        print(text)


Gui()

'''text_symbol={
    "`":"a",
    "~":"b",
    "<":"c",
    "@":"d",
    "#":"e",
    "$":"f",
    "%":"g",
    "^":"h",
    "&":"i",
    "*":"j",
    "(":"k",
    ")":"l",
    "_":"m",
    "-":"n",
    "=":"o",
    "+":"p",
    "[":"q",
    "]":"r",
    "{":"s",
    "}":"t",
    "|":"u",
    ";":"v",
    ":":"w",
    "/":"x",
    "😂":"y",
    ">":"z",

}
input=input("input sentence: ")
def encode(text):
    print(text)
    text=list(text)
    values_list=list(text_symbol.values())
    keys_list=list(text_symbol.keys())
    for t in range(len(text)):
        for v in range(len(values_list)):
            if text[t]==values_list[v]:
                #print(f"{text[t]} : {keys_list[v]}")
                text[t]=keys_list[v]
    text=''.join(text)
    print(text)
encode(input)'''
