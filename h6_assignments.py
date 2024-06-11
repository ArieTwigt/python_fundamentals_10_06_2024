# %% 1.

names_list = ['Pjtr', 'Jim', 'John', 'Marc', 'Danny', 'Peter']
vowels_list = ['a', 'e', 'o', 'u', 'i', 'y']

names_list_new = []

#%%
for name in names_list:
    for letter in name:
        if letter in vowels_list:
            name_new = name.replace(letter, "")

    names_list_new.append(name_new)


#%%
names_list_new

# %%
