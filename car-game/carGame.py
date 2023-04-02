import tkinter as tk
import random
from PIL import Image, ImageTk

class CarGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.car = self.canvas.create_rectangle(225, 400, 275, 450, fill='red')
        self.car_x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.obstacle_list = []
        self.score = 0
        self.score_text = self.canvas.create_text(50, 25, text='Score: {}'.format(self.score), font=('Arial', 12), anchor='nw')
        self.speed = 2
        self.create_obstacle()
        self.update()

    def move_left(self, event):
        if self.car_x > -225:
            self.car_x -= 25
            self.canvas.move(self.car, -25, 0)

    def move_right(self, event):
        if self.car_x < 225:
            self.car_x += 25
            self.canvas.move(self.car, 25, 0)

    def create_obstacle(self):
        x = random.randint(50, 450)
        y = 0
        obstacle = self.canvas.create_rectangle(x, y, x+50, y+50, fill='green')
        self.obstacle_list.append(obstacle)
        self.master.after(2000, self.create_obstacle)

    def update(self):
        for obstacle in self.obstacle_list:
            self.canvas.move(obstacle, 0, self.speed)
            if self.canvas.coords(obstacle)[3] > 500 and obstacle in self.obstacle_list:
                self.obstacle_list.remove(obstacle)
                self.canvas.delete(obstacle)
                self.score += 1
                self.canvas.itemconfigure(self.score_text, text='Score: {}'.format(self.score))
        if self.check_collision():
            self.game_over()
        else:
            self.master.after(20, self.update)

    def check_collision(self):
        car_coords = self.canvas.coords(self.car)
        for obstacle in self.obstacle_list:
            obstacle_coords = self.canvas.coords(obstacle)
            if car_coords[0] < obstacle_coords[2] and car_coords[2] > obstacle_coords[0] and car_coords[1] < obstacle_coords[3] and car_coords[3] > obstacle_coords[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(250, 250, text='Game Over!\nYour score was {}.'.format(self.score), font=('Arial', 20), justify='center')

root = tk.Tk()
game = CarGame(root)
root.mainloop()
