n = input()
a_list = [int(i) for i in input().split(' ')[:int(n)]]


class Node:
    def __init__(self, idx, val):
        self.idx = idx+1
        self.val = val
        self.prev = None
        self.next = None
    def __repr__(self):
        return 'idx: %s, val: %s, prev: %r, next: %r'%(self.idx,self.val, self.prev.val if self.prev else None,self.next.val if self.next else None)
node_l = []
node_d = {}
for i, v in enumerate(a_list):
    node = Node(i, v)
    node_l.append(node)
    node_d[node.val] = node
sorted_node_l = sorted(node_l, lambda x: x.val)
# print([i.val for i in sorted_node_l])
# print([i.idx for i in sorted_node_l])
result = ''

prev = None
curr = None
head = None
for n in sorted_node_l:
    if curr is None:
        head = n
        curr = n 
        continue
    n.prev = curr
    curr.next = n
    prev = curr
    curr = n


for i in a_list[:0:-1]:
    node = node_d[i]
    # print(node)
    r = ''
    if node.prev is None:
        r = '%s %s\n'%(abs(i-node.next.val), node.next.idx)
        node.next.prev = None
    elif node.next is None:
        r = '%s %s\n'%(abs(i-node.prev.val), node.prev.idx)
        node.prev.next = None
    else:
        abs_p = abs(i-node.prev.val)
        abs_n = abs(i-node.next.val)
        if abs_p < abs_n:
            r = '%s %s\n'%(abs_p, node.prev.idx)
        elif abs_p == abs_n:
            r = '%s %s\n' % (abs_p, node.prev.idx if node.prev.val < node.next.val else node.next.idx)
        else:
            r = '%s %s\n'%(abs_n, node.next.idx)
        node.next.prev = node.prev
        node.prev.next = node.next
    result = r+ result
print(result.strip())
#h = head
#while h:
#    print(h.val)
#    h = h.next
