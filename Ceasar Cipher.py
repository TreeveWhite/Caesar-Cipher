import tkinter, re, random, mmap

def encrypt_caesar(plain_text, shift):
  cipherText = ''
  for ch in plain_text:
    stayInAlphabet = ord(ch) + shift
    if ch.islower():
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      elif stayInAlphabet < ord('a'):
        stayInAlphabet += 26
    elif ch.isupper():
      if stayInAlphabet > ord('Z'):
        stayInAlphabet -= 26
      elif stayInAlphabet < ord('A'):
        stayInAlphabet += 26
    finalLetter = chr(stayInAlphabet)
    cipherText += finalLetter
  return cipherText

def decrypt_caesar(plain_text, shift):
  cipherText = ''
  for ch in plain_text:
    stayInAlphabet = ord(ch) + shift
    if ch.islower():
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      elif stayInAlphabet < ord('a'):
        stayInAlphabet += 26
    elif ch.isupper():
      if stayInAlphabet > ord('Z'):
        stayInAlphabet -= 26
      elif stayInAlphabet < ord('A'):
        stayInAlphabet += 26
    finalLetter = chr(stayInAlphabet)
    cipherText += finalLetter
  
  #Find if the decrypted word is in the dictionary.txt
  print(cipherText)
  with open("dictionary.txt", "r+") as file:
    for line in file:
      if cipherText.lower() == line.strip():
        print(cipherText, line.strip())
        return cipherText
        break
      

def startencrypt():
  message = application.entry.get()
  shift = random.randint(0, 26)
  application.changeAwnserLbl("Encyrpted Message: {}".format(encrypt_caesar(message, shift)))

def bruteforce():
  decryptMessage = ""
  application.changeAwnserLbl("")
  message = application.entry.get()
  for shift in range(26):
    decryptWord = decrypt_caesar(message, shift)
    if decryptWord != None:
      break
  application.changeAwnserLbl("Decrypted Message: {}".format(decryptWord))

#---------------------------GUI
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


if __name__ == "__main__":
  root = tkinter.Tk()
  root.title("Caesar Cipher")
  root.geometry("300x300")
  root.configure(bg="azure4")
  root.resizable(False, False)
  application = ui(root)

  root.mainloop()
