import pandas as pd
import os, sys

def main():
	# change the working directory
	os.chdir(ipath)
	# read in the trips
	trips = pd.read_csv(ifile, header=0)
	# define fields to group by
	groupbyFields = ['start station id', 'start station name', 'start station latitude', 'start station longitude', 'end station id', 'end station name', 'end station latitude', 'end station longitude']
	# get the counts and total_duration
	ods = pd.DataFrame({
		'count' : trips.groupby(groupbyFields).size(), 
		'total_duration': trips.groupby( groupbyFields)['tripduration'].sum()
		}).reset_index()
	# write the file out
	ods.to_csv(ofile)

if __name__ == '__main__':
	ipath = 'path to your directory/'
	ifile = 'data/201701-hubway-tripdata.csv'
	ofile = '201701-hubway-tripdata-counts.csv'
	
	main()



