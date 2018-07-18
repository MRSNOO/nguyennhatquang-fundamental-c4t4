def get_even_list(list_numb):
    newlist = []
    for item in list_numb:
        if item % 2 == 0:
            newlist.append(item)
    print(newlist)
get_even_list([1,2,3,4,5])