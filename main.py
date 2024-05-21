from tree_set import TreeSet


def main():
    ts = TreeSet()

    print("Adding Elements:")
    print(ts.add(5))  # True
    print(ts.add(3))  # True
    print(ts.add(7))  # True
    print(ts.add(3))  # False (Doesnt Exist)
    print("TreeSet Contents:", list(ts))  # [3, 5, 7]

    print("\nTesting addAll:")
    print(ts.addAll([1, 4, 6]))  # True
    print("TreeSet Contents:", list(ts))  # [1, 3, 4, 5, 6, 7]

    print("\nTesting ceiling:")
    print(ts.ceiling(5))  # 5
    print(ts.ceiling(2))  # 3
    print(ts.ceiling(8))  # None

    print("\nTesting floor:")
    print(ts.floor(5))  # 5
    print(ts.floor(2))  # 1
    print(ts.floor(0))  # None

    print("\nTesting higher:")
    print(ts.higher(5))  # 6
    print(ts.higher(7))  # None

    print("\nTesting lower:")
    print(ts.lower(5))  # 4
    print(ts.lower(1))  # None

    print("\nTesting first y last:")
    print(ts.first())  # 1
    print(ts.last())  # 7

    print("\nTesting pollFirst y pollLast:")
    print(ts.pollFirst())  # 1
    print("TreeSet Contents:", list(ts))  # [3, 4, 5, 6, 7]
    print(ts.pollLast())  # 7
    print("TreeSet Contents:", list(ts))  # [3, 4, 5, 6]

    print("\nTesting remove:")
    print(ts.remove(5))  # True
    print(ts.remove(10))  # False (Doesnt Exist)
    print("TreeSet Contents:", list(ts))  # [3, 4, 6]

    print("\nTesting contains:")
    print(ts.contains(4))  # True
    print(ts.contains(5))  # False

    print("\nTesting clear y size:")
    print(ts.size())  # 3
    ts.clear()
    print(ts.size())  # 0
    print("Contents of the TreeSet after clear:", list(ts))  # []

    print("Is TreeSet empty?:", ts.isEmpty())  # True

    ts.addAll([1, 2, 3, 4, 5])
    print("Contents of the TreeSet after addAll:", list(ts))  # [1, 2, 3, 4, 5]

    descending_iter = ts.descendingIterator()
    print("TreeSet Downstream Iterator:", list(descending_iter))  # [5, 4, 3, 2, 1]

    cloned_ts = ts.clone()
    print("Contents of the cloned TreeSet:", list(cloned_ts))  # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
