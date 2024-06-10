#%% 1.
full_name = "Erling Haaland"


# %% a. 
full_name_new = full_name + " .Jr"
full_name_new

# %% b.
suffix = ".Jr"
full_name_new = f"{full_name} {suffix}"




# %% 2.a
full_name_replaced = full_name_new.replace("Erling", "E.")
full_name_replaced

# %% b. 
full_name_split = full_name_new.split(" ")
first_name = full_name_split[0]

full_name_split[0] = first_name[0] + "."
full_name_str = " ".join(full_name_split)
full_name_str

# %% 3a. "E. Haaland .Jr - Nationality: Norway"
nationality = "Norway"
sentence = full_name_str + " - Nationality: " + nationality
sentence

# %% b.
sentence = f"{full_name_str} - Nationality: {nationality}"
sentence


# %%
