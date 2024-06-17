import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
import pandas as pd
data = pd.DataFrame({'whoAmI':lst})

one_hot_encoded_data = pd.get_dummies(data['whoAmI'])
data = pd.concat([data, one_hot_encoded_data], axis=1)

print(data.head())
