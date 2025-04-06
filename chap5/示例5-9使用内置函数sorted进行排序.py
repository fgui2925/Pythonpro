lst=[4,56,3,8,20,67,98]
print('原列表：',lst,id(lst))

#使用sorted()函数排序，会产生新的列表对象
asc_lst=sorted(lst)
print('原列表：',lst,id(lst))
print('默认排序后列表：',asc_lst,id(asc_lst))

#降序
asc_lst=sorted(lst,reverse=True)
print('原列表：',lst,id(lst))
print('降序后的列表：',asc_lst,id(asc_lst))

# 对字符窜进行排序，实质是对字符在ASCII表中的顺序进行排序
lst2=['banana','apple','Cat','Orange']
new_lst2=sorted(lst2)
print('原列表：',lst2,id(lst2))
print('默认排序后的列表：',new_lst2,id(new_lst2))

#忽略大小写进行排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表：',lst2,id(lst2))
print('默认排序后的列表：',new_lst2,id(new_lst2))