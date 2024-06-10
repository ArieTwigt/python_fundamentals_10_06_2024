#%% Create a conditional statement that indicates if your name starts with an "A or not

#%% 
my_name = "arie"

if my_name[0].upper() == "A": # my_name[0] in "aA":
    print("Yes")
else:
    print("No")

# %% 2. 
import random
import string


# define the vowels
vowels = ('A', 'E', 'O', 'U', 'I', 'Y')
all_letters = string.ascii_uppercase
non_vowels = [letter for letter in all_letters if letter not in vowels ]

#%%

name = input("Insert name:")


if name[0].upper() in vowels:
    random_letter = random.choice(non_vowels)
    name = name.replace(name[0], random_letter)
else:
    random_letter = random.choice(vowels)
    name = name.replace(name[0], random_letter)

print(name)

#%% 3.

# %% Create a conditional statement that indicates if your age is between 18 and 68.
age = 34

if age > 18 and age < 68:
    print("Yes")
else:
    print("No")

# %%
age = 18

if 18 <= age <= 68:
    print("Yes")
else:
    print("No")
# %%
