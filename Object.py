import const
import math
import pygame

pygame.init()

class Objects:


    def __init__(self,x,y,Vx0,Vy0,mass, radius, color, name=""):
        self.x = x
        self.y = y
        self.Vx0 = Vx0
        self.Vy0 = Vy0
        self.mass = mass
        self.radius = radius
        self.color = color
        self.coordinates = []
        self.name = name


    def draw(self, window):
        x = self.x * const.SCALE + const.WIDTH/2
        y = self.y * const.SCALE + const.HEIGHT/2

        if len(self.coordinates) > 2:
            updated_points = []
            for point in self.coordinates:
                x,y = point
                x = x*const.SCALE + const.WIDTH/2
                y = y*const.SCALE + const.HEIGHT/2
                updated_points.append((x,y))
            pygame.draw.lines(window, self.color, False, updated_points)

        distance_text = const.FONT.render(f"{self.name}", 1, const.WHITE)
        window.blit(distance_text, (x - distance_text.get_width() / 2, y + distance_text.get_width() / 2))
        pygame.draw.circle(window, self.color, (x,y), self.radius*const.radius_scale)

    def update(self, objects):
        total_Fx = total_Fy = 0

        for object in objects:
            if object != self:
                temp_Fx, temp_Fy = self.attraction(object)
                if temp_Fy == 0 and temp_Fx == 0:
                    return
                total_Fx += temp_Fx
                total_Fy += temp_Fy

        self.Vx0 += total_Fx / self.mass * const.TIMESTAMP
        self.Vy0 += total_Fy / self.mass * const.TIMESTAMP

        self.x -= self.Vx0 * const.TIMESTAMP
        self.y -= self.Vy0 * const.TIMESTAMP
        self.coordinates.append((self.x, self.y))

    def fusion(self, larger, smaller):
        larger.mass += smaller.mass
        larger.radius += smaller.radius / 5
        const.all.remove(smaller)

    def attraction(self, foreign):
        foreign_x, foreign_y = foreign.x, foreign.y
        dx = self.x - foreign_x
        dy = self.y - foreign_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < (self.radius + foreign.radius)*0.05/const.radius_scale or distance == 0:
            if self.mass > foreign.mass:
                self.fusion(self, foreign)
            else:
                self.fusion(foreign, self)
            return 0,0

        force = const.G * self.mass * foreign.mass / (distance**2)
        theta = math.atan2(dy, dx)
        Fx = force * math.cos(theta)
        Fy = force * math.sin(theta)

        return Fx, Fy
