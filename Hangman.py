import random
import turtle

animals = ["Shark", "Rhinoceros", "Hippopotamus", "Turtle", "Bear", "Leopard", "penguin", "Tuna", "Beluga", "Jaguar", "Bison", "Wolf", "Whale", "Dolphin", "Narwhal", "Pronghorn", "Kangaroo", "Porpoise", "Elephant", "Gorilla", "Pangolin", "Seal", "Sloth", "elephant", "Orangutan", "Saola", "Tiger", "Vaquita", "ferret", "Bonobo", "Chimpanzee", "Panda", "Monkey", "Dugong", "Tortoise", "Rabbit", "Kitten", "Mouse", "Hamster", "Rabbit", "Duck", "Goat", "Crab", "Deer", "Sheep", "Fish", "Turkey", "Dove", "Chicken", "Horse", "Hawk", "Eagle", "Goose", "Squirrel", "Lion", "Panda", "Walrus", "Otter", "Mouse", "Goat", "Horse", "Monkey", "Koala", "Mole", "Elephant", "Leopard", "Hippopotamus", "Giraffe", "Hedgehong", "Sheep", "Deer", "Woodpecker", "Camel", "Koala", "Alligator", "Tiger", "Bear", "Coyote", "Chimpanzee", "Raccoon", "Lion", "Crocodile", "Dolphin", "Elephant", "Squirrel", "Snake", "Kangaroo", "Gorilla", "Hare", "Toad", "Frog", "Deer", "Badger", "Lizard", "Mole", "Hedgehog", "Otter", "Reindeer", "lemur"]

geography = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Comoros", "Croatia", "Cuba", "Cyprus", "Denmark", "Djibouti", "Dominica", "Ecuador", "Egypt", "Eritrea", "Estonia", "Swaziland", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Nicaragua", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Samoa", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia", "Somalia", "Spain", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "England", "Wales", "Scotland", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", "Kabul", "Tirana", "Algiers", "Luanda", "Yerevan", "Canberra", "Vienna", "Baku", "Nassau", "Manama", "Dhaka", "Bridgetown", "Minsk", "Brussels", "Sarajevo", "Gaborone", "Brasilia", "Sofia", "Gitega", "Praia", "Ottawa", "Bangui", "Santiago", "Beijing", "Bogota", "Moroni", "Kinshasa", "Zagreb", "Havana", "Nicosia", "Prague", "Copenhagen", "Roseau", "Quito", "Cairo", "Asmara", "Tallinn", "Suva", "Helsinki", "Paris", "Tbilisi", "Berlin", "Accra", "Athens", "Bissau", "Georgetown", "Budapest", "Reykjavik", "Jakarta", "Tehran", "Baghdad", "Dublin", "Jerusalem", "Rome", "Kingston", "Tokyo", "Amman", "Nairobi", "Tarawa", "Pristina", "Bishkek", "Vientiane", "Riga", "Beirut", "Maseru", "Monrovia", "Tripoli", "Vaduz", "Vilnius", "Bamako", "Valletta", "Monaco", "Ulaanbaatar", "Podgorica", "Rabat", "Maputo", "Naypyidaw", "Windhoek", "Kathmandu", "Amsterdam", "Wellington", "Managua", "Niamey", "Abuja", "Pyongyang", "Skopje", "Oslo", "Muscat", "Islamabad", "Ngerulmud", "Jerusalem", "Lima", "Manila", "Warsaw", "Lisbon", "Doha", "Bucharest", "Moscow", "Kigali", "Basseterre", "Castries", "Kingstown", "Apia", "Riyadh", "Dakar", "Belgrade", "Victoria", "Singapore", "Bratislava", "Ljubljana", "Honiara", "Mogadishu", "Seoul", "Juba", "Madrid", "Khartoum", "Paramaribo", "Stockholm", "Bern", "Damascus", "Taipei", "Dushanbe", "Dodoma", "Bangkok", "Dili", "Tunis", "Ankara", "Kampala", "London", "Montevideo", "Tashkent", "Caracas", "Hanoi", "Lusaka", "Harare", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "Wisconsin", "Wyoming"]

