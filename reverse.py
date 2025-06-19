def reverse(f_list):
    item = len(f_list)
    r_list =[]
    for i in range(item):
        r_list[::] = f_list[::-1]
        item -= 1
        i += 1
    print(r_list)

list = [1,2,3,"Hello","first"]
reverse(list)