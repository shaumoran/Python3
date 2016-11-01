# Balances a BST
#   Arrange a list so that when added to a tree will cause the tree to be completely balanced
#
def make_list(lst):
    if len(lst) < 2:
        return lst
    lst = sorted(lst)
    middle = len(lst) // 2
    return [lst[middle]] + make_list(lst[:middle]) + make_list(lst[middle+1:])
