#%%
names_list = ['Arie', 'James', 'Xander', 'Pieter']

#%%
for name in names_list:
    print(name)

    for idx, _ in enumerate(name):
        letters = name[idx:idx + 2]
        print(letters)



# %% populating empty lists based on a condition
ages_list = [13, 28, 45, 11, 8, 33]

#%%

ages_list_adult = []
ages_list_infant = []

for age in ages_list:
    if age > 18:
        ages_list_adult.append(age)
    else:
        ages_list_infant.append(age)

#%%
ages_list_adult
# %%
ages_list_infant

# %% list comprehension
ages_list_adult = [age  for age in ages_list if age >= 18 ]

ages_list_infante = [age  for age in ages_list if age < 18 ]

# %%
names_list = ['Gunter', 'Adolf', 'Frederick', 'Adolf','Christian', 'Adolf', 'Heindrich']

names_list_filtered = [name if name != 'Adolf' else 'Dirk' for name in names_list ]

names_list_filtered
# %%
