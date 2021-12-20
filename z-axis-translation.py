# import numpy as np
import pandas as pd
from os import scandir, getcwd

park_path = 'C:/Users/marco/OneDrive - Universidade de Vigo/3I/Faro Focus/Workflow/for recap/Parking-no pipes/' #  directorio de trabajo
pipes_path = 'C:/Users/marco/OneDrive - Universidade de Vigo/3I/Faro Focus/Workflow/for recap/Pipes/'
rgb = [255, 170, 0] # objective colour

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

park_files = ls(park_path)
pipes_files = ls(pipes_path)

park_data = pd.DataFrame()
pipes_data = pd.DataFrame()

for file in park_files:
    txt = pd.read_csv(park_path + file, sep = ' ')
    park_data = pd.concat([park_data, txt])
    
for file in pipes_files:
    txt = pd.read_csv(pipes_path + file)
    pipes_data = pd.concat([pipes_data, txt])
    

park_data = park_data.dropna(subset=["Z"])
pipes_data = pipes_data.dropna(subset=["Z"])

park_data = park_data.drop(park_data.columns[[6, 7, 8, 9]], axis='columns')
pipes_data = pipes_data.drop(pipes_data.columns[[6, 7, 8, 9, 10]], axis='columns')


park_data.rename(columns={'//X':'X'}, inplace=True)
pipes_data.rename(columns={'//X':'X'}, inplace=True)

filtered_park_data = park_data[park_data.R.eq(rgb[0])&park_data.G.eq(rgb[1])&park_data.B.eq(rgb[2])]

z = filtered_park_data['Z'].median() # median for floor points
z_std = filtered_park_data['Z'].std()

new_park_data = park_data
new_pipes_data = pipes_data

new_park_data['Z'] -= z
new_pipes_data['Z'] -= z


new_park_data.to_csv(park_path + 'Filtered/parking-no-pipes-filtered.txt', 
                     header=['X', 'Y', 'Z', 'R', 'G', 'B'],index=None, sep=' ', mode='a')

new_pipes_data.to_csv(pipes_path + 'Filtered/parking-pipes-filtered.txt', 
                     header=['X', 'Y', 'Z', 'R', 'G', 'B'],index=None, sep=' ', mode='a')







