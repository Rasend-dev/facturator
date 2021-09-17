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
hero_label = Label(hero,text = 'Platillos disponibles: \n\n')
hero_currencie.grid(row=0,column=0)
hero_label.grid(row=1,column=0)

#precio de los platillos
price_1 = Label(hero,text='Precio: 123123$')
price_2 = Label(hero,text='Precio: 123123$')
price_3 = Label(hero,text='Precio: 123123$')
price_4 = Label(hero,text='Precio: 123123$')
price_5 = Label(hero,text='Precio: 123123$')
price_6 = Label(hero,text='Precio: 123123$')
price_7 = Label(hero,text='Precio: 123123$')
price_8 = Label(hero,text='Precio: 123123$')


#Botones de platillos
platillo_1 = Button(hero,text='Platillo numero 1',padx=30,pady=30)
platillo_2 = Button(hero,text='Platillo numero 2',padx=30,pady=30)
platillo_3 = Button(hero,text='Platillo numero 3',padx=30,pady=30)
platillo_4 = Button(hero,text='Platillo numero 4',padx=30,pady=30)
platillo_5 = Button(hero,text='Platillo numero 5',padx=30,pady=30)
platillo_6 = Button(hero,text='Platillo numero 6',padx=30,pady=30)
platillo_7 = Button(hero,text='Platillo numero 7',padx=30,pady=30)
platillo_8 = Button(hero,text='Platillo numero 8',padx=30,pady=30)

price_1.grid(row=2,column=0)
price_2.grid(row=2,column=1)
price_3.grid(row=2,column=2)
price_4.grid(row=2,column=3)
price_5.grid(row=4,column=0)
price_6.grid(row=4,column=1)
price_7.grid(row=4,column=2)
price_8.grid(row=4,column=3)

platillo_1.grid(row=3,column=0,padx=20)
platillo_2.grid(row=3,column=1,padx=20)
platillo_3.grid(row=3,column=2,padx=20)
platillo_4.grid(row=3,column=3,padx=20)
platillo_5.grid(row=5,column=0,padx=20)
platillo_6.grid(row=5,column=1,padx=20)
platillo_7.grid(row=5,column=2,padx=20)
platillo_8.grid(row=5,column=3,padx=20)

sum_button = Button(sum_side,text='prueba',padx=10,pady=10)
sum_button.pack()

root.mainloop()