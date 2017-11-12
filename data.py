
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
import glob
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages

start = 112
end = 115

with PdfPages('densities.pdf') as pdf:
	for i in range(start, end+1):
		df = pd.read_csv('H{}_members.csv'.format(i))
		df = df.loc[df['state_abbrev'] == 'CA']
		df = df[['dim1']]
		df.plot(kind='density')
		pdf.savefig()
		plt.show()
		plt.close()

	for i in range(start, end+1):
		df = pd.read_csv('H{}_members.csv'.format(i))
		df = df.loc[df['state_abbrev'] == 'NY']
		df = df[['dim1']]
		df.plot(kind='density')
		pdf.savefig()
		plt.show()
		plt.close()