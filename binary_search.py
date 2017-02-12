import random


def search(sorted_collection, value, low, high):
    """
    This comparator applies binary search algorithm, and returns true if the element is present
    :pre-condition the collection must be sorted
    :param sorted_collection: collection
    :param value: item to be searched
    :return: boolean
    """
    while high > low:
        mid = (low + high) // 2
        if value == sorted_collection[mid]:
            return True, mid
        elif value < sorted_collection[mid]:
            high = mid - 1
        elif value > sorted_collection[mid]:
            low = mid + 1

    else:
        return False, -1


def _search(sorted_collection, value, low, high):
    if high < low:
        return False, -1
    else:
        mid = (low + high) // 2
        if value == sorted_collection[mid]:
            return True, mid
        elif value < sorted_collection[mid]:
            return _search(sorted_collection, value, low, mid - 1)
        else:
            return _search(sorted_collection, value, mid + 1, high)


def main():
    collection = []
    for _ in range(10):
        collection.append(random.randint(0, 10))
    value = random.randint(0, 10)
    collection.sort()
    print('Collection is, ', collection)
    found, index = _search(collection, value, 0, len(collection))
    if found:
        print('Value, ', value, 'found at location, ', index)
    else:
        print('Value,', value, 'is not present in collection')


if __name__ == '__main__':
    main()
