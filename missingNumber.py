def find_missing(list1, list2):
    slist1 = sorted(list1)
    slist2 = sorted(list2)

    if len(list1) == 0 and len(list2) == 0:
       return 0
    elif slist1 == slist2:
        return 0
    else:
        missingNum = set(slist1) ^ set(slist2)
        finalist = list(missingNum)[0]
        return finalist




print(find_missing([1,2,3,4],[1,2,3,4,5] ))