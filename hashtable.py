#source: zyBooks 6.2 Chaining
class HashTable:
    def __init__(self, size=40):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, package): # Method to insert packages into the hash table
        package_id = package.ID
        bucket_index = self.hash(package_id)
        bucket = self.hash_table[bucket_index]

        for key_value in bucket:
            if key_value[0] == package_id:
                key_value[1] = package
                return True
#source: zyBooks Tuple basics
        bucket.append([package_id, package])
        return True

    def lookup(self, package_id): # Method to look up the packages that are stored
        bucket_index = self.hash(package_id)
        bucket = self.hash_table[bucket_index]

        for key_value in bucket:
            key, value = key_value
            if key == package_id:
                return value
        return None  # Return None if the package is not found
