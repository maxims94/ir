#!/usr/bin/python3

import model
import random
from random_data_model import *
from keyword_data_model import *

TEST_SIZE = 1/3.0

# Load database

items = model.Item.select()
items_arr = []

for item in items:
  items_arr.append(item) 

num_total = len(items_arr)
print(num_total)
num_test = int(TEST_SIZE * num_total)

test_sample = random.sample(items_arr, num_test)
training_sample = items_arr
for item in training_sample:
    if item in test_sample:
      training_sample.remove(item)

#print("##### Test items:")
#for item in test_sample:
#  print("%s | %s" % (str(item.class_), item.title))
#
#print("##### Training items:")
#for item in training_sample:
#  print("%s | %s" % (str(item.class_), item.title))

# For reference
#data_model = RandomDataModel()
data_model = KeywordDataModel()
data_model.train(training_sample)
print ("Trained model: %s" % str(data_model))
 
print ("Classification result:")

num_correct = 0
for item in test_sample:

  model_class = data_model.class_(item)
  model_class_prob = data_model.class_prob(item)

  if item.class_ == model_class:
    num_correct += 1
  print("%i | %i (%0.2f) | %10s " % (item.class_, model_class, model_class_prob, item.title))

perc_correct = (float(num_correct)/num_test*100)
print("%i correct out of %i (%0.2f%%)" % (num_correct, num_test, perc_correct))

mse = 0
for item in test_sample:
  mse += (int(item.class_) -  data_model.class_prob(item))**2 

mse = float(mse) / num_test

print("MSE: %1.5f" % mse)
