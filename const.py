from Object import *
pygame.init()


AU = 149.6e6 * 1000
SCALE = 200 / AU
radius_scale = AU * SCALE /20 / 696340 #km
G = 6.67428e-11
WIDTH, HEIGHT = 1450,850
HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT =  10,10
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N body simulation")
TIMESTAMP = 3600*24
FONT = pygame.font.SysFont("comicsans", 20)

WHITE = (255,255,255)
sun_color = (255,255,0)
earth_color = (100, 149, 237)
mars_color = (188, 39, 50)
mercury_color = (80, 78, 81)
jupiter_color = (216,202,157)
venus_color = (249,194,26)
saturn_color = (234,214,184)
uranus_color =  (79, 208, 231)

# solar system simulation
sun = Objects(x=0, y=0, Vx0=0, Vy0=0, mass=2 * 10 ** 30, radius=696340, color=sun_color, name="sun")
earth = Objects(x=1 * AU, y=0, Vx0=0, Vy0=29.8 * 1000, mass=5.972 * 10 ** 24, radius=6378.1, color=earth_color,name="earth")
mercury = Objects(x=0.387 * AU, y=0, Vx0=0, Vy0=47.36 * 1000, mass=0.33 * 10 ** 24, radius=2440,color=mercury_color, name="mercury")
jupiter = Objects(x=-4.95 * AU, y=0, Vx0=0, Vy0=-13.06 * 1000, mass=1898 * 10 ** 24, radius=71492,color=jupiter_color, name="jupiter")
venus = Objects(x=0.723 * AU, y=0, Vy0=35.02 * 1000, Vx0=0, mass=4.8673 * 10 ** 24, radius=6051.8,color=venus_color, name="venus")
mars = Objects(x=-1.524 * AU, y=0, Vy0=-24.07 * 1000, Vx0=0, mass=0.64169 * 10 ** 24, radius=227.956,color=mars_color, name="mars")
saturn = Objects(x=9.957 * AU, y=0, Vy0=9.68 * 1000, Vx0=0, mass=568.32 * 10 ** 24, radius=60268,color=saturn_color, name="saturn")
uranus = Objects(x=-19.8 * AU, y=0, Vy0=-6.8 * 1000, Vx0=0, mass=86.811 * 10 ** 24, radius=25559,color=uranus_color, name="uranus")
halley = Objects(x=0.587 * AU, y=0.2 * AU, Vx0=0, Vy0=50.6 * 1000, mass=2.2 * 10 ** 14, radius=11,color=(255, 255, 255), name="halley's comet")

all = []

# all = [sun, earth, mercury, jupiter, venus, mars, saturn, uranus, halley]




