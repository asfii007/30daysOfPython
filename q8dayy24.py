# Merge two dictionaries. If the same key exists, sum their values.

dict1={
    "apples":10,
    "mango":21,
    "orange":11
}
dict2={
    "stawberry":9,
    "apples":9,
    "tomato":8
}
merged = dict1.copy()  # start with dict1

for key, value in dict2.items():
    if key in merged:
        merged[key] += value  # sum values if key exists
    else:
        merged[key] = value   # add new key

print(merged)