import pandas as pd
import random

# Создаем список
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI':lst})

# Преобразуем столбец 'whoAmI' в one-hot вид
data['is_robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['is_human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

# Выводим первые строки DataFrame
data.head()