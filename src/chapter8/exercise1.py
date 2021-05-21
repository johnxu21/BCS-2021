
def chop(lst):
    del lst[0]  # removes 1st element in the list
    del lst[-1]  # removes last element in the list
    return None


def middle(lst):
    new = lst[1:]
    del new[-1]
    return new


list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

chop_list = chop(list1)
print(list1)
print(chop_list)

middle_list = middle(list2)
print(list2)
print(middle_list)
