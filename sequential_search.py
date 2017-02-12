import random


def search(collection, value):
    index = 0
    for item in collection:
        if item == value:
            return True, index
        index += 1
    else:
        return False, -1


def main():
    collection = []
    for _ in range(100):
        collection.append(random.randint(0, 100))
    value = random.randint(0, 100)
    print('Collection is, ', collection)
    found, index = search(collection, value)
    if found:
        print('Value, ', value, 'found at location, ', index)
    else:
        print('Value is not present in collection')


if __name__ == '__main__':
    main()
