#%%
ages_list = [45, 23, 8, 11, 32]

#%%
sorted(ages_list)

# %%
ages_list.sort(reverse=True)
# %%
ages_list

# %% person dict

person_1 = {'name': 'James', 
            'age': 27}

# %%
hobbies = ['football', 'programming', 'reading']

person_1['hobbies'] = hobbies
# %%
person_1

# %%
person_1['hobbies'][1]


# %% using zip
properties = ['name', 'age', 'city']
values = ['arie', 34, 'Katwijk']

# %%
person = dict(zip(properties, values))
person
# %%
