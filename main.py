from tkinter import *

def action():
    ch = str (entryPhrase.get())
    key= int (entryKey.get())
    lblChiffre['text'] = "Votre message chiffré :"
    def code_ascii(lettre, entryKey):
        num = ord(lettre) + entryKey
        if num > 122:
            num -= 26
        return chr(num)

        def cesar(entryPhrase, entryKey):
            chiffrés = ""
              for lettre in entryPhrase:
                 if entryPhrase == " ":
                chiffrés += " "
            else:
                 chiffrés += code_ascii(entryPhrase, entryKey)
        return chiffrés

    print(cesar(entryPhrase, entryKey))

fen = Tk()
fen.geometry("400x175")

lblPhrase = Label(fen, text = "Entrez une phrase : ")
lblPhrase.place(x = 10, y = 20)
entryPhrase = Entry(fen)
entryPhrase.place(x = 200 , y = 20)

lblKey = Label(fen, text = "Entrez une clé : ")
lblKey.place(x = 10 , y=50)
entryKey = Entry(fen)
entryKey.place(x = 200 , y = 50)

Valider = Button(fen, text = "Valider l'opération", command = action)
Valider.place(x=200, y = 90)

lblChiffre = Label(fen, text = "Votre message chiffré : ")
lblChiffre.place(x = 10 , y=120)


fen.mainloop()