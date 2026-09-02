input_vector = []
#input vector = [dnd_experience, magic_theming, melee, ranged, damage, support, enemy_manipulation, complexity, spellcasting]

print("Welcome to DND character creation assistant. This should help you in choosing a character to play in your DND game.\n" \
"Based on your answers, we can recommend you a class to start with for your DND game. Please type your name:")
name = input()

def q1():
    print(f"Hello {name}. We will now begin the questionaire. Firstly, have you played DND before or have any knowledge about DND? Please enter the associated number.\n"

        "1. I have never played DND and know nothing about DND.\n"

        "2. I have never played DND but I know a little bit about DND.\n" 

        "3. I have played once or twice or have some knowledge about DND.\n" 

        "4. I have played DND a few times and have some knowledge about DND.\n" 

        "5. I have played DND many times, and know everything about DND.\n" 
      )
    dnd_knowledge = int(input())
    if 1<= dnd_knowledge <= 5:
        input_vector.append(dnd_knowledge)
    return dnd_knowledge

def q2():
    magic_theming = input()
    return magic_theming


q1_a = q1() #dnd experience input




