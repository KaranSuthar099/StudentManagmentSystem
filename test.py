from backend import get_all_data
data = get_all_data()

for i in data:
    if i[0]==1:
        print(i)

print(data)