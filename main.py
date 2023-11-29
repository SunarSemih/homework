import turtle

#ekran ayarları
cizimTahtası = turtle.Screen()
cizimTahtası.bgcolor("#6a8")
cizimTahtası.title("Kaplumbağa Denemesi")


#kaplumbağa star
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(53.5)
    turtle_instance.forward(100)
    turtle_instance.left(-126.5)
    turtle_instance.forward(100)



turtle.done()