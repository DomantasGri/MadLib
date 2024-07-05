def nebututuscias(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("negali buti tuscias")

adj1 = nebututuscias("Adjective: ")
adj2 = nebututuscias("Adjective: ")
adj3 = nebututuscias("Adjective: ")
adj4 = nebututuscias("Adjective: ")
pluralNoun1 = nebututuscias("Plural noun: ")
pluralNoun2 = nebututuscias("Plural noun: ")
color = nebututuscias("Color: ")
clothingItem = nebututuscias("Clothing item: ")
verb1 = nebututuscias("verb ending with ing: ")
verb2 = nebututuscias("verb ending with ing: ")
noun = nebututuscias("noun: ")
number = nebututuscias("Number: ")
food = nebututuscias("type of food: ")
liquid = nebututuscias("liquid: ")

madlib = f"Today, my best friend and I decided to go to the {adj1} beach. We packed our {pluralNoun1} \
and wore our {color} {clothingItem}. The weather was {adj2}, \
perfect for {verb1} in the water. As soon as we arrived, we saw a {noun} \
building a {adj3} sandcastle. We joined in and added {pluralNoun2} to make it look even better. After that,\
we ate {number} {food} and drank {liquid}. It was a {adj4} day, and we had so much fun {verb2}!"

print (madlib)