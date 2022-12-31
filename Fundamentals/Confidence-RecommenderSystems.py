def item_select(items, query):
    '''
    input:
    items -> dictionary of items, with id as the key and list of items as the value
    query -> list of 2 values
    output:
    item_name -> name of the item with higher confidence value, showing it drives the growth of the other item
    '''
    item_name = ""

    # Your Code Starts here
    cnt_a = 0
    cnt_b = 0
    cnt_a_with_b = 0
    conf_a_b = -1
    conf_b_a = -1

    (query_a, query_b) = (query[0], query[1])
    print(" input ", query_a,query_b)
    for vals in items.values():
        if query_a in vals and query_b in vals:
            cnt_a_with_b += 1
        if query_a in vals:
            cnt_a += 1
        if query_b in vals:
            cnt_b += 1
    print(" cnt_a_with_b ", cnt_a_with_b," cnt_a ",cnt_a," cnt_b ",cnt_b)
    if cnt_a > 0:
        conf_a_b = cnt_a_with_b / cnt_a
    if cnt_b > 0:
        conf_b_a = cnt_a_with_b / cnt_b

    if conf_a_b > conf_b_a:
        item_name = query_a
    elif conf_a_b == conf_b_a:
        item_name = "same"
    else:
        item_name = query_b
    # Your Code Ends here
    return item_name


items = {'id1':['Bread','Milk'],
'id2':['Bread', 'Butter'],
'id3':['Eggs','Milk','Butter','Beer'],
'id4':['Bread','Beer','Butter'],
'id5':['Diapers','Cola','Shampoo','Cola','Bread']
}
query = ['Beer','Butter']

print(item_select(items, query))