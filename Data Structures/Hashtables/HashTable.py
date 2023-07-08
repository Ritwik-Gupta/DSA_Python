class HashTable:
    def __init__(self, size=7):
        self.data_map = [None]*7
    
    def create_hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 71) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        #calculate the hash
        idx = self.create_hash(key)
        if(self.data_map[idx] is None) :
            self.data_map[idx] = []
        self.data_map[idx].append([key,value])

    def print_table(self):
        for i,j in enumerate(self.data_map):
            print("{}: {}".format(i,j))


h1 = HashTable(8)

h1.set_item("name", "ritwik")
h1.set_item("age",100)

h1.print_table()