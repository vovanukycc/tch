def remove_duplicates(list_n):
    list_e = []
    for i in list_n:
        if i not in list_e:
            list_e.append(i)
    return list_e


print(remove_duplicates([1,1,2,2,3,3,3,3]))