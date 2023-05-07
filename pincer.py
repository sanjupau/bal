from collections import defaultdict
import csv
from itertools import combinations

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the first row (header)
        transactions = []
        for row in reader:
            transactions.append([int(item) for item in row[1].split(',')])
        return transactions


def pincer_search(transactions, min_sup, min_conf):
    # Initialize variables
    itemsets = defaultdict(int)
    frequent_itemsets = []
    n = len(transactions)
    m = len(transactions[0])
    start = 0
    end = m - 1
    
    # Phase 1: forward pincer movement
    while start < n and end >= 0:
        # Count the frequency of itemsets in the current range
        count = defaultdict(int)
        for i in range(start, n):
            for j in range(end, -1, -1):
                items = transactions[i][j:]
                for k in range(len(items)):
                    itemset = tuple(sorted(items[:k] + items[k+1:]))
                    count[itemset] += 1

        # Prune infrequent itemsets
        infrequent_itemsets = set(itemset for itemset, freq in count.items() if freq < min_sup)
        for itemset in infrequent_itemsets:
            del count[itemset]

        # Add frequent itemsets to the result
        frequent_itemsets.extend(count.keys())
        itemsets.update(count)

        # Move the pincer
        if end > 0:
            end -= 1
        else:
            start += 1

    # Phase 2: backward pincer movement
    for i in range(n):
        for j in range(m):
            items = transactions[i][:j+1]
            for k in range(len(items)):
                itemset = tuple(sorted(items[:k] + items[k+1:]))
                if itemset in itemsets and itemsets[itemset] >= min_sup:
                    frequent_itemsets.append(itemset)

    # Generate association rules
    rules = []
    for itemset in frequent_itemsets:
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(itemset) - set(antecedent)))
                support = itemsets[itemset] / float(n)
                confidence = itemsets[itemset] / float(itemsets[antecedent])
                lift = confidence / (itemsets[consequent] / float(n))
                if confidence >= min_conf:
                    rules.append((antecedent, consequent, support, confidence, lift))

    return frequent_itemsets, rules


# Example usage
filename = 'datasettapadhir.csv'
min_sup = 3
min_conf = 0.5
transactions = read_csv_file(filename)
frequent_itemsets, rules = pincer_search(transactions, min_sup, min_conf)

print("Frequent itemsets:")
for itemset in frequent_itemsets:
    print(list(itemset),end=',')

print("Association rules:")
for antecedent, consequent, support, confidence, lift in rules:
    print(list(antecedent), "->", list(consequent), "Support:", round(support, 2), "Confidence:", round(confidence, 2), "Lift:", round(lift, 2))
    
    

    
OUTPUT:
  Frequent itemsets:
[],[9],[8],[7, 8],[7],[6, 8],[6, 7],[6],[9],[8],[7, 8],[],[7],[6, 8],[6, 7],[6],[7, 8],[8],[7],[6, 8],[6, 7],[],[6],[7, 8],[6, 8],[6, 7],[6],[7, 8],[6, 8],[6, 7],[6],[6, 7],[6],[6],[],[7],[6],[7, 8],[6, 8],[6, 7],[],[7],[6],[7, 8],[6, 8],[6, 7],[7, 8],[6, 8],[6, 7],[],[7],[6],[6, 7],[6, 7],[],[7],[6],[7],[6],[7],[6],[],[7],[6],[7, 8],[6, 8],[6, 7],[7, 8],[6, 8],[6, 7],[],[7],[6],[7, 8],[6, 8],[6, 7],[7, 8],[6, 8],[6, 7],[],[7],[6],[7],[6],[7],[6],[],[7],[6],[7, 8],[6, 8],[6, 7],[],[9],[6],[9],[6],[9],[6],[],[],[],[],Association rules:
[7] -> [8] Support: 0.3 Confidence: 0.5 Lift: 1.67
[8] -> [7] Support: 0.3 Confidence: 1.0 Lift: 1.67
[6] -> [8] Support: 0.3 Confidence: 1.0 Lift: 3.33
[8] -> [6] Support: 0.3 Confidence: 1.0 Lift: 3.33
[6] -> [7] Support: 0.3 Confidence: 1.0 Lift: 1.67
