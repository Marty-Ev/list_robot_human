import random
import pandas as pd

# Исходные данные
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Уникальные категории в столбце
categories = data['whoAmI'].unique()

# Создание one-hot представления для каждой категории
one_hot_dict = {category: [1 if category == row else 0 for row in data['whoAmI']] for category in categories}

# Создание DataFrame из one-hot представления
one_hot_df = pd.DataFrame(one_hot_dict)

# Объединение исходного DataFrame с one-hot DataFrame
data = pd.concat([data, one_hot_df], axis=1)

print(data.head())
