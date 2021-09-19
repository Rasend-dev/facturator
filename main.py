from tkinter import *
import json
import os
import subprocess

PATH_JSON = os.path.join(os.path.join(os.getcwd(),'export'),'json_files')

root = Tk()
root.title('Facturacion')

prueba_botones = {'Sushi rico': 8999,'Sushi sabroso':3567,'Sushi extra rico':6543,'Teriyaki':4555,'Monas chinas':
                    5444,'pulpo a la braza':4555,'orlando sabroso':10000}

def _show_currency():
    subprocess.run(['py','run.py'],cwd='./Scraper/Scraper/spiders')
    with open(os.path.join(PATH_JSON,'mean_currencies.json'), 'r+') as f:
            content = json.load(f)
            f.seek(0)
    label_currencies = Label(hero,text=f'Precio del COP: {content["mean_usd_cop"]}, Precio del USD: {content["mean_usd_ves"]}')        
    label_currencies.grid(row=0,column=1)
    button_slide['state'] = DISABLED


def _charge(name):
    print(name)

def _load_hero(dicti):
    """
    A function that create buttons for the hero part
    """
    platillo = []
    for i in dicti.keys():
        platillo.append(Button(hero,text=i,padx=30,pady=30,command=lambda i=i: _charge(i))) #usando i=i en nuesta funcion lambda hacemos que el valor en el que esta el for se guarde

    for i, name in enumerate(platillo):
        platillo[i].grid(row=4,column=i,padx=20)
        if i >4:
            platillo[i].grid(row=6,column=i -5, padx=20)
    

def _load_price_label(dicti):
    """
    a function that load the price of each dish in the hero
    """
    for idx, price in enumerate(dicti.values()):
        price = Label(hero,text=f'{price}$')
        price.grid(row=3,column=idx)
        if idx > 4:
            price.grid(row=5,column=idx-5)
        

#slide side
slide = LabelFrame(root,text='Export zone',padx=20,pady=200)
slide.grid(row=0,column=0,sticky='n')

#principal side
hero = LabelFrame(root,text='Este es la parte principal',pady=120)
hero.grid(row=0,column=1,sticky='n')

#sum side
sum_side = LabelFrame(root,text='esto es una prueba',padx=300,pady=50)
sum_side.grid(row=1,column=1,sticky='s')

#Slider part
button_slide = Button(slide,text='Extract todays currency',padx=10,pady=10,command=_show_currency)
button_register = Button(slide,text='Register today work',padx=10,pady=10)
button_slide.grid(row=0,column=0,pady=10)
button_register.grid(row=1,column=0)

#Hero part
value = StringVar()
change_menu = OptionMenu(hero,value,'Principal','Entradas','Bebidas','Tempurizados','Adicionales')
hero_currencies = Label(hero,text='Current currency value: ')
hero_currencies.grid(row=1,column=0)
change_menu.grid(row=2,column=0,pady=5)

_load_hero(prueba_botones)

_load_price_label(prueba_botones)


sum_button = Button(sum_side,text='prueba',padx=10,pady=10)
sum_button.pack()

root.mainloop()