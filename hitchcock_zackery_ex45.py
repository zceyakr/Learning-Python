from random import randint

code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
correct_lever = randint(1,5)

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('win')
        print("""
*Radio static* Good morning Agent 47. Your mission is to infiltrate and assassinate the well know evil mastermind known as Lexx Diablo. We have gotten intel that he has been in hiding in a warehouse near your current location. You have been equipped with our state-of-the-art knife. Keep it quiet, we do not want you drawing any unnecessary attention in there. We are counting on you 47, don’t let us down. *Radio static*
You sneak up to the secret base and make your way inside.
         """)

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    message = [
        "Would you look at that, you are dead. How surprising.",
        "Good Job. You are dead.",
        "Why did you even become an Agent? You are dead.",
        "In the final moments of your life you think to yourself, did I leave the stove on?. You are dead."
    ]

    def enter(self):
        print(Death.message[randint(0, len(self.message)-1)])
        exit(1)

class Captured(Scene):

    message = [
        "You are now forever their prisoner. At least you are not dead.",
        "You failed your mission. You are captured",
        "Why did you even become an Agent? You are captured.",
        "You are now a prisoner for the rest of your life. You sometimes think it would have been better if you just dead."
    ]

    def enter(self):
        print(Captured.message[randint(0, len(self.message)-1)])
        exit(1)

class LeverDeath(Scene):

    message = [
        "As the door opens a heard of elephants are released trampling you to death. Your last thought before you were squished was “Is that an elephant!?” You are dead.",
        "You failed your mission. You are captured",
        "Why did you even become an Agent? You are captured.",
        "You are now a prisoner for the rest of your life. You sometimes think it would have been better if you just dead."
    ]

    def enter(self):
        print(LeverDeath.message[randint(0, len(self.message)-1)])
        exit(1)

class BaseEntrance(Scene):

    def enter(self):
        print("""You are presented with three doors. Which way do you go?
        1: Go throught the left door?
        2: Go throught the center door?
        3: Go throught the right door?
        """)

        action = input("> ")

        if action == "1":
            print("""You decide to enter the door on the left.
Upon entering the room the are spotted by several guards and are then shot repeatedly.
            """)

            return 'death'

        elif action == "2":
            print("You decide to enter the center door.")

            return 'fake_treasure_room'

        elif action == "3":
            print("You decide to enter the door on the right.")

            return 'first_enemy_action_1'

        else:
            print("You continue to ponder your choices")

            return 'base_entrance'

class FakeTreasureRoom(Scene):

    def enter(self):
        print("""As you enter the room you see a huge pile of gold sitting on to of a pedestal. Do you:
        1: Take the gold.
        2: Leave the room.
        3: Look around.
        """)

        action = input("> ")

        if action == "1":
            print("Blinded by the wealth you take the gold, you rush over and start stuffing your pockets. It turns out that the gold was trapped! You are suddenly locked in the room and killed by a poisonous gas.")

            return 'death'

        elif action == "2":
            print("“This must be a trap” you think to yourself as you leave the room.")

            return 'base_entrance'

        elif action == "3":
            print(f"You look around the room and spot a golden plaque that tells you there are {code} pieces of gold on this pedestal.")


            return 'fake_treasure_room'

        else:
            print("You stare at the pile of gold.")

            return 'fake_treasure_room'

class FirstEnemyAction1(Scene):

    def enter(self):
        print("""As you enter you spot a soldier standing there. You need to act quick before he sees you! Do you:
        1: attack?
        2: hide?
        3: look around?
        """)

        action = input("> ")

        if action == "1":
            print("You rush the soldier trying to stab him with your knife. He shoots you before you could get close to him.")

            return 'death'

        elif action == "2":
            print("You quickly dash behind the nearest table. The soldier gets alerted by this and starts to investigate the sound.")

            return 'first_enemy_action_2'

        if action == "3":
            print("As you look around for a better option you get spotted and shot.")

            return 'death'
        else:
            print("Unable to react, you get spotted and shot.")

            return "death"

class FirstEnemyAction2(Scene):

    def enter(self):
        print("")

        action = input("> ")

        if action == "1":
            print("""As the soldier grows closer, you take this time to strike! Jumping up from behind the table and lunging your knife into his neck killing him instantly.
After that ordeal you decide you need more protection and make your way to the weapons locker.
            """)

            return 'weapon_room'

        elif action == "2":
            print("Knowing the soldier is getting closer, you decide you are in the best possible position. That is until the soldier spots you and opens fire on you")

            return 'death'

        elif action == "3":
            print("Franticly looking around for a way out of this situation the soldier spots and captures you.")

            return 'captured'

        else:
            print("You are immobilized with fear and get captured")

            return "captured"

class WeaponRoom(Scene):

    def enter(self):
        print("""Now standing in front of the weapons locker, the only thing in your way from protection is a golden keypad.
You need to guess the 3 digit combonation to the golden keypad.
""")

        guess = input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 10:
            print(f"BZZZZEDDD! Guess ({guesses}/10)")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("By pure luck or through some prior knowledge, you manage to open the door to the weapons locker")

            return 'pick_your_weapon'
        else:
            print(f"BZZZZEDDD! Guess ({guesses}/10) The alarm goes off and you are swarmed by enemies. Without a gun to defend yourself they shoot you.")

            return 'death'

class PickYourWeapon(Scene):

    def enter(self):
        print("""This is the room where the player can pick a weapon they want
        1: pick up the shotgun?
        2: pick up the suppressed pistol?
        3: look around?
        """)

        action = input("> ")

        if action == "1":
            print("You pick the first weapon")

            return 'death'

        elif action == "2":
            print("You pick the second weapon")

            return 'second_enemy'

        elif action == "3":
            print("you find the lever code")

            return 'death'

        else:
            print("someone spots you")
            return "death"

class SecondEnemy(Scene):

    def enter(self):
        print("""As you enter the room the guard spots you and is drawing his pistol! You need to do something fast! Do you:
        1: attack?
        2: dodge?
        3: look around?
        """)

        action = input("> ")

        if action == "1":
            print("Quicker than the human eye, you manage to draw your pistol and put one bullet stight")

            return 'boss_door'

        elif action == "2":
            print("With your ninja skills you manage to dodge his first shot, too bad you couldn't do the same the second shot he took...")

            return 'death'

        if action == "3":
            print("Instead of doing anything you decide to look around and get shot")

            return 'death'
        else:
            print("Unable to react fast enough you get shot.")

            return "death"

class BossDoor(Scene):

    def enter(self):
        print("You rush through the ship desperately trying to make it to")

        guess = input("[lever #]> ")


        if int(guess) != correct_lever:
            print(f"Without thinking you quickly pull lever number {guess}")

            return 'lever_death'
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
        'first_enemy_action_1': FirstEnemyAction1(),
        'first_enemy_action_2': FirstEnemyAction2(),
        'weapon_room': WeaponRoom(),
        'pick_your_weapon': PickYourWeapon(),
        'second_enemy': SecondEnemy(),
        'boss_door': BossDoor(),
        'boss_room': BossRoom(),
        'death': Death(),
        'captured': Captured(),
        'lever_death': LeverDeath(),
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
