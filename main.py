# Pandas: Find the closest value to a Number in a Column

import pandas

df = pandas.DataFrame({
    'first name': ['Alice', 'Bobby', 'Carl', 'Alice'],
    'age': [20, 25, 50, 65],
    'net salary': [75, 60, 100, 70]
})

num = 21

result = df.iloc[(df['age'] - num).abs().argsort()[:1]]

#   first name  age  net salary
# 0      Alice   20          75
print(result)