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

# %% 2. 
import datetime

#%% define the date of today
date_today = datetime.date.today()

#%% specify the number of days to increase
num_days = 1
max_days = 10

while num_days <= max_days:
    new_date = date_today + datetime.timedelta(days=num_days)
    new_day = new_date.strftime("%A")
    print(new_day)

    num_days += 1


# %%
