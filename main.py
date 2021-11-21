from tkinter import *
import json
import os
import subprocess

PATH_JSON = os.path.join(os.path.join(os.getcwd(),'export'),'json_files')

root = Tk()
root.title('Facturacion')

prueba_botones = {'Sushi rico': 8999,'Sushi sabroso':3567,'Sushi extra rico':6543,'Teriyaki':4555,'Monas chinas':
                    5444,'pulpo a la braza':4555,'orlando sabroso':10000,'Andrey mi fornite':3217,'empanada':13124
                    ,'cualquier cosa': 7722,'owo':9999,'el lol apesta':12312}

entradas = {'Empanada': 1500,'cocacola':2000,'jugo de limon':1456,'Teriyaki':4555,'Monas chinas':
                    5444,'pulpo a la braza':4555,'orlando sabroso':10000,'Andrey mi fornite':3217,'empanada':13124
                    ,'cualquier cosa': 7722,'owo':9999,'el lol apesta':12312}

def _show_currency():
    subprocess.run(['py','run.py'],cwd='./Scraper/Scraper/spiders')
    with open(os.path.join(PATH_JSON,'mean_currencies.json'), 'r+') as f:
            content = json.load(f)
            f.seek(0)
    label_currencies = Label(hero,text=f'Precio del COP: {content["mean_usd_cop"]}, Precio del USD: {content["mean_usd_ves"]}')        
    label_currencies.grid(row=0,column=1)
    button_slide['state'] = DISABLED

comanda = {} #Posicionamiento en la comanda
frames_comanda = {} #Memorizado de los frames de la comanda
root.count = 0 #posicionamiento de los frames

def _update_price(dicti):
    """
    Funcion que suma los precios de la comanda y los muestra
    """
    total_price = sum([dicti[i][2] for i in dicti]) #sumamos los precios de los platillos
    sum_cop['text'] = f'Total pesos:\n{total_price}$'

def _minus(name): 
    """
    Funcion que resta la comanda
    """
    if comanda[name][0] > 1:
        comanda[name][0] -= 1 #Restamos al numero de veces ordenaron el platillo
        comanda[name][2] = comanda[name][2] - prueba_botones[name] #restamos el precio
        comanda[name][1]['text'] = f'{comanda[name][0]}x {name}\n {comanda[name][2]}$ '
        _update_price(comanda) #actualizamos los precios

def _delete(frame,name):
    """
    Funcion que elimina un platillo entero de la comanda
    """
    frame.destroy() #Quitamos el framde de la vista
    comanda.pop(name) #Borramos el label de la memoria
    frames_comanda.pop(name) #Borramos el frame de la comanda
    root.count -= 1 #Restamos el contador

    for idx, key in enumerate(frames_comanda.keys()): #Ajustamos los grid de los frames
        frames_comanda[key].grid(row=1,column=idx)

    _update_price(comanda) #actualizamos los precios

def _charge(name,precio):
    """
    Funcion que nos sirve para poder cargar los platillos a la comanda
    """
    if name in comanda.keys(): #Caso de que ya este el nombre en la comanda

        comanda[name][0] += 1 #Sumamos el platillo 
        comanda[name].pop() #Quitamos el precio anterior
        comanda[name].append(precio*comanda[name][0]) # Renovamos el precio
        comanda[name][1]['text'] = f'{comanda[name][0]}x {name}\n {comanda[name][2]}$' #Cambiamos el label
        _update_price(comanda)
        
    else: #Caso de que no se haya añadido aun el nombre de la comanda

        comanda[name] = [1] #Creamos una lista con el numero de veces que se ha invocado el platillo
        frames_comanda[name] = Frame(sum_side) #hacemos un frame y lo guardamos en un diccionario

        frame = frames_comanda[name] #lo guardamos en una variable para poder manipularlo

        frame.grid(row=1,column=root.count,padx=5) #lo posicionamos utilizando el root.count

        #creamos los botones para modificar la comanda
        boton_minus = Button(frame,text='-',command=lambda :_minus(name))
        boton_delete = Button(frame, text='x',command=lambda : _delete(frame,name))

        #posicionamos los botones
        boton_minus.grid(row=0,column=0,sticky='e')
        boton_delete.grid(row=0,column=1)

        #colocamos el label en la memoria para poder trabajar con el más tarde
        comanda[name].append(Label(frame,text=f'{comanda[name][0]}x {name}\n{precio}$')) 
        comanda[name].append(precio)#colocamos el precio en la memoria

        comanda[name][1].grid(row=1,column=0) #posicionamos el label

        root.count += 1 #aumentamos el root.count para seguir posicionando
        _update_price(comanda) # actualizamos los precios
    

