def checkEmpty(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("can't be empty")

adj1 = checkEmpty("Adjective: ")
adj2 = checkEmpty("Adjective: ")
adj3 = checkEmpty("Adjective: ")
adj4 = checkEmpty("Adjective: ")
adj5 = checkEmpty("Adjective: ")
number = checkEmpty("Number: ")
animalPlural = checkEmpty("Animal plural: ")
typeFood = checkEmpty("type of food: ")
noun = checkEmpty("Noun: ")
bodyPart = checkEmpty("Body part: ")
verbING = checkEmpty("verb ending in ing: ")

madlib = f"Yesterday, my family and I went to the zoo to see the {adj1} animals.\
The first exhibit we visited had {number} {animalPlural} \
that were {verbING}. Next, we watched a {adj2} monkey swing from tree to tree.\
My favorite part was when the {adj3} elephant sprayed water with its {bodyPart}. We had lunch at the zoo café, where \
I ate a {adj4} {typeFood}. On our way out, we bought a {noun} as a souvenir. It was a {adj5} day at the zoo!"

print(madlib)