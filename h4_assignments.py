# %% Assign a variable that holds the number of days until your next birthday


# %%
import datetime

#%%
today = datetime.date.today()

# %%
bday = datetime.date(2024, 12, 5)

# %%
delta = bday - today
# %%
delta
# %%
type(delta)
# %%
num_days = delta.days
num_days

# %% Calculate the surface of a circle with a diameter of 10 (radius^ * pi)

# %%

#%% 
from math import pi, pow

#%%
diameter = 10
radius = diameter / 2

size = pow(radius, 2) * pi
size

# %%
10 ^ 5
# %%


#%% 3. Calculate the surface of a circle with a diameter of 10 (radius^ * pi)

#%%
import os

#%%
files_folders = os.listdir()
files_folders

# %% Add a directory with the name our_functions
if not os.path.exists("our_functions"):
    os.mkdir("our_functions")

# %%
