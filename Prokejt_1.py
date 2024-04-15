
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Hana Stříbrná
email: stribrna.hana@gmail.com
discord: Hanka0531
"""

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
    print ("unregistered user, terminating the program.")
    quit ()


text = ("1", "2", "3")
select_text = input("Enter a number btw. 1 and 3 to select: ")
print ("-" * 40)
if select_text.isnumeric () == False:
    print ("Not a number, program finished.") 
    quit ()
elif select_text not in text:
    print("Not a valid number, program finished.")
    quit ()


Text_1 =("""
         Situated about 10 miles west of Kemmerer,
fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""
    )
Text_2 = ("""
          At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick."""
          )
Text_3 = ("""
          The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""")



text = int(select_text)
titlecase = []

if text == 1:
    words = Text_1.strip().split()
    for title in Text_1:
        if title.istitle ():
            titlecase.append(title)
        else:
            continue


elif text == 2:
    words = Text_2.strip().split()
    for title in Text_2:
        if title.istitle ():
            titlecase.append(title)
        else:
            continue


else:
    words = Text_3.strip().split()
    for title in Text_3:
        if title.istitle ():
            titlecase.append(title)
        else:
            continue



count_words = len(words)
print ("There are",count_words, "words in the selected text.")

titlecase_count = len(titlecase)
print ("There are", titlecase_count, "titlecase words.")


all_titlecase = ' '.join(words).split()


uppercase = 0
for hovno in all_titlecase:
    if hovno.isupper() and hovno.isalpha():
        uppercase += 1
print ("There are:", uppercase, "uppercase words.")

lowercase = 0
for lower in all_titlecase:
    if lower.islower() and lower.isalpha():
        lowercase += 1
print ("There are:", lowercase, "lowercase words.")

number = 0
for numer in all_titlecase:
    if numer.isnumeric() and numer.isdigit():
        number += 1
print ("There are:", number, "numeric strings.")

numeric_sum = 0
for prase in all_titlecase:
    if prase.isdigit():
        numeric_sum += int(prase)
print ("The sum of all the numbers", numeric_sum)


print(
        "-" * 40,"\n"
        "LEN|  OCCURENCES      |NR.""\n",
        "-" * 40
    )


word_length_count = {}

for word in all_titlecase:
    word_length = len(word)
    if word_length in word_length_count:
        word_length_count[word_length] += 1
    else:
        word_length_count[word_length] = 1

sorted_word_length_count = sorted(word_length_count.items())


for length, count in sorted_word_length_count:
    if length <= 9:
        print (length, " |", "*" * length, " "*(15-length), "|", count)
    else:
        print (length, "|", "*" * length, " "*(15-length), "|", count)