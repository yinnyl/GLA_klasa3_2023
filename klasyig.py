# klasa: schemat np. człowiek
# obiekty: instancja klasy np. jakieś konkretne imiona

class Point:  # nazwę klasy piszemy wielką litery!
    default_color = "red"  # atrybut klasy

    def __init__(self, x, y):  # magiczna metoda (magic method), init - konstruktor, który odpala wszystko po zainicjowaniu klasy
        self.x = x       # inicjalizacja klasy z wartościami, które trzeba przypisać do self; referencja do obecnego parametru
        self.y = y
    def draw(self): # pierwszy parametr funkcji w klasie to zawsze ma być self
        print(f"Point ({self.x}, {self.y})")  # print(f"... = drukowanie stringa formatowanego (wstawi zmienną jak zonaczy {})

Point.default_color = "yellow" # zmienienie atrybuty klasy?

# stworzenie instancji obiektu klasy; inicjowanie obiektu
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

print(type(point))  # <class '__main__.Point'>, klasa o nazwie Point z modułu main
print(isinstance(point, Point))  # (zainicjowany obiekt, klasa)

print(point.x)
point.z = 10  # przykładowy atrybut instancji dodany do objektu


another = Point(3, 4)  # klasa to "pojemnik" na dane, ale bez konkretnych wartości
print(another.default_color)
another.draw()