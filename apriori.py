import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_csv('tapadhirdataset.csv')
transactions = [x.strip().split(',') for x in df['Items Purchased'].tolist()]

items = list(set([item for transaction in transactions for item in transaction]))
transaction_data = []
for transaction in transactions:
    row = []
    for item in items:
        if item in transaction:
            row.append(1)
        else:
            row.append(0)
    transaction_data.append(row)
transactions_df = pd.DataFrame(transaction_data, columns=items)
frequent_itemsets = apriori(transactions_df, min_support=0.3, use_colnames=True)

# Generate association rules from the frequent itemsets
association_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.15)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(association_rules)



OUTPUT:
  Frequent Itemsets:
   support   itemsets
0      1.0        (6)
1      0.3        (9)
2      0.8        (7)
3      0.5        (8)
4      0.3     (6, 9)
5      0.8     (6, 7)
6      0.5     (6, 8)
7      0.5     (8, 7)
8      0.5  (6, 8, 7)

Association Rules:
   antecedents consequents  antecedent support  consequent support  support  \
0          (6)         (9)                 1.0                 0.3      0.3   
1          (9)         (6)                 0.3                 1.0      0.3   
2          (6)         (7)                 1.0                 0.8      0.8   
3          (7)         (6)                 0.8                 1.0      0.8   
4          (6)         (8)                 1.0                 0.5      0.5   
5          (8)         (6)                 0.5                 1.0      0.5   
6          (8)         (7)                 0.5                 0.8      0.5   
7          (7)         (8)                 0.8                 0.5      0.5   
8       (6, 8)         (7)                 0.5                 0.8      0.5   
9       (6, 7)         (8)                 0.8                 0.5      0.5   
10      (8, 7)         (6)                 0.5                 1.0      0.5   
11         (6)      (8, 7)                 1.0                 0.5      0.5   
12         (8)      (6, 7)                 0.5                 0.8      0.5   
13         (7)      (6, 8)                 0.8                 0.5      0.5   

    confidence  lift  leverage  conviction  
0        0.300  1.00       0.0    1.000000  
1        1.000  1.00       0.0         inf  
2        0.800  1.00       0.0    1.000000  
3        1.000  1.00       0.0         inf  
4        0.500  1.00       0.0    1.000000  
5        1.000  1.00       0.0         inf  
6        1.000  1.25       0.1         inf  
7        0.625  1.25       0.1    1.333333  
8        1.000  1.25       0.1         inf  
9        0.625  1.25       0.1    1.333333  
10       1.000  1.00       0.0         inf  
11       0.500  1.00       0.0    1.000000  
12       1.000  1.25       0.1         inf  
13       0.625  1.25       0.1    1.333333  
