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

memory = {}
root.count = 0 #posicionamiento de los frames

def _minus(name):
    if memory[name][0] > 1:
        memory[name][0] -= 1 #Restamos al numero de veces que fue pulsado el boton
        memory[name][2] = memory[name][2] - prueba_botones[name] #restamos el precio
        memory[name][1]['text'] = f'{memory[name][0]}x {name}\n {memory[name][2]}$ '

def _delete(platillo,name):
    platillo.destroy()
    memory.pop(name)
    root.count -= 1

def _charge(name):
    precio = prueba_botones[name]
    if name in memory.keys(): #Caso de que ya este el nombre en la comanda
        memory[name][0] += 1
        memory[name].pop() #Eliminamos el resultado anterior para evitar que se aglomeren
        memory[name].append(precio*memory[name][0]) # precio multiplicado
        memory[name][1]['text'] = f'{memory[name][0]}x {name}\n {memory[name][2]}$'
    else: #Caso de que no se haya añadido aun el nombre de la comanda
        memory[name] = [1] #Creamos una lista con el numero de veces que se ha invocado el platillo
        platillo = Frame(sum_side) #hacemos un frame
        platillo.grid(row=1,column=root.count,padx=5) #lo posicionamos utilizando el root.count
        boton = Button(platillo,text='-',command=lambda :_minus(name))#creamos los botones para modificar la comanda
        boton_2 = Button(platillo, text='x',command=lambda: _delete(platillo,name))
        boton.grid(row=0,column=0,sticky='e')
        boton_2.grid(row=0,column=1)
        memory[name].append(Label(platillo,text=f'{name}\n{precio}$')) #colocamos el label en la memoria para poder trabajar con el más tarde
        memory[name].append(precio)#colocamos el precio en la memoria
        memory[name][1].grid(row=1,column=0) #la posicionamos
        root.count += 1 #aumentamos el root.count para seguir posicionando
    print(memory.keys())

def _load_hero(dicti):
    """
    A function that create buttons for the hero part
    it recieves a dictionary and place the name in the sum part
    """
    platillo = []
    for i in dicti.keys(): #usando i=i en nuesta funcion lambda hacemos que el valor en el que esta el for se guarde
        platillo.append(Button(hero,text=i,padx=30,pady=30,command=lambda i=i: _charge(i))) 

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
slide.grid(row=0,column=0,sticky='w')

#principal side
hero = LabelFrame(root,text='Este es la parte principal',pady=120)
hero.grid(row=0,column=1,sticky='w')

#sum side
sum_side = LabelFrame(root,text='esto es una prueba',pady=10)
sum_side.grid(row=1,column=1,sticky='w')

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


sum_button = Button(sum_side,text='hacer venta')
sum_button.grid(row=0,column=0)

root.mainloop()