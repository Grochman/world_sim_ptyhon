import math
import random
import pickle
import tkinter as tk

from Plants.Plant import Plant
from Animals.Animal import Animal

from Animals.Sheep import Sheep
from Animals.Wolf import Wolf
from Animals.Fox import Fox
from Animals.Antelope import Antelope
from Animals.Turtle import Turtle
from Animals.Human import Human
from Plants.Grass import Grass
from Plants.Dandelion import Dandelion
from Plants.Guarana import Guarana
from Plants.Nightshade import Nightshade
from Plants.PineBorscht import PineBorscht
from Animals.CyberSheep import CyberSheep


class World:
    __instance = None

    @staticmethod
    def get_instance():
        if World.__instance is None:
            World()
        return World.__instance

    def __init__(self):

        if World.__instance is None:
            self.__organisms = []
            self.pine = []
            self.__animals = None

            self.__window_width = 1000
            self.__window_height = 700
            self.__window = tk.Tk()
            self.__window.title("My Window")
            self.__window.resizable(False, False)
            self.__window.bind('<KeyPress>', self.__turn)

            self.__legenda_panel = tk.Frame(self.__window, width=self.__window_width / 4,
                                            height=self.__window_height * 3 / 4)
            self.__legenda_panel.grid(row=0, column=0)
            data = [("Antelope", "brown"), ("CyberSheep", "#3bfff2"), ("Dandelion", "yellow"), ("Fox", "orange"), ("Grass", "#19e34f"),
                    ("Guarana", "#ff5eea"), ("Human", "black"), ("Nightshade", "blue"), ("Pine Borscht", "red"), ("Sheep", "white"),
                    ("Turtle", "green"), ("Wolf", "#363636")]
            for index, (label_text, color) in enumerate(data):
                label = tk.Label(self.__legenda_panel, text=label_text)
                label.grid(sticky="w")
                square = tk.Label(self.__legenda_panel, width=1, height=1, bg=color)
                square.grid(row=label.grid_info()["row"], column=1)

            self.__game_panel = tk.Frame(self.__window, bg="blue", width=self.__window_width / 2,
                                         height=self.__window_height * 3 / 4)
            self.__game_panel.grid(row=0, column=1)
            self.sym_width = 20
            self.sym_height = 20
            self.box_size = 10

            self.__sym_panel = tk.Canvas(self.__game_panel, bg="gray", width=self.sym_width * self.box_size,
                                         height=self.sym_height * self.box_size)
            self.__sym_panel.place(x=self.__window_width / 4 - self.sym_width * self.box_size / 2, y=50)
            self.__sym_panel.bind("<Button-1>", self.printpos)

            self.__logs_panel = tk.Frame(self.__window, bg="green", width=self.__window_width / 4,
                                         height=self.__window_height * 3 / 4)
            self.__logs_panel.grid(row=0, column=2)
            self.__logs_panel.grid_propagate(False)
            self.__logs = []

            self.__tools_panel = tk.Frame(self.__window, bg="pink", height=self.__window_height / 4)
            self.__tools_panel.grid(row=1, column=0, columnspan=3, sticky="nsew")
            self.__save_b = tk.Button(self.__tools_panel, text="save", command=self.save)
            self.__load_b = tk.Button(self.__tools_panel, text="load", command=self.load)
            self.__round_b = tk.Button(self.__tools_panel, text="next round")
            self.__round_b.bind("<Button-1>", lambda event: self.__turn(event))
            self.__load_b.pack()
            self.__save_b.pack()
            self.__round_b.pack()

            self.__window.update()
            World.__instance = self

        else:
            raise Exception("this is a singleton!")

    def run(self):
        self.__window.mainloop()

    def __draw(self):
        for org in self.__organisms:
            self.__sym_panel.coords(org.sprite, org.x, org.y, org.x + self.box_size, org.y + self.box_size)

    def __turn(self, event):
        org_s_flag = False
        self.human_dir = event.keysym

        for log in self.__logs:
            log.grid_forget()
        self.__logs.clear()

        for org in self.__organisms:
            org.action()

            if isinstance(org, Plant):
                while org.plant() != 0:
                    self.__add_plant(org)
            elif event.keysym == 'space' and isinstance(org, Human) and org.cooldown == 10:
                self.__logs.append(tk.Label(self.__logs_panel, text="activated superpower!"))

            for other in self.__organisms.copy():
                if other.x == org.x and other.y == org.y and not (other is org):
                    org_s_flag = True
                    result = other.collision(org)
                    cords = str(org.x) + " " + str(org.y) + " "
                    message = " "
                    if result == 0:
                        self.__sym_panel.delete(org.sprite)
                        self.__organisms.remove(org)
                        if isinstance(other, Plant):
                            self.__sym_panel.delete(other.sprite)
                            self.__organisms.remove(other)
                            message = " died from eating eaten "
                        else:
                            message = " got killed by "
                    elif result == 1:
                        self.__sym_panel.delete(other.sprite)
                        self.__organisms.remove(other)
                        if isinstance(other, Plant):
                            message = " eaten "
                        else:
                            message = " killed "
                    elif result == 2:
                        message = " didn't catch "
                    elif result == 3:
                        message = " got deflected by "
                    elif result == 4:
                        if self.__animals_mated(org):
                            message = " mated with "
                        else:
                            message = " tried to mate with "

                    self.__logs.append(tk.Label(self.__logs_panel, text=cords + type(org).__name__ + message + type(other).__name__))

        for i in range(len(self.__logs)):
            self.__logs[i].grid(row=i, column=0)

        if org_s_flag:
            self.__organisms.sort(key=lambda organ: organ.initiative, reverse=True)
        self.__draw()

    def populate(self):
        x = 1
        y = 0
        self.__organisms.append(Human(0, 0))

        for i in range(self.sym_width * self.sym_height - 1):
            n = random.randint(0, 60)

            if n == 0:
                self.__organisms.append(Sheep(x * self.box_size, y * self.box_size))
            elif n == 1:
                self.__organisms.append(Wolf(x * self.box_size, y * self.box_size))
            elif n == 2:
                self.__organisms.append(Fox(x * self.box_size, y * self.box_size))
            elif n == 3:
                self.__organisms.append(Antelope(x * self.box_size, y * self.box_size))
            elif n == 4:
                self.__organisms.append(Turtle(x * self.box_size, y * self.box_size))
            elif n == 5:
                self.__organisms.append(Grass(x * self.box_size, y * self.box_size))
            elif n == 6:
                self.__organisms.append(Nightshade(x * self.box_size, y * self.box_size))
            elif n == 7:
                self.__organisms.append(Guarana(x * self.box_size, y * self.box_size))
            elif n == 8:
                self.__organisms.append(Dandelion(x * self.box_size, y * self.box_size))
            elif n == 9:
                self.__organisms.append(PineBorscht(x * self.box_size, y * self.box_size))
            elif n == 10:
                self.__organisms.append(CyberSheep(x * self.box_size, y * self.box_size))

            if x >= self.sym_width - 1:
                x = -1
                y += 1
            x += 1

        self.__organisms.sort(key=lambda org: org.initiative, reverse=True)
        for org in self.__organisms:
            org.action()

    def make_sprite(self, x, y, c):
        return self.__sym_panel.create_rectangle(x, y, x + self.box_size, y + self.box_size, fill=c)

    def make_move(self, organism, x, y):
        self.__sym_panel.coords(organism, x, y, x + self.box_size, y + self.box_size)

    def is_safe(self, x, y, strength):
        for org in self.__organisms:
            if org.x == x and org.y == y and org.strength > strength:
                return False
        return True

    def is_empty(self, x, y):
        if x < 0 or y < 0 or x > self.sym_width * self.box_size - self.box_size or\
                y > self.sym_height * self.box_size - self.box_size:
            return False

        for org in self.__organisms:
            if org.x == x and org.y == y:
                return False

        return True

    def kill(self, x, y):
        for org in self.__organisms:
            if org.x == x and org.y == y and isinstance(org, Animal) and not isinstance(org, CyberSheep):
                self.__logs.append(tk.Label(self.__logs_panel, text=str(org.x) + " " + str(org.y) + " " + type(org).__name__ + " got too close to pine borscht "))
                self.__sym_panel.delete(org.sprite)
                self.__organisms.remove(org)

    def __animals_mated(self, org):
        x = org.x + self.box_size
        y = org.y
        if self.is_empty(x, y):
            self.__organisms.append(type(org)(x, y))
            return True

        x -= self.box_size * 2
        if self.is_empty(x, y):
            self.__organisms.append(type(org)(x, y))
            return True

        x += self.box_size
        y += self.box_size
        if self.is_empty(x, y):
            self.__organisms.append(type(org)(x, y))
            return True

        y -= self.box_size * 2
        if self.is_empty(x, y):
            self.__organisms.append(type(org)(x, y))
            return True

        return False

    def __add_plant(self, org):
        direction = random.randint(0, 3)
        x = org.x
        y = org.y
        if direction == 0:
            x += self.box_size
        elif direction == 1:
            x -= self.box_size
        elif direction == 2:
            y += self.box_size
        elif direction == 3:
            y -= self.box_size

        if self.is_empty(x, y):
            self.__organisms.append(type(org)(x, y))
            # self.__organisms.sort(key=lambda organ: organ.initiative, reverse=True)

    def save(self):
        with open('objects.bin', 'wb') as file:
            pickle.dump(len(self.__organisms), file)
            for obj in self.__organisms:
                obj.save(file)

    def load(self):
        with open('objects.bin', 'rb') as file:
            length = pickle.load(file)
            self.pine.clear()
            for org in self.__organisms.copy():
                self.__sym_panel.delete(org.sprite)
                self.__organisms.remove(org)

            while length > 0:
                org_type = pickle.load(file)
                self.__organisms.append(globals()[org_type](0, 0))
                self.__organisms[-1].load(file)
                length -= 1
            self.__organisms.sort(key=lambda organism: organism.initiative, reverse=True)

        self.__draw()

    def printpos(self, event):
        x = math.floor((event.x_root - event.widget.winfo_rootx()) / 10) * 10
        y = math.floor((event.y_root - event.widget.winfo_rooty()) / 10) * 10

        popup = tk.Toplevel()
        popup.title("add organism")

        selected_value = tk.StringVar(value="Antelope")

        buttons = [(tk.Radiobutton(popup, text="Antelope", variable=selected_value, value="Antelope")),
                   tk.Radiobutton(popup, text="CyberSheep", variable=selected_value, value="CyberSheep"),
                   tk.Radiobutton(popup, text="Dandelion", variable=selected_value, value="Dandelion"),
                   tk.Radiobutton(popup, text="Fox", variable=selected_value, value="Fox"),
                   tk.Radiobutton(popup, text="Grass", variable=selected_value, value="Grass"),
                   tk.Radiobutton(popup, text="Guarana", variable=selected_value, value="Guarana"),
                   tk.Radiobutton(popup, text="Human", variable=selected_value, value="Human"),
                   tk.Radiobutton(popup, text="Nightshade", variable=selected_value, value="Nightshade"),
                   tk.Radiobutton(popup, text="Pine Borscht", variable=selected_value, value="PineBorscht"),
                   tk.Radiobutton(popup, text="Sheep", variable=selected_value, value="Sheep"),
                   tk.Radiobutton(popup, text="Turtle", variable=selected_value, value="Turtle"),
                   tk.Radiobutton(popup, text="Wolf", variable=selected_value, value="Wolf")]

        def on_select():
            selected_option = selected_value.get()
            if self.is_empty(x, y):
                self.__organisms.append(globals()[selected_option](x, y))
                self.__organisms.sort(key=lambda organ: organ.initiative, reverse=True)
            popup.destroy()

        # Create a button to trigger the selection
        select_button = tk.Button(popup, text="Select", command=on_select)

        for b in buttons:
            b.pack()
        select_button.pack()
