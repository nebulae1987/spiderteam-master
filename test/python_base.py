#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 8:48
# @Author  : Jun
# @Site    : 
# @File    : python_base.py
# @Software: PyCharm

#冒泡排序，相邻元素对比，大的往后移动：时间复杂度：O(n^2)
# a =[1,6,3,4,9,2,1]
# n = len(a)
# for i in range(n-1):
#     for j in range(n-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)
#
#
# #选择排序，从选择首位元素分别对比其他元素，大的往后换：时间复杂度：O(n^2)
# a =[1,6,3,4,9,2,1]
# n = len(a)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if a[i]>a[j]:
#             a[i],a[j] = a[j],a[i]
# print(a)

#快速排序：时间复杂度：O(log(n))

# def qSort(qlist):
#     if qlist == []:
#         return []
#     else:
#         qfirst = qlist[0]
#         lessPart = qSort([l for l in qlist[1:] if l < qfirst])
#         morePart = qSort([m for m in qlist[1:] if m >= qfirst])
#         return lessPart+[qfirst]+morePart
#
# a = [8,5,66,11,22,4,9,1,3,7]
# b = qSort(a)
# print(b)

#归并排序：把列表递归拆分为只包含一个元素的一个个列表，然后合并所有单元素列表
# def merge_sort(array):
#     #比较所有拆分过的列表元素，然后合并拆分后的列表
#     def merge_array(l_arr,r_arr):
#         array = []
#         while len(l_arr) and len(r_arr):
#             if l_arr[0] <= r_arr[0]:
#                 array.append(l_arr.pop(0))
#             elif l_arr[0] > r_arr[0]:
#                 array.append(r_arr.pop(0))
#         #左右两列表其中一个为空，另一个不是空时
#         if len(l_arr) != 0:
#             array += l_arr
#         elif len(r_arr) != 0:
#             array += r_arr
#         return array
#     #递归拆分列表：
#     def recursive(array):
#         if len(array) == 1:
#             return array
#         mid = len(array) // 2
#         l_arr = recursive(array[:mid])
#         r_arr = recursive(array[mid:])
#         return merge_array(l_arr,r_arr)
#
#     return recursive(array)
# a = [3,5,1,2,11,55,22,4,6]
# print(merge_sort(a))


#二分查找：从有序列表的候选区data[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半
# 在一段数字内，找到中间值，判断要找的值和中间值大小的比较。
# 如果中间值大一些，则在中间值的左侧区域继续按照上述方式查找。
# 如果中间值小一些，则在中间值的右侧区域继续按照上述方式查 找。
# 直到找到我们希望的数字。
import time
#计算运算时间：
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("runtime:",func.__name__, t2 - t1)
        return result
    return wrapper
#时间修饰器
@cal_time
def bin_search(data_set,val):
    #low 和high： 最小下标，最大下标，在给定数集列表data_set中查找val这个值
    low=0
    high=len(data_set)-1
    # 当low小于High的时候可取中间数
    while low <=high:
        mid=(low+high)//2
        if data_set[mid]==val:
            #得到该数在列表中的下标
            return mid
        elif data_set[mid]>val:
            high=mid-1
        else:
            low=mid+1
    # retrn Noneu证明没有找到
    return
data_set = list(range(10000000))
print(bin_search(data_set, 888888))