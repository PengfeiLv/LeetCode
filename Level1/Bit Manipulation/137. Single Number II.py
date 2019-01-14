# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:55
# @Author  : Lvpengfei

"""  学习 bit manipulation """
"""
方法一：数学计算 
	这类题目真正考察的是位运算，虽然本题可以用数学法计算出来
"""
def singleNumber1(nums):
	return (3*sum(set(nums))-sum(nums))//2

if __name__ == "__main__":
	nums = [0, 1, 0, 1, 0, 1, 99]
	print(singleNumber1(nums))