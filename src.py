import time

print("Enter your character's full name.")
name = input()

age = None 
    
print("Enter your character's age.")
def get_age():
    global age
    age = int(input())

    if age < 18:
        print("Your character can not be under 18. Please enter a valid age.")
        get_age()

get_age()


allowed_colors = [
    "Red",
    "Green",  
    "Blue"
]
chosen_color = None

def get_color():
    global allowed_colors
    global chosen_color

    chosen_color = input()

    if not chosen_color in allowed_colors:
        print("Please choose your character's favorite color out of the list of following options: " + str(allowed_colors))
        get_color()

print("Please choose your character's favorite color out of the list of following options: " + str(allowed_colors))
get_color()

for loop in range(10):
    print("Generating story... "  + str((loop/10)*100) + "%") 
    time.sleep(0.5)
print("Generating story... 100%")

print("Story generated:")

print("Once upon a time there was a lovely " + str(age) + " year old princess named " + name + ". But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a " + str.lower(chosen_color) + " castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but non prevailed. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss.")
