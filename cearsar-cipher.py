import re, random, mmap
from gui import ui

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


if __name__ == "__main__":
  root = tkinter.Tk()
  root.title("Caesar Cipher")
  root.geometry("300x300")
  root.configure(bg="azure4")
  root.resizable(False, False)
  application = ui(root)

  root.mainloop()
