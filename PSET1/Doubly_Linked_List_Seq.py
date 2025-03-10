class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        head = self.head
        new_head = Doubly_Linked_List_Node(x)
        if head:
            head.prev = new_head
        if not self.tail:
            self.tail = new_head
        new_head.next = head
        self.head = new_head

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        tail = self.tail
        new_tail = Doubly_Linked_List_Node(x)
        if tail:
            tail.next = new_tail
        if not self.head:
            self.head = new_tail
        new_tail.prev = tail
        self.tail = new_tail

    def delete_first(self):
        assert self.head
        x = self.head.item
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_head = self.head.next
        if new_head:
            new_head.prev = None
            if not new_head.next:
                self.tail = new_head
        self.head = new_head
        return x

    def delete_last(self):
        assert self.tail
        x = self.tail.item
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_tail = self.tail.prev
        if new_tail:
            new_tail.next = None
            if not new_tail.prev:
                self.head = new_tail
        self.tail = new_tail
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! #
        ###########################
        left, right = x1.prev, x2.next

        if left:
            left.next = right
            if not right:
                self.tail = left
        else:
            self.head = right

        if right:
            right.prev = left
            if not left:
                self.head = right
        else:
            self.tail = left

        x1.prev = x2.next = None
        L2.head, L2.tail = x1, x2
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! #
        ###########################
        left, right = x, x.next

        L2.head.prev = left
        L2.tail.next = right
        left.next = L2.head
        if right:
            right.prev = L2.tail
        else:
            self.tail = L2.tail
        L2.head = L2.tail = None
