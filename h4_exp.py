#%% 
import os


#%%
files_folders = os.listdir()

# %%
os.path.isdir(".gitignore")
# %%
folders = [x
              for x 
              in files_folders
              if os.path.isdir(x)
              ]
folders

# %%
files = [x
              for x 
              in files_folders
              if os.path.isfile(x)
              ]
files
# %%
