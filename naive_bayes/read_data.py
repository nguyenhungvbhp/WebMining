import pandas as pd

# path_train = 'dataset/labeled_dataset.csv'
# data = pd.read_csv(path_train)
#
# data = data.sample(frac=1)
#
# data.to_csv('dataset/train.csv', sep=',', encoding='utf-8')

def read_data(path):
    data = pd.read_csv(path)
    # Thống kế giá trị nhãn
    # print(data["Label"].value_counts())
    return data['Review'], data['Label']


# d = read_data('dataset/test.csv')
# print(d)
