# to access dic by index
embeddings_index = {}
for i in range(10):
    print(embeddings_index.index2entity[i])

# to get dict items

for k, v in embeddings_index.items():
    do anything



import operator
# reversed(descending) sorting of dictionary
sorted_x = sorted(oov.items(), key=operator.itemgetter(1))[::-1]

# ascending sorting of dictionary
sorted_x = sorted(oov.items(), key=operator.itemgetter(1))
