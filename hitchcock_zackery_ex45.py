from random import randint

code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('win')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    message = [
        "Would you look at that, you are dead. How surprising.",
         "You are dead. Good Job.",
         "Why did you even become an explorer? You are dead.",
         "In the final moments of your life you think to yourself, did I leave the stove on?. You are dead."
    ]

    def enter(self):
        print(Death.message[randint(0, len(self.message)-1)])
        exit(1)

class BaseEntrance(Scene):

    def enter(self):
        print("You enter and there are three doors you can go through.")

        action = input("> ")

        if action == "1":
            print("There is something bad in here and you die")

            return 'death'

        elif action == "2":
            print("You go into the treasure room")
            print(f"There are {code} peices of gold on the table")

            return 'fake_treasure_room'

        elif action == "3":
            print("This is the main way to go")

            return 'first_enemy'

        else:
            print("DOES NOT COMPUTE!")
            return 'base_entrance'

class FakeTreasureRoom(Scene):

    def enter(self):
        print("A room with gold in it that is trapped.")

        action = input("> ")

        if action == "1":
            print("You take the gold and die")

            return 'death'

        elif action == "2":
            print("You leave the room")

            return 'base_entrance'

        elif action == "3":
            print("You look around")

            return 'fake_treasure_room'

        else:
            print("DOES NOT COMPUTE!")
            return 'fake_treasure_room'

class FirstEnemy(Scene):

    def enter(self):
        print("This is the room where the player will fight the first enemy")

        action = input("> ")

        if action == "1":
            print("You fail to kill the enemy")

            return 'death'

        elif action == "2":
            print("After you kill the enemy you go to the weapons room")

            return 'weapon_room'
        else:
            print("DOES NOT COMPUTE!")
            return "first_enemy"

class WeaponRoom(Scene):

    def enter(self):
        print("The code is 3 digit.")
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The door opens to the weapon room")

            return 'pick_your_weapon'
        else:
            print("The alarm goes off and you are swarmed by enemies without a weapon and they shoot you.")

            return 'death'

class PickYourWeapon(Scene):

    def enter(self):
        print("This is the room where the player can pick a weapon they want")

        action = input("> ")

        if action == "1":
            print("You pick the first weapon")

            return 'second_enemy'

        elif action == "2":
            print("You pick the second weapon")

            return 'second_enemy'
        else:
            print("DOES NOT COMPUTE!")
            return "pick_your_weapon"

class SecondEnemy(Scene):

    def enter(self):
        print("You rush through the ship desperately trying to make it to")


        good_pod = randint(1,1)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(f"You jump into the bad pod {guess} and are now mush.")

            return 'death'
        else:
            print(f"You jump into pod {guess} and hit the eject button.")

            return 'boss_room'

class BossRoom(Scene):

    def enter(self):
        print("This is the room where you fight the boss")


        action = input("> ")

        if action == "1":
            print("You do something")

            return 'death'

        elif action == "2":
            print("You do something")

            return 'win'
        else:
            print("DOES NOT COMPUTE!")
            return "boss_room"

class Win(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'win'

class Map(object):

    scenes = {
        'base_entrance': BaseEntrance(),
        'fake_treasure_room': FakeTreasureRoom(),
        'first_enemy': FirstEnemy(),
        'weapon_room': WeaponRoom(),
        'pick_your_weapon': PickYourWeapon(),
        'second_enemy': SecondEnemy(),
        'boss_room': BossRoom(),
        'death': Death(),
        'win': Win(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('base_entrance')
a_game = Engine(a_map)
a_game.play()