english_words = ["happy", "agency", "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "beekeeper", "bikini", "blizzard", "bookworm", "buffalo", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "crypt", "cycle", "daiquiri", "disavow", "dizzying", "duplex", "embezzle", "equip", "espionage", "exodus", "faking", "fishhook", "fixable", "fjord", "flopping", "fluffiness", "frazzled", "frizzled", "fuchsia", "funny", "galaxy", "galvanize", "gazebo", "gizmo", "glowworm", "gnarly", "gossip", "grogginess", "hyphen", "icebox", "injury", "ivory", "jackpot", "jaywalk", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "keyhole", "khaki", "kilobyte", "kiosk", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mystify", "onyx", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "psyche", "puppy", "puzzling", "quartz", "queue", "quiz", "rhubarb", "rhythm", "scratch", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "stretch", "stronghold", "subway", "syndrome", "topaz", "transcript", "transgress", "transplant", "twelfth", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vortex", "walkway", "waltz", "wheezy", "whizzing", "whomever", "wizard", "woozy", "wristwatch", "xylophone", "yachtsman", "youthful", "zigzag", "zipper", "zombie", "administration", "admit", "adult", "against", "agency", "agreement", "economic", "edge", "education", "effort","election", "employee", "general", "generation", "glass","government", "greet", "think", "paint", "teacher", "student", "bank", "washer", "dancer", "singer", "soccer", "tennis", "division", "rushes", "brush", "zebra", "elephant"]

tiptup = turtle.Turtle()
# This is the gallow turtle
tiptup.right(150)
tiptup.penup()
tiptup.forward(225)
tiptup.pendown()
tiptup.right(30)
tiptup.forward(50)
tiptup.backward(100)
tiptup.forward(50)
tiptup.right(90)
tiptup.forward(250)
tiptup.right(90)
tiptup.forward(75)
tiptup.right(90)
tiptup.forward(40)
tiptup.hideturtle()

pipsy = turtle.Turtle()
# this is the fill in the word turtle
pipsy.penup()
pipsy.backward(150)
pipsy.right(50)
pipsy.forward(150)
# pipsy.pendown()
pipsy.hideturtle()
# print(pipsy.position()[0], pipsy.position()[1])

lyly = turtle.Turtle()
# this is the wrong letter turle
lyly.color("red")
lyly.penup()
lyly.backward(75)
lyly.left(60)
lyly.forward(100)
lyly.right(60)
lyly.hideturtle()

ginny = turtle.Turtle()
# this is the wrong word turtle
ginny.color("red")
ginny.penup()
ginny.backward(75)
ginny.left(55)
ginny.forward(75)
ginny.right(55)
ginny.hideturtle()


all_guesses = []
# this list stores all previous guesses to be used to prevent people from guessing same letter or word more than once

def welcome():
  # basic instructions and setting up game with theme
  print("Welcome to Hangman!")
  print()
  print("You have 6 tries to either guess a letter or guess the word. If you guess the complete word in 6 tries then you win!")
  print()

  print("Which theme would you like to play?")

  theme = "1"
  mystery_word = ""
  
  while theme not in "AGR":
    # this will promt for theme again if they don't select options available (A,G, or R)
    theme = input('Type "G" for Geography, "A" for animals, or "R" for random words >').upper()
    if theme == "G":
      mystery_word = random.choice(geography).lower()
    elif theme == "A":
      mystery_word = random.choice(animals).lower()
    elif theme == "R":
      mystery_word = random.choice(english_words).lower()
  return mystery_word


def hide_letters(mystery_word):
  # this function draws the blanks for the letters of mystery

  i = 0
  while i < len(mystery_word):
    pipsy.goto(-53+(i*25),-120)
    pipsy.write("_", font= ("calibri", 22, "normal"))
    i +=1



def play_move():
# this gets the letter or guessed word from user and returns it

  guess = ""
  letter = ""
  action = input('Guess a letter or guess the word. > ').lower()

  while action in all_guesses:
    action = input("That was already guessed, try a new letter or guess.> ").lower()

  if len(action) == 1:
    letter = action
    all_guesses.append(letter)

  if len(action) > 1:
    guess = action
    all_guesses.append(guess)

  return(letter, guess)



def draw_man(incorrect_guess, correct_letters):
# this is the function to draw the hangman after each incorrect guess

        if incorrect_guess == 0:
          # head
          tiptup.penup()
          tiptup.forward(50)
          tiptup.pendown()
          tiptup.right(270)
          tiptup.circle(25)

        elif incorrect_guess == 1:
          # body
          tiptup.right(90)
          tiptup.forward(50)

        elif incorrect_guess == 2:
          # arm 1
          tiptup.backward(35)
          tiptup.right(120)
          tiptup.forward(50)
          tiptup.backward(50)

        elif incorrect_guess == 3:
          # arm 2
          tiptup.right(120)
          tiptup.forward(50)
          tiptup.backward(50)
          tiptup.right(120)

        elif incorrect_guess == 4:
          # leg 1
          tiptup.forward(45)
          tiptup.right(60)
          tiptup.forward(60)
          tiptup.backward(60)
        
        elif incorrect_guess == 5:
          # leg 2
          tiptup.right(240)
          tiptup.forward(60)
          print("You lost")
          print(f"'{mystery_word}' was the mystery word")
          for i, missing_letter in enumerate(mystery_word):
            if missing_letter not in correct_letters:
              # this is used after player lost game to fill in the letters they didn't guess
              pipsy.color("red")
              pipsy.goto(-53+(i*25),-115)
              pipsy.write(missing_letter, font= ("calibri", 18, "normal"))



def check_mystery_word():

  incorrect_guess = 0
  correct_letters = []
  unguessed = list(mystery_word)

  while incorrect_guess < 6:
    letter, guess = play_move()

    if letter != "":
      # needed to add in because when they guess the word instead of letter the letter returns as a blank and prompts incorrect print statement
      if letter in mystery_word:
        print(f"{letter} is in mystery word")
        correct_letters.append(letter)
        for i, correct_letter in enumerate(mystery_word):
          if correct_letter == letter:
            pipsy.goto(-53+(i*25),-115)
            pipsy.write(letter, font= ("calibri", 18, "normal"))
            unguessed.remove(letter)
        if len(unguessed) == 0:
          print("you won")
          break

      elif letter not in mystery_word:
        print(f"{letter} not in mystery word")
        lyly.write(letter, font = ("calibri", 14, "normal"))
        lyly.forward(12)
        lyly.write(", ", font= ("calibri", 20, "normal") )
        lyly.forward(10)

        draw_man(incorrect_guess, correct_letters)

        incorrect_guess = int(incorrect_guess) + 1  

    if guess != "":
       # needed to add in because when they guess the letter instead of word the word returns as a blank and prompts incorrect print statement
      if guess == mystery_word:
        print(f"'{guess}' is the mystery word!")
        print("You won!")
        for i, missing_letter in enumerate(mystery_word):
          if missing_letter not in correct_letters:
            pipsy.goto(-53+(i*25),-115)
            pipsy.write(missing_letter, font= ("calibri", 18, "normal"))
        break

      if guess != mystery_word:
        print(f"{guess} was not the mystery word")
        ginny.write(guess, font = ("calibri", 15, "normal"))
        ginny.right(90)
        ginny.forward(25)
        ginny.left(90)

        draw_man(incorrect_guess, correct_letters)
    
      incorrect_guess = int(incorrect_guess) + 1


mystery_word = welcome()
hide_letters(mystery_word)
check_mystery_word()
