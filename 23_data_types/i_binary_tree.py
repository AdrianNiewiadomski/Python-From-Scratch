from typing import Union


class TreeNode:
    def __init__(self, parent=None):
        self.value: Union[None, int] = None
        self.parent: Union[None, TreeNode] = parent
        self.left_child: Union[None, TreeNode] = None
        self.right_child: Union[None, TreeNode] = None

    def add_node(self, value: int):
        if not self.value:
            self.value = value

        else:
            if value < self.value:
                if not self.left_child:
                    self.left_child = TreeNode(parent=self)
                self.left_child.add_node(value)
            else:
                if not self.right_child:
                    self.right_child = TreeNode(parent=self)
                self.right_child.add_node(value)

    def find_in_tree(self, value: int):
        if value == self.value:
            return self
        elif value < self.value:
            return self.left_child.find_in_tree(value)
        else:
            return self.right_child.find_in_tree(value)

    def remove(self):
        pass

    def print(self):
        pass


if __name__ == "__main__":
    my_tree = TreeNode()
    numbers = [15, 7, 13, 30, 25, 4, 34]
    for number in numbers:
        my_tree.add_node(number)

    searching_result = my_tree.find_in_tree(13)
    print(searching_result.value)

