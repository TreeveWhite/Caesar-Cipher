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
  application.changeAwnserLbl("The Encyption is: " + cipherText)

def decrypt_caesar(plain_text, shift, i):
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
  key = cipherText.lower()
  import mmap
  info = False
  bytes = str.encode(str(key.lower()))
  type(bytes)

  with open('dictionary.txt', 'rb', 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if s.find(bytes) != -1:
        info = True

  with open("dictionary.txt", "r+") as file:
    if info == True:
      for line in file:
        if key.lower() in line:
          application.changeAwnserLbl("The Transcript is: " + key)
          break

def startencrypt():
  application.changeAwnserLbl("")
  message = application.entry.get()
  shift = random.randint(0, 26)
  encrypt_caesar(message, shift)

def bruteforce():
  application.changeAwnserLbl("")
  message = application.entry.get()
  for i in range(26):
      shift = i
      decrypt_caesar(message, shift, i)

#---------------------------GUI
class ui:
  def __init__(self, master):
    self.master = master
    
    self.title = tkinter.Label(self.master, text="Caesar Cipher", font=("Algerian", "20"), fg="black", bg="azure4").place(x=30, y=0)

    self.txt = tkinter.Label(self.master, text="Text: ", font=("Algerian", "12"), bg="azure4").place(x=0, y=50)
    self.entry = tkinter.Entry(self.master, font=("Arial", "12"), bg="DarkGoldenrod1")
    self.entry.place(x=50, y=50)

    self.brute = tkinter.Button(self.master, text="Brute Force\nDecrypt", font=("Arial", "12"), command=bruteforce, bg="DarkGoldenrod1").place(x=45, y=100)
    self.encrypt = tkinter.Button(self.master, text="Encrypt\n", font=("Arial", "12"), command=startencrypt, bg="DarkGoldenrod1").place(x=170, y=100)
    self.awnser = tkinter.Label(self.master, text="", font=("Arial", "12"), bg="azure4")
    self.awnser.place(x=50, y=75)

  def changeAwnserLbl(self, text):
    self.awnser.configure(text=text)


if __name__ == "__main__":
  root = tkinter.Tk()
  root.title("Caesar Cipher")
  root.geometry("250x200")
  root.configure(bg="azure4")

  application = ui(root)

  root.mainloop()