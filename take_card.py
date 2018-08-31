#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
	Request: 一副从1到n的牌，每次从牌堆顶取一张放桌子上，再取一张放牌堆底，直到手机没牌，
			 最后桌子上的牌是从1到n有序，设计程序，输入n，输出牌堆的顺序数组
	Deal way: 后一半n/2~n间隔插在中间，迭代至1
	Time: 2018-8-31 14:40:23
"""
import math
# @param card num 	n>1
# @return list		orgin card list
def generate_cards(n):
	half_stack = []
	def get_half(pre_list):
		__half_list = pre_list[math.ceil(len(pre_list)/2):]
		# print(__half_list)
		half_stack.append(__half_list)
		if len(__half_list)>1:
			get_half(__half_list)
			pass
	# 间隔插入
	def l_insert(pre_harf_list, harf_list):
		print("{} ---> {}".format(harf_list, pre_harf_list))
		__pre_len = len(pre_harf_list)
		# 单数逆一张
		if (__pre_len/2) > int(__pre_len/2):
			_t = harf_list.pop()
			harf_list.insert(0,_t)
			pass
		for i in range(0,len(harf_list)):
			pre_harf_list.insert(1+2*(i), harf_list[i])
		return pre_harf_list[:__pre_len]
		pass
	res_cards = list(range(1,n+1))
	half_stack.append(res_cards)
	get_half(res_cards)
	# 间隔插入
	half_stack.reverse()
	print(half_stack)
	current_l = half_stack[0]
	for pre in range(1,len(half_stack)):
		current_l = l_insert(half_stack[pre], current_l)
		print(current_l)
	return current_l
	pass

def print_request(card_list):
	_t_list = card_list.copy()
	def mov2end(ls):
		if len(ls)>1:
			_t = ls.pop(0)
			ls.append(_t)
			pass
		pass
	for x in range(0,len(card_list)):
		print(_t_list.pop(0))
		mov2end(_t_list)
		pass
	pass

def main():
	card_num = 16
	res = generate_cards(card_num)
	print("="*35)
	print_request(res)
	pass

if __name__ == '__main__':
	main()