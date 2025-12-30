items = input().split() # список продуктов :(
    
freq = {} #пустой словарь, где ключи будут названия продуктов, а значения сколько раз они встречаются


for item in items:
    if item in freq:
        freq[item] += 1 #Если продукт уже есть в словаре freq, увеличиваем счётчик на 1
    else:
        freq[item] = 1 #Если нет — добавляем продукт в словарь с начальным значением 1

print("Purchase frequency:")
for item in freq:
    print(item, ":", freq[item])


max_count = 0 #Макс. продукт 
popular = ""

for item in freq:
    if freq[item] > max_count:# Проходим по всем продуктам и проверяем, чей счётчик больше всего
        max_count = freq[item]
        popular = item

print("Most popular item:", popular)

print("Purchased once:", end=" ")
for item in freq:
    if freq[item] == 1:
        print(item, end=" ")
print()

print("Sorted by frequency:")
for item in freq:
    print(item, freq[item])
