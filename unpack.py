
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
import glob

df_dict = {}
start = 112
end = 115

CA_frames, NY_frames = [], []
CA_keys, NY_keys = [], []

CA_right_frames, NY_right_frames = [], []
CA_left_frames, NY_left_frames = [], []
CA_right_keys, NY_right_keys = [], []
CA_left_keys, NY_left_keys = [], []

for i in range(start, end+1):
	df = pd.read_csv('H{}_members.csv'.format(i))
	df = df[['bioname', 'dim1', 'state_abbrev', 'number_of_votes']]
	CA_frames.append(df.loc[df['state_abbrev'] == 'CA'].describe())
	CA_keys.append('H{}_CA_members'.format(i))
	NY_frames.append(df.loc[df['state_abbrev'] == 'NY'].describe())
	NY_keys.append('H{}_NY_members'.format(i))

all_df = pd.concat((CA_frames+NY_frames), keys=(CA_keys+NY_keys))
all_df.to_excel('data.xlsx')

for i in range(start, end+1):
	df = pd.read_csv('H{}_members.csv'.format(i))
	df = df[['bioname', 'dim1', 'state_abbrev', 'party_code']]

	df_R = df.loc[df['party_code'] == 200]
	df_R_CA = df_R.loc[df['state_abbrev'] == 'CA']
	CA_right_frames.append(df_R_CA.describe())
	CA_right_keys.append('H{}_CA_R_members'.format(i))
	df_R_NY = df_R.loc[df['state_abbrev'] == 'NY']
	NY_right_frames.append(df_R_NY.describe())
	NY_right_keys.append('H{}_NY_R_members'.format(i))

	df_L = df.loc[df['party_code'] == 100]
	df_L_CA = df_L.loc[df['state_abbrev'] == 'CA']
	CA_left_frames.append(df_L_CA.describe())
	CA_left_keys.append('H{}_CA_L_members'.format(i))
	df_L_NY = df_L.loc[df['state_abbrev'] == 'NY']
	NY_left_frames.append(df_L_NY.describe())
	NY_left_keys.append('H{}_NY_L_members'.format(i))

all_pol_df = pd.concat(CA_right_frames+CA_left_frames+NY_right_frames+NY_left_frames, keys=CA_right_keys+CA_left_keys+NY_right_keys+NY_left_keys)
all_pol_df.to_excel('pol.xlsx')