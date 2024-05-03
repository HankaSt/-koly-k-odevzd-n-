"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Hana Stříbrná
email: stribrna.hana@gmail.com
discord: Hanka0531
"""

"""ověření uživatele"""
users= {
      "bob": "123",
      "ann": "pass123",
      "mike": "password123",
      "liz": "pass123"

}

user = input("user: ")
passw = input("password: ")

password = users.get(user)


if password == passw:
    print(
        "-" * 40,"\n"
        "Welcome to the app,", user,"\n"
        "We have 3 texts to be analyzed.\n",
        "-" * 40
    )
else:
    print("unregistered user, terminating the program.")
    quit()


"""texty v seznamu, spočítat kolik jich tam je, vybrat minimální a maximální hodnotu indexu, 
aby mohly být texty do proměnné přidávány/odebírány"""


Texts = (
"""Situated about 10 miles west of Kemmerer,
fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""", 
"""
          At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""
          The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""")

chosen_text = input("Enter a number between 1 and {} to select: ".format(len(Texts)))

print("-" * 40)
if chosen_text.isnumeric() == False:
    print("Not a number, program finished.") 
    quit()

chosen_index = int(chosen_text)
if chosen_index not in range(1, len(Texts) + 1):
    print("Not a valid number, program finished.")
    quit()


"""statistika"""

chosen_text_clean = (Texts[chosen_index - 1].strip().split())
titlecase = []
uppercase = 0
lowercase = 0
number = 0
numeric_sum = 0

for i in chosen_text_clean:
    if i.istitle():
        titlecase.append(i)
    if i.isupper() and i.isalpha():
        uppercase += 1
    if i.islower() and i.isalpha():
        lowercase += 1
    if i.isnumeric() and i.isdigit():
        number += 1
    if i.isdigit():
        numeric_sum += int(i)


titlecase_count = len(titlecase)
count_words = len(chosen_text_clean)

print("There are",count_words, "words in the selected text.")
print("There are", titlecase_count ,"titlecase words.")
print("There are:", uppercase, "uppercase words.")
print("There are:", lowercase, "lowercase words.")
print("There are:", number, "numeric strings.")
print("The sum of all the numbers", numeric_sum)


"""sloupcový graf"""

print(
        "-" * 40,"\n"
        "LEN|  OCCURENCES      |NR.""\n",
        "-" * 40
    )

word_length_count = {}

for word in chosen_text_clean:
    word_length = len(word)
    if word_length in word_length_count:
        word_length_count[word_length] += 1
    else:
        word_length_count[word_length] = 1

sorted_word_length_count = sorted(word_length_count.items())


for length, count in sorted_word_length_count:
    if length <= 9:
        print(length, " |", "*" * length, " "*(15-length), "|", count)
    else:
        print(length, "|", "*" * length, " "*(15-length), "|", count)

