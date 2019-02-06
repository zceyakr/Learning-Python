from random import randint

code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
gold = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
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
        "As the door opens you hear a turret starting up. Before you can get out of the way you get shot. You are dead.",
        "After pulling the lever you hear a voice say “self-destruct sequence initiated.” Detonation in 5, 4, 3, 2, 1, ... *Boom* You are dead.",
        "After you pull the lever a trapdoor below you opens up and you fall into a pit of spikes. You are dead."
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
            print("This must be a trap” you think to yourself as you leave the room.")

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
        print("""As the soldier is now approaching to your hiding spot you must act quick. Do you:
        1: attack?
        2: stay hiding?
        3: look around?
        """)

        action = input("> ")

        if action == "1":
            print("""As the soldier is now within arms reach, you take this time to strike! Jumping up from behind the table and lunging your knife into his neck killing him instantly.
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
            print(f"BZZZZEDDD! Guess ({guesses}/10)The alarm goes off and you are swarmed by enemies. Without a gun to defend yourself they shoot you.")

            return 'death'

class PickYourWeapon(Scene):

    def enter(self):
        print("""Upon entering the weapons locker, you spot two weapon racks. On one rack there is a very powerful yet loud shotgun and on the other is a not as powerful suppressed pistol, but at least it is quiet.
        1: pick up the shotgun?
        2: pick up the suppressed pistol?
        3: look around?
        """)

        action = input("> ")

        if action == "1":
            print("You pick up the shotgun from the rack and then hear someone from behind you. As you turn around you spot two guards. You quickly fire your shotgun taking both of them out in one shot but alerting the rest of them in the process. You manage to hold your ground for as long as you can until you run out of ammo and get forced to surrender.")

            return 'captured'

        elif action == "2":
            print("You pick up the suppressed pistol from the rack and then hear someone from behind you. As you turn around you spot two guards. You quickly fire one bullet into each of the guards killing them. You managed to not alert the rest of the base due to you having a suppressor on your weapon.")

            return 'second_enemy'

        elif action == "3":
            print(f"As you look around the room you find a hidden peice of paper that says level = {correct_lever}")

            return 'pick_your_weapon'

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
            print("Quicker than the human eye, you manage to draw your pistol and put one bullet straight between his eyes.")

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
        print("You manage to make it to the last known location of Lexx Diablo. Now the only thing in your way is finding out the correct lever to pull. ")

        guess = input("[lever #]> ")


        if int(guess) != correct_lever:
            print(f"Without thinking you quickly pull lever number {guess}")

            return 'lever_death'
        else:
            print("By pure luck or through some prior knowledge, you manage to pull the correct lever. Now there all you have to do is confront Lexx Diablo.")
            not_there = randint(1,100)
            if not_there == 1:
                return 'to_be_continue'
            else:
                return 'boss_room_action_1'

class BossRoomAction1(Scene):

    def enter(self):
        print("""As you enter the room you make eye contact with Lexx Diablo. This is it, the final battle. Only one of you are leaving this room alive. As soon as he recognizes you, he immediately pulls out a shotgun and aims it at your head. Do you:
        1: attack?
        2: hide?
        3: dodge?
        """)

        action = input("> ")

        if action == "1":
            print("You draw you gun as fast as you can, but you are unable to draw faster than the mighty Lexx Diablo can fire.")

            return 'death'

        elif action == "2":
            print("You quickly flip the nearest table and hide behind it as Lexx Diablo fires. While the table was able to withstand the shotgun blast it is uncertain how much more the table can withstand.")

            return 'boss_room_action_2'

        elif action == "3":
            print("You try to jump out of the way of the shotgun spread, but alas the spread on the shotgun is just too large. You get injured and start to beg for mercy as Lexx Diablo fires another shot into your skull.")

            return 'death'
        else:
            print("Unable to react fast enough you get shot.")

            return "death"

class BossRoomAction2(Scene):

    def enter(self):
        print("""As you take a moment to catch your breath from that action you hear what sounds like an engine revving up and begin to panic. Do you:
        1: attack?
        2: hide?
        3: dodge?
        """)


        action = input("> ")

        if action == "1":
            print("As a first instinct, you pop up from the table and ready your gun. To your surprise you see Lexx Diablo standing there with a minigun and are welcomed with hundreds of bullets entering your chest.")

            return 'death'

        elif action == "2":
            print("Not knowing what weapon Lexx Diablo was using, you decide to remain hiding behind the fragile table. The table was no match for the bullet rain from his minigun. The table and your body were shredded like paper.")

            return 'death'

        elif action == "3":
            print("After hearing what sounded like a minigun you decide the table was not safe. You quickly dodge rolled past the table as Lexx Diablo is indeed using a minigun to try to kill you.")

            return 'boss_room_action_3'
        else:
            print("Unable to react fast enough you get shot.")

            return "death"

class BossRoomAction3(Scene):

    def enter(self):
        print("""After seeing what destruction the minigun can do, you need to decide what you are going to do next. Do you:
        1: attack?
        2: hide?
        3: dodge?
        """)


        action = input("> ")

        if action == "1":
            print("Taking advantage of the slow movement of the minigun, you quickly raise your weapon and take multiple shots at Lex Diablo. You manage to land a shot in his arm forcing him to drop the minigun and then quickly take another shot at his head killing him before he is able to pull out another weapon. With your mission now complete your only goal is to now escape.")

            return 'real_treasure_room'

        elif action == "2":
            print("You quickly jump behind another table to hide from the minigun. Sadly, there is no table in the world that can withstand the fire from a minigun. The table is soon destroyed along with your body.")

            return 'death'

        elif action == "3":
            print("As you continue to dodge the rain of bullets you trip over a chair and are forced to watch as death slowly came your way.")

            return 'death'
        else:
            print("Unable to react fast enough you get shot.")

            return "death"

class RealTreasureRoom(Scene):

    def enter(self):
        print("""As you enter the room you see a huge pile of gold sitting on to of a pedestal. Do you:
        1: Take the gold.
        2: Leave the room.
        3: Look around.
        """)

        action = input("> ")

        if action == "1":
            print(f"Now with Lexx Diablo dead you are free to take his riches and escape with {gold} gold and your life.")

            return 'win'

        elif action == "2":
            print("You thought that this gold just sitting here must be a trap, so you leve the room without taking any gold")

            return 'no_gold_win'

        elif action == "3":
            print("""As you look around you see a piece of paper laying on the ground. The paper reads "There is a 1% chance you get a secret ending." Not knowing what that means you ignore the paper.
            """)

            return 'real_treasure_room'

        else:
            print("You stare at the pile of gold.")

            return 'real_treasure_room'

class Win(Scene):

    def enter(self):
        print(f"You won! Good job. You escaped with {gold} gold")
        return 'win'

class NoGoldWin(Scene):

    def enter(self):
        print(f"You won! Good job.")
        exit()

class ToBeContinued(Scene):

    def enter(self):
        print("""
After entering the room and looking around for Lexx Diablo there is no sign of him. The only thing left in his room is a note on the table that reads:
    "I am sorry Agent 47, but Lexx Diablo is in another warehouse."

    The End?
""")
        exit()



class Map(object):

    scenes = {
        'base_entrance': BaseEntrance(),
        'fake_treasure_room': FakeTreasureRoom(),
        'real_treasure_room': RealTreasureRoom(),
        'first_enemy_action_1': FirstEnemyAction1(),
        'first_enemy_action_2': FirstEnemyAction2(),
        'weapon_room': WeaponRoom(),
        'pick_your_weapon': PickYourWeapon(),
        'second_enemy': SecondEnemy(),
        'boss_door': BossDoor(),
        'boss_room_action_1': BossRoomAction1(),
        'boss_room_action_2': BossRoomAction2(),
        'boss_room_action_3': BossRoomAction3(),
        'death': Death(),
        'captured': Captured(),
        'lever_death': LeverDeath(),
        'win': Win(),
        'no_gold_win': NoGoldWin(),
        'to_be_continue': ToBeContinued()
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
