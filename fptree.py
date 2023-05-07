import csv
import pyfpgrowth

transactions = []
with open('datasettapadhir.csv', mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        transactions.append(row)
       
# Finding the frequent patterns with min support threshold=0.5
FrequentPatterns = pyfpgrowth.find_frequent_patterns(transactions=transactions, support_threshold=0.5)
print(FrequentPatterns)

# Generating rules with min confidence threshold=0.5
Rules = pyfpgrowth.generate_association_rules(patterns=FrequentPatterns, confidence_threshold=0.5)
Rules



OUTPUT:
  {('ï»¿Transaction ID',): 1, ('Items Purchased',): 1, ('Items Purchased', 'ï»¿Transaction ID'): 1, ('1',): 1, ('6,7,8,9',): 1, ('1', '6,7,8,9'): 1, ('2',): 1, ('2', '6,7,8'): 1, ('3',): 1, ('6,7,9',): 1, ('3', '6,7,9'): 1, ('4',): 1, ('4', '6,7'): 1, ('5',): 1, ('5', '6,7,8'): 1, ('7',): 1, ('6,7', '7'): 1, ('8',): 1, ('6,7,8,16',): 1, ('6,7,8,16', '8'): 1, ('9',): 1, ('6,9',): 1, ('6,9', '9'): 1, ('10',): 1, ('10', '6'): 1, ('6,7',): 2, ('6',): 2, ('6', '6,7,8'): 1, ('6,7,8',): 3}
{('Items Purchased',): (('ï»¿Transaction ID',), 1.0),
 ('ï»¿Transaction ID',): (('Items Purchased',), 1.0),
 ('1',): (('6,7,8,9',), 1.0),
 ('6,7,8,9',): (('1',), 1.0),
 ('2',): (('6,7,8',), 1.0),
 ('3',): (('6,7,9',), 1.0),
 ('6,7,9',): (('3',), 1.0),
 ('4',): (('6,7',), 1.0),
 ('6,7',): (('7',), 0.5),
 ('5',): (('6,7,8',), 1.0),
 ('7',): (('6,7',), 1.0),
 ('6,7,8,16',): (('8',), 1.0),
 ('8',): (('6,7,8,16',), 1.0),
 ('6,9',): (('9',), 1.0),
 ('9',): (('6,9',), 1.0),
 ('10',): (('6',), 1.0),
 ('6',): (('6,7,8',), 0.5)}
