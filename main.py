from tkinter import *
import json
import os
import subprocess

PATH_JSON = os.path.join(os.path.join(os.getcwd(),'export'),'json_files')

root = Tk()
root.title('Facturacion')

def _show_currency():
    subprocess.run(['py','run.py'],cwd='./Scraper/Scraper/spiders')
    with open(os.path.join(PATH_JSON,'mean_currencies.json'), 'r+') as f:
            content = json.load(f)
            f.seek(0)
    label_currencies = Label(hero,text=f'Precio del COP: {content["mean_usd_cop"]}, Precio del USD: {content["mean_usd_ves"]}')        
    label_currencies.grid(row=0,column=1)
    button_slide['state'] = DISABLED

def _load_principal_dishes():
    """
    A function that create buttons for the hero part
    """
    for i in range(10):
        platillo = Button(hero,text=f'Platillo numero {i + 1}',padx=30,pady=30)
        platillo.grid(row=3,column=i,padx=20)
        if i > 4:
            platillo.grid(row=5,column=i - 5,padx=20)
    pass

def _load_price_label():
    """
    a function that 
    """
    for i in range(10):
        mitad = 10 // 5
        price = Label(hero,text='Precio: 123123$')
        price.grid(row=mitad,column=i)
        if i > 4:
            price.grid(row=mitad + 2,column=i-5)
        

#slide side
slide = LabelFrame(root,text='Export zone',padx=20,pady=200)
slide.grid(row=0,column=0)

#principal side
hero = LabelFrame(root,text='Este es la parte principal',pady=120)
hero.grid(row=0,column=1)

#sum side
sum_side = LabelFrame(root,text='esto es una prueba',padx=450,pady=50)
sum_side.grid(row=1,column=1)

#Slider part
button_slide = Button(slide,text='Extract todays currency',padx=10,pady=10,command=_show_currency)
button_register = Button(slide,text='Register today work',padx=10,pady=10)
button_slide.grid(row=0,column=0,pady=10)
button_register.grid(row=1,column=0)

#Hero part
hero_currencie = Label(hero,text='Current currency value:')
hero_label = Label(hero,text = 'Platillos disponibles: \n')
hero_currencie.grid(row=0,column=0)
hero_label.grid(row=1,column=0)

_load_principal_dishes()

_load_price_label()


sum_button = Button(sum_side,text='prueba',padx=10,pady=10)
sum_button.pack()

root.mainloop()