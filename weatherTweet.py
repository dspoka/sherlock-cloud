import csv



def run(data):
	raw_train_data = open(data, 'r')
	train_data = csv.reader(raw_train_data, delimiter = ",")
	for row in train_data:
		print row


run('train.csv')