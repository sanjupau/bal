import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the CSV file into a dataframe
df = pd.read_csv('datasettapadhir.csv')

# Split the Items Purchased column into separate columns for each item
items = df['Items Purchased'].str.split(',', expand=True)

# Convert the columns to binary variables
df = pd.get_dummies(items.stack()).sum(level=0)

# Define the number of partitions
num_partitions = 2

# Split the dataframe into partitions
partitions = [df[i:i+len(df)//num_partitions] for i in range(0, len(df), len(df)//num_partitions)]

# Apply association rule mining to each partition
for i, partition in enumerate(partitions):
    frequent_itemsets = apriori(partition, min_support=0.2, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
    print(f"Partition {i+1}:")
    print(rules)
   
   
 
OUTPUT:
   Partition 1:
   antecedents consequents  antecedent support  consequent support  support  \
0          (6)         (7)                 1.0                 1.0      1.0   
1          (7)         (6)                 1.0                 1.0      1.0   
2          (6)         (8)                 1.0                 0.6      0.6   
3          (8)         (6)                 0.6                 1.0      0.6   
4          (9)         (6)                 0.4                 1.0      0.4   
5          (8)         (7)                 0.6                 1.0      0.6   
6          (7)         (8)                 1.0                 0.6      0.6   
7          (9)         (7)                 0.4                 1.0      0.4   
8          (9)         (8)                 0.4                 0.6      0.2   
9       (6, 8)         (7)                 0.6                 1.0      0.6   
10      (6, 7)         (8)                 1.0                 0.6      0.6   
11      (8, 7)         (6)                 0.6                 1.0      0.6   
12         (6)      (8, 7)                 1.0                 0.6      0.6   
13         (8)      (6, 7)                 0.6                 1.0      0.6   
14         (7)      (6, 8)                 1.0                 0.6      0.6   
15      (6, 9)         (7)                 0.4                 1.0      0.4   
16      (7, 9)         (6)                 0.4                 1.0      0.4   
17         (9)      (6, 7)                 0.4                 1.0      0.4   
18      (6, 9)         (8)                 0.4                 0.6      0.2   
19      (8, 9)         (6)                 0.2                 1.0      0.2   
20         (9)      (6, 8)                 0.4                 0.6      0.2   
21      (8, 9)         (7)                 0.2                 1.0      0.2   
22      (7, 9)         (8)                 0.4                 0.6      0.2   
23         (9)      (8, 7)                 0.4                 0.6      0.2   
24   (6, 8, 9)         (7)                 0.2                 1.0      0.2   
25   (6, 7, 9)         (8)                 0.4                 0.6      0.2   
26   (8, 7, 9)         (6)                 0.2                 1.0      0.2   
27      (6, 9)      (8, 7)                 0.4                 0.6      0.2   
28      (8, 9)      (6, 7)                 0.2                 1.0      0.2   
29      (7, 9)      (6, 8)                 0.4                 0.6      0.2   
30         (9)   (6, 8, 7)                 0.4                 0.6      0.2   

    confidence      lift  leverage  conviction  
0          1.0  1.000000      0.00         inf  
1          1.0  1.000000      0.00         inf  
2          0.6  1.000000      0.00         1.0  
3          1.0  1.000000      0.00         inf  
4          1.0  1.000000      0.00         inf  
5          1.0  1.000000      0.00         inf  
6          0.6  1.000000      0.00         1.0  
7          1.0  1.000000      0.00         inf  
8          0.5  0.833333     -0.04         0.8  
9          1.0  1.000000      0.00         inf  
10         0.6  1.000000      0.00         1.0  
11         1.0  1.000000      0.00         inf  
12         0.6  1.000000      0.00         1.0  
13         1.0  1.000000      0.00         inf  
14         0.6  1.000000      0.00         1.0  
15         1.0  1.000000      0.00         inf  
16         1.0  1.000000      0.00         inf  
17         1.0  1.000000      0.00         inf  
18         0.5  0.833333     -0.04         0.8  
19         1.0  1.000000      0.00         inf  
20         0.5  0.833333     -0.04         0.8  
21         1.0  1.000000      0.00         inf  
22         0.5  0.833333     -0.04         0.8  
23         0.5  0.833333     -0.04         0.8  
24         1.0  1.000000      0.00         inf  
25         0.5  0.833333     -0.04         0.8  
26         1.0  1.000000      0.00         inf  
27         0.5  0.833333     -0.04         0.8  
28         1.0  1.000000      0.00         inf  
29         0.5  0.833333     -0.04         0.8  
30         0.5  0.833333     -0.04         0.8  
Partition 2:
   antecedents consequents  antecedent support  consequent support  support  \
0         (16)         (6)                 0.2                 1.0      0.2   
1         (16)         (7)                 0.2                 0.6      0.2   
2         (16)         (8)                 0.2                 0.4      0.2   
3          (8)        (16)                 0.4                 0.2      0.2   
4          (6)         (7)                 1.0                 0.6      0.6   
5          (7)         (6)                 0.6                 1.0      0.6   
6          (8)         (6)                 0.4                 1.0      0.4   
7          (9)         (6)                 0.2                 1.0      0.2   
8          (8)         (7)                 0.4                 0.6      0.4   
9          (7)         (8)                 0.6                 0.4      0.4   
10     (16, 6)         (7)                 0.2                 0.6      0.2   
11     (16, 7)         (6)                 0.2                 1.0      0.2   
12        (16)      (6, 7)                 0.2                 0.6      0.2   
13     (16, 6)         (8)                 0.2                 0.4      0.2   
14      (6, 8)        (16)                 0.4                 0.2      0.2   
15     (16, 8)         (6)                 0.2                 1.0      0.2   
16        (16)      (6, 8)                 0.2                 0.4      0.2   
17         (8)     (16, 6)                 0.4                 0.2      0.2   
18     (16, 8)         (7)                 0.2              
