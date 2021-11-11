class BinarySearchTree:
    def __init__(self, value):
        # the value at the current node
        self.value = value
        # reference to this node's left child
        self.left = None
        # reference to this node's right child
        self.right = None

    def insert(self, value):
        # check if the new node's value is less than our current node's value
        if value < self.value:
            # if there's no left child here already, place the new node here
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise, repeat the process!
                self.left.insert(value)
        # check if the new node's value is greater than or equal to our
        # current node's value
        elif value >= self.value:
            # if there's no right child here already, place the new node here
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # otherwise, repeat the process!
                self.right.insert(value)

    def pre_order_dft(self):
        if self is None:
            return
        print(self.value)
        self.left.pre_order_dft()
        self.right.pre_order_dft()

    def in_order_dft(self):
        if self is None:
            return
        self.left.in_order_dft()
        print(self.value)
        self.right.in_order_dft()

    def post_order_dft(self):
        if self is None:
            return
        self.left.post_order_dft()
        self.right.post_order_dft()
        print(self.value)

    def bft_print(self):
        q = []
        q.append(self)

        while len(q) > 0:
            current = q.pop(0)
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    def dft_print(self):
        s = []
        s.append(self)

        while len(q) > 0:
            print(current.value)
            current = s.pop()
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


# test
t = BinarySearchTree("hello")
t.left = BinarySearchTree("hi")
t.right = BinarySearchTree("woooo")


def mult_10(val):
    print(val * 20)


t.for_each(mult_10)
