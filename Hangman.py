#Yonadhan
#Hangman_Game
#9-9-23

my_file = open("words.txt","r")
data = my_file.read()
words = data.split("\n")
my_file.close()

from random import choice
word = choice(words)
print(word)

def predict():
    print("Welcome to Hangman!!!\n\n")
    for x in word:
        print(" _", end='')
    # Guess a letter
    life_chance = 6
    num_of_times = 0
    negative_words = []
    correct_prediction = []
    a=[]
    gameon = True
    while gameon:
        print("\n****************************************************\n")
        x = input("Guess a letter!\n")


        if x in word:
            correct_prediction.append(x)

            num_of_times = num_of_times + word.count(x)
            if num_of_times == len(word):
                print(word)

                return "victory!!!"
            for letter in word:
               if letter in correct_prediction:
                   print(letter,end="")
               else:
                   print("_",end="")

        else:
            life_chance -= 1
            print("life_chance:"+str(life_chance))
            if life_chance < 0:
                print("You are hanged!")
                return "Loss"
            negative_words.append(x)

        print("\nIncorrect words that you are predicted till now = ",negative_words)
        print("_______________________________________________________________\n")


print(predict())





