# 1. Create a dictionary with an (imaginary) person with attributes like his name, age and hobbies

#%%
hobbies = ['archery', 'reading']

dict_name = {'name': 'Frank', 
             'age': 57,
             'hobbies': hobbies}

# add a hobby to the list
dict_name['hobbies'].append('football')

# %%
dict_name



# %%
person_1 = {'name': 'Frank', 
             'age': 57,
             'hobbies': ['archery', 'reading']}

person_2 = {'name': 'James', 
             'age': 33,
             'hobbies': ['football', 'cycling']}

person_3 = {'name': 'Mary', 
             'age': 13,
             'hobbies': ['gaming']}

person_4 = {'name': 'Peter', 
             'age': 34,
             'hobbies': ['cooking', 'reading', 'programming']}

# %%
family_dict = {}

# %%
family_dict['name'] = 'Jones'
family_dict

# %%
family_dict['members'] = [person_1, person_2, person_3, person_4]
# %%
family_dict

# %%
family_dict.keys()
# %%
family_dict['name']
# %%
family_dict['members'][0]['hobbies'][1]

# %%

# %%
