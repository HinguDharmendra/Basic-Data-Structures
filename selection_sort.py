import random


def sort(collection):
    for i in range(0, len(collection) - 1):
        smallest = collection[i]
        index = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[index]:
                smallest = collection[j]
                index = j
        collection[i], collection[index] = collection[index], collection[i]
    return collection


def main():
    collection = []
    for _ in range(10):
        collection.append(random.randint(0, 10))
    print(collection)
    print(sort(collection))


if __name__ == '__main__':
    main()
