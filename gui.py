import tkinter

class ui:
  def __init__(self, master):
    self.master = master
    
    self.title = tkinter.Label(self.master,
                               text="Caesar Cipher",
                               font=("Algerian", "20"),
                               fg="black",
                               bg="azure4"
                               ).place(x=45, y=0)

    self.txt = tkinter.Label(self.master,
                             text="Text: ",
                             font=("Algerian", "12"),
                             bg="azure4"
                             ).place(x=38, y=50)
    
    self.entry = tkinter.Entry(self.master,
                               font=("Adobe Garamond Pro Bold", "12"),
                               bg="DarkGoldenrod1")
    self.entry.place(x=88, y=50)

    self.brute = tkinter.Button(self.master,
                                text="Brute Force\nDecrypt",
                                font=("Adobe Garamond Pro Bold", "12"),
                                command=bruteforce,
                                bg="DarkGoldenrod1",
                                width=11
                                ).place(x=35, y=100)
    
    self.encrypt = tkinter.Button(self.master,
                                  text="Encrypt\n",
                                  font=("Adobe Garamond Pro Bold", "12"),
                                  command=startencrypt,
                                  bg="DarkGoldenrod1",
                                  width=11
                                  ).place(x=160, y=100)
    
    self.awnser = tkinter.Label(self.master,
                                text="",
                                width=28,
                                height=5,
                                bg="DarkGoldenrod1",
                                relief = "groove",
                                font=("Adobe Garamond Pro Bold", "12"))
    self.awnser.place(x=21, y=175)

  def changeAwnserLbl(self, text):
    self.awnser.configure(text=text)
