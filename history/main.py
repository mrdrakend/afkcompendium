from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import data as d
from data import heroes_dict

# Colors
c1 = '#000000' # Black
c2 = '#FFFFFF' # White
c3 = '#712F85' # Purple
c4 = '#F2E297' # Yellow
c5 = '#779A71' # Green
c6 = '026B5C' # Dark Green
c7 = '#1F75FE' # Blue
c8 = '#FF0000' # Red

#window
window = Tk()
window.title("AFK Compendium")
window.configure(background=c2)
window.geometry("550x510")

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use('clam')

# Frames
frame_hero = Frame(window, width=550, height=290, relief='flat')
frame_hero.grid(row=1, column=0)

def hero_select(hero):
    global hero_img, hero_placement, sig_img, hero_sig_img, hero_background

    hero_img = Image.open(heroes_dict[hero]['img'])
    hero_img = hero_img.resize((230, 230))
    hero_img = ImageTk.PhotoImage(hero_img)

    sig_img = Image.open(heroes_dict[hero]['sig_img'])
    sig_img = sig_img.resize((100, 100))
    sig_img = ImageTk.PhotoImage(sig_img)

    hero_placement.configure(image=hero_img)
    hero_placement.image = hero_img
    
    hero_sig_img.configure(image=sig_img)
    hero_sig_img.image = sig_img

    hero_background = heroes_dict[hero]['background']

    hero_name.configure(text=heroes_dict[hero]['name'])
    hero_fac.configure(text=heroes_dict[hero]['fac'])
    hero_role.configure(text=heroes_dict[hero]['role'])
    hero_sig.configure(text=heroes_dict[hero]['sig'])
    hero_background.configure(bg=heroes_dict[hero]['background'])


    hero_skill_1.configure(text=heroes_dict[hero]['skills']['skill_1'])
    hero_skill_2.configure(text=heroes_dict[hero]['skills']['skill_2'])
    hero_skill_3.configure(text=heroes_dict[hero]['skills']['skill_3'])
    hero_skill_4.configure(text=heroes_dict[hero]['skills']['skill_4'])



# Labels
hero_name = Label(frame_hero, text="Alna", font=("Ivy", 20, 'bold'), relief='flat', anchor='center')
hero_name.place(x=12, y=5)

hero_fac = Label(frame_hero, text="Celestial", font=("Ivy", 15), relief='flat', anchor='center')
hero_fac.place(x=12, y=40)

hero_role = Label(frame_hero, text="Debuffer", font=("Ivy", 15), relief='flat', anchor='center')
hero_role.place(x=12, y=75)

# HERO IMAGE
hero_img = Image.open('images/heroes/alna.png')
hero_img = hero_img.resize((230, 230))
hero_img = ImageTk.PhotoImage(hero_img)

# SIGNATURE ITEM IMAGE
sig_img = Image.open('images/items/alna_sigitem.webp')
sig_img = sig_img.resize((100, 100))
sig_img = ImageTk.PhotoImage(sig_img)

hero_placement = Label(frame_hero, image=hero_img, relief='flat')
hero_placement.place(x=120, y=35)

hero_name.lift()
hero_fac.lift()
hero_role.lift()
frame_hero.lift()

hero_skill_title = Label(window, text="Skills", font=("Ivy", 20))
hero_skill_title.place(x=15, y=310)

hero_skill_1 = Label(window, text="Winter War Cry", font=("Ivy", 15))
hero_skill_1.place(x=15, y=360)

hero_skill_2 = Label(window, text="Freezing Pierce", font=("Ivy", 15))
hero_skill_2.place(x=15, y=385)

hero_skill_3 = Label(window, text="Winter's Call", font=("Ivy", 15))
hero_skill_3.place(x=15, y=411)

hero_skill_4 = Label(window, text="Frozen Fury", font=("Ivy", 15))
hero_skill_4.place(x=15, y=437)

hero_skill_title.lift()

hero_sig_title = Label(window, text="Signature Item", font=("Ivy", 20))
hero_sig_title.place(x=300, y=310)

hero_sig = Label(window, text="Frostbite", font=("Ivy", 15))
hero_sig.place(x=300, y=355)

hero_sig_img = Label(window, image=sig_img, relief='flat')
hero_sig_img.place(x=300, y=385)

hero_sig_title.lift()

# Buttons

# Button Images
ico_img_1 = Image.open('images/heroes portraits/Alna_portrait.png')
ico_img_1 = ico_img_1.resize((50, 50))
ico_img_1 = ImageTk.PhotoImage(ico_img_1)

btn_ico_img_1 = Button(window, command=lambda:hero_select('Alna'), image=ico_img_1, text=' Alna', width=150, relief='raised', overrelief='ridge', compound='left', anchor='nw', font=("Ivy", 12, 'bold'), fg=c1, bg=c2)
btn_ico_img_1.place(x=375, y=5)

ico_img_2 = Image.open('images/heroes portraits/Arthur_portrait.png')
ico_img_2 = ico_img_2.resize((50, 50))
ico_img_2 = ImageTk.PhotoImage(ico_img_2)

btn_ico_img_2 = Button(window, command=lambda:hero_select('Arthur'), image=ico_img_2, text=' Arthur', width=150, relief='raised', overrelief='ridge', compound='left', anchor='nw', font=("Ivy", 12, 'bold'), fg=c1, bg=c2)
btn_ico_img_2.place(x=375, y=65)

ico_img_3 = Image.open('images/heroes portraits/Belinda_portrait.png')
ico_img_3 = ico_img_3.resize((50, 50))
ico_img_3 = ImageTk.PhotoImage(ico_img_3)

btn_ico_img_3 = Button(window,  command=lambda:hero_select('Belinda'), image=ico_img_3, text=' Belinda', width=150, relief='raised', overrelief='ridge', compound='left', anchor='nw', font=("Ivy", 12, 'bold'), fg=c1, bg=c2)
btn_ico_img_3.place(x=375, y=125)

ico_img_4 = Image.open('images/heroes portraits/Numisu_portrait.png')
ico_img_4 = ico_img_4.resize((50, 50))
ico_img_4 = ImageTk.PhotoImage(ico_img_4)

btn_ico_img_4 = Button(window,  command=lambda:hero_select('Numisu'), image=ico_img_4, text=' Numisu', width=150, relief='raised', overrelief='ridge', compound='left', anchor='nw', font=("Ivy", 12, 'bold'), fg=c1, bg=c2)
btn_ico_img_4.place(x=375, y=185)

ico_img_5 = Image.open('images/heroes portraits/Tasi_portrait.png')
ico_img_5 = ico_img_5.resize((50, 50))
ico_img_5 = ImageTk.PhotoImage(ico_img_5)

btn_ico_img_5 = Button(window, command=lambda:hero_select('Tasi'), image=ico_img_5, text=' Tasi', width=150, relief='raised', overrelief='ridge', compound='left', anchor='nw', font=("Ivy", 12, 'bold'), fg=c1, bg=c2)
btn_ico_img_5.place(x=375, y=245)

window.mainloop()
