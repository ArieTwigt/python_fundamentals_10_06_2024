#%% conditional statement
age = 17

#%% indentation
if age > 18:
    print("Yes!")
else:
    print("No")

print("De rest van de code")

#%%
letters_list = ['a', 'b', 'c']
vowels = ('a', 'e', 'o', 'u', 'i', 'y')

# %%


letter = input("Insert letter:")

if letter in letters_list and letter in vowels:
    print('Letter already present, but is is a vowel')
    letters_list.append(letter)
elif letter in letters_list and letter not in vowels:
    print('Letter already present')
else:
    print(f"Adding letter {letter}")
    letters_list.append(letter)

print(letters_list)

# %%
max_donation = 100
donation_amount = 0

while donation_amount < max_donation:
    print("Adding donation")
    donation_amount += 1
    print(f"Donation amount = {donation_amount}")

print("Done")
# %%

age = 17
zoontje_baas = "No"
drank = "Bier"


if age > 18 and (zoontje_baas == "Yes" or drank == "Cola"):
    print("Yes")
else:
    print("No")
# %%
