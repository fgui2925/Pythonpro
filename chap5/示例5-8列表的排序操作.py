lst=[4,56,3,8,20,67,98]
print('原列表：',lst,id(lst))

# 排序
lst.sort()  # 默认是升序。sort(key=None,reverse=False).key是排序关键字，即排序规则；默认是升序，reverse=False时是降序。
print('默认排序后列表：',lst,id(lst))

# 降序
lst.sort(reverse=True)
print('降序后的列表',lst,id(lst))


# 对字符窜进行排序，实质是对字符在ASCII表中的顺序进行排序
lst2=['banana','apple','Cat','Orange']
lst2.sort()
print('默认排序后的列表：',lst2,id(lst2))

#降序
lst2.sort(reverse=True)
print('降序后的列表',lst2,id(lst2))

#忽略大小写进行排序
lst2.sort(key=str.lower)
print('忽略大小写后排序：',lst2,id(lst2))

