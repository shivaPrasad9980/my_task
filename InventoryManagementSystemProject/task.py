#Question 1
def circular_index_multiply_add(n):
    if not n:
        return []
    
    length = len(n)
    result = []
    
    for i in range(length):
        multiplied_value = n[i] * i
        next_index = (i + 1) % length
        next_value = n[next_index]
        result_value = multiplied_value + next_value
        
        result.append(result_value)
    
    return result


n = [1, 2, 3, 4]
print(circular_index_multiply_add(n))


# Question 2
def compress_string(s):
    
    result_list = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result_list.append(s[i - 1] + str(count))
            count = 1
    result_list.append(s[-1] + str(count))
    compressed_string = ''.join(result_list)
    return compressed_string if len(compressed_string) < len(s) else s

# for example
original_string = "aabcccccaaa"
print(compress_string(original_string))  


#Question 3
class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class NumberStore:
    def __init__(self):
        self.num_count = {}
        self.head = ListNode(0)  
        self.tail = ListNode(0)  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.num_nodes = {}

    def add(self, number):
        if number in self.num_count:
            self.num_count[number] += 1
            if self.num_count[number] == 2:
                self._remove_node(self.num_nodes[number])
        else:
            self.num_count[number] = 1
            new_node = ListNode(number)
            self.num_nodes[number] = new_node
            self._add_node(new_node)

    def getFirstUnique(self):
        if self.head.next == self.tail:
            return None
        return self.head.next.value

    def _add_node(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# for example 
store = NumberStore()
store.add(1)
store.add(2)
store.add(1)
print(store.getFirstUnique())  
store.add(2)
print(store.getFirstUnique())  
