import time
import itertools

class BaseWeapon:

    # how much health takes away from the opponent in case of a successful hit
    damage = 25
    # interval between shots in seconds
    shoot_interval = 0.9
    # chance of hitting
    hit_chance = 0.7
    # the number of cartridges, when you need to recharge
    magazine_size = 7
    # how long it takes to recharge in seconds
    reload_time = 2

    def shoot(self, enemy):
        # time.sleep(shoot_interval) 
        time.sleep(self.shoot_interval) 
        return enemy.hit_points - self.damage


class Shotgun(BaseWeapon):
    damage = 50
    shoot_interval = 1.5
    hit_chance = 0.9
    magazine_size = 6
    reload_time = 10


class AssaultRifle(BaseWeapon):
    damage = 15
    shoot_interval = 0.3
    hit_chance = 0.5
    magazine_size = 30
    reload_time = 3


class Enemy:
    def __init__(self, hit_points = 0):
        self.hit_points = hit_points

    @property
    def is_dead(self):
        if self.hit_points:
            return True
        else:
            return False


enemy_spotted = Enemy(200)
weapon = Shotgun()


array_enemy = []

for a in range(20):
    enemy_spotted = Enemy(200)
    array_enemy.append(enemy_spotted)

array_weapon = []

for b in range(2):
    weapon = Shotgun()
    array_weapon.append(weapon)

print(array_weapon)

list_objeect = [array_enemy, array_weapon]

size = weapon.magazine_size

for item_enemy, item_weapon in itertools.product(*list_objeect):
    while item_enemy.is_dead:
        step = item_weapon.shoot(item_enemy)
        print(step)
        item_enemy.hit_points = step
        size -= 1
        if size == 0:
            # the number of cartridges, when you need to recharge
            size = item_weapon.magazine_size -1
            # how long it takes to recharge in seconds
            time.sleep(item_weapon.reload_time) 
        print(size)
        print('--------------------------------------------')

