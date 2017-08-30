from os import listdir
from os.path import isfile, join

mypath = "/home/carlos/Bee/images/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

train_file = open("train.txt", 'w')
val_file = open("val.txt", 'w')
i = 0
for file in onlyfiles:
	file = file.split('.')[0]
	train_file.write(file+" -1\n")
	if i%10 == 0:
		val_file.write(file+" -1\n")
	i += 1
