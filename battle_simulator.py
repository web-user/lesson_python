import time
import itertools
import datetime

class BaseWeapon:

    def __init__(self):
        self.time_history = 0
        self.count_ammo = 1
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
            enemy.hit_points = enemy.hit_points - self.damage

    def recharge(self):
        self.count_ammo -= 1
        if self.count_ammo == 0:
            # the number of cartridges, when you need to recharge
            self.count_ammo = self.magazine_size -1
        print(self.count_ammo)


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

for item_enemy in array_enemy:
    while item_enemy.is_alive:
        for item_weapon in array_weapon:
            item_weapon.shoot(item_enemy)
            item_weapon.recharge()
            print(item_enemy.hit_points)
            print('--------------------------------------------')
