def filter_long_words(lin,n):
    l2=[]
    for i in lin:
        if len(i)>n:
            l2.append(i)

    return(l2)


# l=['hahahahahha','new','newww','nax','tyson','frigga']
# print(l)
# l3=filter_long_words(l,3)
# print(l3)
