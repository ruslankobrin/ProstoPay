class HashMap:
    def __init__(self, size=10):
        """
        Initializes the HashMap with an optional initial size.

        Args:
            size (int): The initial size of the HashMap (default is 10).
        """
        self.size = size
        self.map = [None] * size

    def _hash(self, key):
        """
        Generates a hash code for the given key.

        Args:
            key: The key to be hashed.

        Returns:
            int: The hash code for the key.
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Inserts a key-value pair into the HashMap.

        If a key already exists, its value will be updated.

        Args:
            key: The key of the entry to be inserted or updated.
            value: The value associated with the key.
        """
        index = self._hash(key)
        if self.map[index] is None:
            self.map[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    self.map[index][i] = (key, value)
                    return
            self.map[index].append((key, value))

    def get(self, key):
        """
        Retrieves the value associated with the given key from the HashMap.

        Args:
            key: The key whose associated value is to be retrieved.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        if self.map[index] is None:
            return None
        for k, v in self.map[index]:
            if k == key:
                return v
        return None
