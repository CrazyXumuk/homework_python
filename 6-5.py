class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")

class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")

start = Stationery()
start.draw()
pen = Pen("Pilot")
pen.draw()
pencil = Pencil("Сибирский кедр")
pencil.draw()
marker = Marker("Copic")
marker.draw()