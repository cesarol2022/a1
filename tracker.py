from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title ("Localizar o Telefone")
root.geometry("365x584+1000+75")
root.resizable(False,False)

def Track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)


    # Country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)


    # Operator 
    operator=carrier.name_for_number(number,'en')
    sim.config(text=operator)

    # Phone Timezone
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)


    # Longitude Latitude
    geolocator= Nominatim(user_agent="geoapiExercices")
    location= geolocator.geocode(locate)
    lng=location.longitude
    lat=location.latitude    
    longitude.config(text=lng)   
    latitude.config(text=lat)
        

    # Time showing in phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)


# Icon image
icon=PhotoImage(file="logoimage.png")
root.iconphoto(False,icon)

# logo
logo=PhotoImage(file="logoimage.png")
Label(root,image=logo).place(x=240,y=70)

Eback=PhotoImage(file="searchpng.png")
Label(root,image=Eback).place(x=20,y=190)

# Heading
Heading=Label(root,text="LOCALIZAR O TELEFONE",font=('arial',15,'bold'))
Heading.place(x=10,y=110)

# Botton box
Box=PhotoImage(file="bottom.png")
Label(root,image=Box).place(x=-2,y=355)

# Entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=('arial',20))
enter_number.place(x=50,y=220)

# Search button
Search_image=PhotoImage(file="search.png")
search=Button(root,image=Search_image,borderwidth=0,cursor="hand2",bd=0,command=Track)
search.place(x=35,y=300)

# Label (information)
country=Label(root,text="País:",bg="#57adff",fg="black",font=('arial',10,'bold'))
country.place(x=50,y=400)

sim=Label(root,text="Operadora:",bg="#57adff",fg="black",font=('arial',10,'bold'))
sim.place(x=200,y=400)

zone=Label(root,text="Área:",bg="#57adff",fg="black",font=('arial',10,'bold'))
zone.place(x=50,y=450)

clock=Label(root,text="Hora:",bg="#57adff",fg="black",font=('arial',10,'bold'))
clock.place(x=50,y=500)

longitude=Label(root,text="Longitude:",bg="#57adff",fg="black",font=('arial',10,'bold'))
longitude.place(x=200,y=550)

latitude=Label(root,text="Latitude:",bg="#57adff",fg="black",font=('arial',10,'bold'))
latitude.place(x=50,y=550)


root.mainloop()


