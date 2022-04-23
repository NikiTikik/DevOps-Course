import random
from time import sleep

KNIGHT_HEALTH = 10
KNIGHT_ATTACK = 10
NUMBER_OF_KILLED_MONSTERS = 0


def stats_monitor():
    print("---------------------------------------------------")
    print("HEALTH", KNIGHT_HEALTH, "| ATTACK", KNIGHT_ATTACK, "| KILLED_MONSTERS", NUMBER_OF_KILLED_MONSTERS)
    sleep(1.5)


def monster():
    def fight_monster() -> int:
        global KNIGHT_HEALTH
        global KNIGHT_ATTACK
        global NUMBER_OF_KILLED_MONSTERS
        if monster_attack >= KNIGHT_HEALTH:
            print("The monster has torn you apart, GAME OVER")
            exit()
        elif KNIGHT_ATTACK >= monster_health:
            KNIGHT_HEALTH -= monster_attack
            NUMBER_OF_KILLED_MONSTERS += 1
            print(f"You won, but now you have {KNIGHT_HEALTH} points of health")
            return KNIGHT_HEALTH
        else:
            KNIGHT_HEALTH -= monster_attack
            print(f"This monster hurt you and you won't be able to kill him, "
                  f"now you have {KNIGHT_HEALTH} points of health")

    monster_health = random.randint(5, 30)
    monster_attack = random.randint(5, 30)

    text = input(f"It's a monster, it looks like it has {monster_health} points of health and {monster_attack} attack, "
                 "do you want to fight? Please enter \"1\" if you want to fight or \"2\" if you run away ")

    while (text != "1") and (text != "2"):
        text = input("Please enter \"1\" or \"2\"")

    if text == "1":
        fight_monster()


def apple() -> int:
    global KNIGHT_HEALTH
    apple_richness = random.randint(5, 30)
    KNIGHT_HEALTH += apple_richness
    print(f"You found an apple and ate it, it gave you {apple_richness} points of health", KNIGHT_HEALTH)
    return KNIGHT_HEALTH


def sword():
    def change_sword() -> int:
        global KNIGHT_ATTACK
        KNIGHT_ATTACK = new_sword
        return KNIGHT_ATTACK

    new_sword = random.randint(5, 30)
    text = input(f"You found a new sword, it has {new_sword} attack, "
                 "do you choose this one? Please enter \"1\" if you want to choose a new sword or \"2\" if not ")

    while (text != "1") and (text != "2"):
        text = input("Please enter \"1\" or \"2\"")

    if text == "1":
        change_sword()


print("Hello, you are a knight and life is a pain, you must survive!!!")
print("You can meet monsters in this dark wood, you have to kill 10 monsters. "
      "It will show your courage and will allow you to win the heart of a princess =)")

while NUMBER_OF_KILLED_MONSTERS != 10:
    stats_monitor()
    actions = monster, apple, sword
    new_action = random.choice(actions)
    new_action()

print("**************************************************************")
print("Yeah, VICTORY!!! now you can ask for the hand of a princess!!!")
print("**************************************************************")