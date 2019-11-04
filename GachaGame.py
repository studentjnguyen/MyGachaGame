from tkinter import *
import random


def origin_screen():
    background_image = Label(root, image=background_photo)
    background_image.place(relwidth=1, relheight=1)
    regular_summon = Button(root, text="Regular summons", bg="grey", fg="black")
    regular_summon.place(relx=0.25, rely=0.5, anchor=CENTER)
    premium_summon = Button(root, text="Premium summons", bg="gold", fg="red")
    premium_summon.place(relx=0.75, rely=0.5, anchor=CENTER)
    free_five = Button(root, text="FREE FIVE STAR", bg="purple", fg="light blue", command=five_star)
    free_five.place(relx=0.5, rely=0.7, anchor=CENTER)


def five_star():
    background_image = Label(root, image=win_photo)
    background_image.place(relwidth=1, relheight=1)
    back_button = Button(root, text="return", command=origin_screen, bg="black", fg="white")
    back_button.place(relx=0.5, rely=0.95, anchor=CENTER)
    free_rates = random.randint(1, 7)
    if free_rates == 1:
        label1 = Label(root, image=legendarygear4th_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="LEGENDARY GEAR FOURTH MIKE WAZOWSKI 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 2:
        label1 = Label(root, image=ok_mikeweird)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="OK MIKE WAZOWSKI 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 3:
        label1 = Label(root, image=friekegel_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="fake dimitri mike 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 4:
        label1 = Label(root, image=shrek_photo)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="shrekzowski 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 5:
        label1 = Label(root, image=duo_photo)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="DUO SKILL MIKE 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 6:
        label1 = Label(root, image=legendary_jesse)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="DUO LEGENDARY JESSE AND MIKE WAZOWSKI SAMA 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 7:
        label1 = Label(root, image=gear_second_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="LEGENDARY GEAR SECOND MIKE 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif free_rates == 8:
        label1 = Label(root, image=ivankov_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="LEGENDARY IVANKOV MIKE 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)


def premium_summons():
    background_image = Label(root, image=premium_photo)
    background_image.place(relwidth=1, relheight=1)
    back_button = Button(root, text="return", command=origin_screen, bg="black", fg="white")
    back_button.place(relx=0.5, rely=0.95, anchor=CENTER)
    premium_rates = random.randint(1, 100)
    if premium_rates == 1:
        label1 = Label(root, image=legendarygear4th_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="LEGENDARY GEAR FOURTH MIKE WAZOWSKI 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 2:
        label1 = Label(root, image=ok_mikeweird)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="OK MIKE WAZOWSKI 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 3:
        label1 = Label(root, image=friekegel_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="fake dimitri mike 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 4:
        label1 = Label(root, image=shrek_photo)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="shrekzowski 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 5:
        label1 = Label(root, image=duo_photo)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="DUO SKILL MIKE 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 6:
        label1 = Label(root, image=legendary_jesse)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="DUO LEGENDARY JESSE AND MIKE WAZOWSKI SAMA 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 7:
        label1 = Label(root, image=gear_second_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="LEGENDARY GEAR SECOND MIKE 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif premium_rates == 8:
        label1 = Label(root, image=ivankov_mike)
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label2 = Label(root, text="LEGENDARY IVANKOV MIKE 5*", bg="gold", fg="purple")
        label2.place(relx=0.5, rely=0.9, anchor=CENTER)

# def regular_summons():
#     regular_rates = random.randint(1, 1000)


root = Tk()

root.geometry('1280x720')
root.title("Gachi Game")

background_photo = PhotoImage(file="maxresdefault.png")
wypers_cry = PhotoImage(file="4.png")
ok_mikeweird = PhotoImage(file="77e.png")
legendarygear4th_mike = PhotoImage(file="77e2.png")
friekegel_mike = PhotoImage(file="734.png")
clown_frog = PhotoImage(file="honklhonk.png")
regular_photo = PhotoImage(file="normalbackground.png")
premium_photo = PhotoImage(file="premiumbackground.png")
win_photo = PhotoImage(file="5starbackground.png")
shrek_photo = PhotoImage(file="images (2).png")
duo_photo = PhotoImage(file="images (1).png")
legendary_jesse = PhotoImage(file="legendaryjesse.png")
gear_second_mike = PhotoImage(file="gearsecondmike.png")
ivankov_mike = PhotoImage(file="ivakovmike.png")

background_image = Label(root, image=background_photo).place(relwidth=1, relheight=1)

regular_summon = Button(root, text="Regular summons", bg="grey", fg="black").place(relx=0.25, rely=0.5, anchor=CENTER)
premium_summon = Button(root, text="Premium summons", bg="gold", fg="red", command=premium_summons).\
    place(relx=0.75, rely=0.5, anchor=CENTER)
free_five = Button(root, text="FREE FIVE STAR", bg="purple", fg="light blue", command=five_star).\
    place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
