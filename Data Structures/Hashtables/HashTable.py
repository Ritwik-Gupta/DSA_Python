class HashTable:
    def __init__(self, size=7):
        self.data_map = [None]*7
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 71) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        #calculate the hash
        idx = self.__hash(key)
        if(self.data_map[idx] is None) :
            self.data_map[idx] = []
        self.data_map[idx].append([key,value])

    def get_item(self, key):
        idx = self.__hash(key)
        val = self.data_map[idx]
        if val:
            for k in val:
                if(k[0] == key):
                    return k[1]
        return None

    def get_keys(self):
        keys = []
        for key_pairs in self.data_map:
            if key_pairs:
                for j in key_pairs:
                    keys.append(j[0])
        return keys

    def print_table(self):
        for i,j in enumerate(self.data_map):
            print("{}: {}".format(i,j))


h1 = HashTable(8)

h1.set_item("name", 888)
h1.set_item("age",100)
h1.set_item("test",101)
h1.set_item("som1",87)


h1.print_table()

print(h1.get_item("age"))

print(h1.get_keys())