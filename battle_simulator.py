import time
import itertools
import datetime

class BaseWeapon:

    def __init__(self):
        self.time_history = 0
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
        # time.sleep(self.shoot_interval) 
        now_time = time.time()
        print(now_time - self.time_history, self.shoot_interval)
        if now_time - self.time_history >= self.shoot_interval:
            print('-------TIME--------')
            self.time_history = now_time
            return enemy.hit_points - self.damage
        return enemy.hit_points


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
    def is_alive(self):
        if self.hit_points != 0 or self.hit_points > 0:
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

size = weapon.magazine_size

counter = 0

for item_enemy in array_enemy:
    while item_enemy.is_alive:
        for item_weapon in array_weapon:
            print(item_weapon.shoot(item_enemy))
            item_enemy.hit_points = item_weapon.shoot(item_enemy)
            size -= 1
            if size == 0:
                # the number of cartridges, when you need to recharge
                size = item_weapon.magazine_size -1
                # how long it takes to recharge in seconds
                # time.sleep(item_weapon.reload_time) 
            print(size)
            print('--------------------------------------------')