def _load_hero(dicti):
    """
    A function that create buttons for the hero part
    it recieves a dictionary and place the name in the sum part
    """
    #Carga de los precios
    for idx, price in enumerate(dicti.values()): 
        price = Label(hero,text=f'{price}$')
        price.grid(row=3,column=idx)
        if idx >= 5 and idx <= 9:
            price.grid(row=5,column=idx-5)
        elif idx >= 10 and idx <= 14:
            price.grid(row=7,column=idx-10)

    #Carga de los botones
    for idx, value in enumerate(dicti.keys()): 
        #usando i=value en nuesta funcion lambda hacemos que el valor en el que esta el for se guarde
        precio = dicti[value]
        platillo = Button(hero,text=value,padx=30,pady=30,command=lambda name=value, precio=precio: _charge(name,precio))
        platillo.grid(row=4,column=idx,padx=20) #Posicionamiento de los platillo
        if idx >= 5 and idx <= 9: 
            platillo.grid(row=6,column=idx-5,padx=20)
        elif idx >= 10 and idx <= 14:
            platillo.grid(row=8,column=idx-10,padx=20)    


def _update_hero(frame,dicti):
    for widget in frame.winfo_children():
        widget.destroy()
    _load_hero(dicti)

#container
container = Frame(root)
container.grid(row=0,column=0,sticky='w')

#slide side
slide = LabelFrame(container,text='Export zone',padx=20,pady=50)
slide.grid(row=0,column=0,sticky='w')

#principal side
hero = LabelFrame(container,text='Este es la parte principal')
hero.grid(row=0,column=1,sticky='nw')

#change hero button part
change = LabelFrame(container,text='Cambio de apartado',pady=92)
change.grid(row=0,column=2)

button = Button(change,text='Principal',command= lambda : _update_hero(hero,prueba_botones))
button_1 = Button(change,text='Entradas',command =lambda :_update_hero(hero,entradas))
button_2 = Button(change,text='Bebidas')
button_3 = Button(change,text='Tempurizados')
button_4 = Button(change,text='Adicionales')

button.pack()
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()

#sum side
sum_side = LabelFrame(root,text='esto es una prueba',pady=10)
sum_side.grid(row=1,column=0,sticky='w')
sum_button = Button(sum_side,text='hacer venta')
sum_cop = Label(sum_side)
sum_ves = Label(sum_side)
sum_usd = Label(sum_side)
sum_button.grid(row=0,column=0)
sum_cop.grid(row=0,column=1,sticky='w')
sum_ves.grid(row=0,column=2,sticky='w')
sum_usd.grid(row=0,column=3,sticky='w')

#Slider part
button_slide = Button(slide,text='Extract todays currency',padx=10,pady=10,command=_show_currency)
button_register = Button(slide,text='Register today work',padx=10,pady=10)
button_slide.grid(row=0,column=0,pady=10)
button_register.grid(row=1,column=0)

#Hero part
value = StringVar()
change_menu = OptionMenu(hero,value,'Principal','Entradas','Bebidas','Tempurizados','Adicionales')
hero_currencies = Label(hero,text='Current currency value: ')
#hero_currencies.grid(row=1,column=0)
#change_menu.grid(row=2,column=0,pady=5)

_load_hero(prueba_botones)

root.mainloop()