#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""package problem
动态规划的经典应用场景 @背包九讲

object list = {
	{'weight':5,'value':20},
	{'weight':2,'value':08},
	{'weight':9,'value':53},
	{'weight':8,'value':50},
	{'weight':4,'value':12},
	{'weight':6,'value':35},
	{'weight':7,'value':23},
}
问题特点:
	1.物品数量固定，唯一
	2.问题可以要求[恰好]背包装满与不装满(稍微有些不同)
公式：
	value_map[i][content] = max{value_map[i-1][content], value_map[i-1][content-object[i].weight] + object[i].value}
	value_map[i][content]:表示前i件物品恰放入一个容量为 content 的背包可以获得的最大价值
思路:
	运行后可以看见一个规划表格 max_value_map，表格代表的含义 横:容量，纵:第 i 个物品
简化：
	二维压为一维
简化后的回溯：
	（待解决）额，，，好像没法回溯，最好还是在跑的时候记录吧, 
类似图的路径最短
"""
# object weight list and value list
wl = [5, 2, 9, 8,4,6,7]
vl = [20,8,53,50,12,35,23]
package_content = 21
"""base_func 未经优化的计算方法 时空(时间空间)复杂度为 O(N*V)
"""
def base_func(weight_list,value_list,package_content):
	if len(weight_list) != len(value_list):
		raise Exception("weight_list is not equle value_list")
	N = len(weight_list)
	wl,vl = weight_list,value_list
	value_map = [[0 for _t in range(package_content+1)] for i in range(N+1)]
	for i in range(1,N+1):
		for _c in range(1,package_content+1):
			# 默认不放置物品，设置最大值为前一个状态
			value_map[i][_c] = value_map[i-1][_c]
			# 满足最低放置的重量条件
			# 由于 i 由 0 出发，即 当前对象在 object_list 中对应的 index 为 i-1
			if  _c >= wl[i-1]:
				# value_map[i-1][_c - wl[i-1]]+vl[i-1] 着重理解这个对比对象
				# 即：value_map[i-1]上一个状态
				value_map[i][_c] = max(value_map[i][_c], value_map[i-1][_c - wl[i-1]]+vl[i-1])
	# 回溯获取物品
	# 思路，跟上一个状态做对比，如果值被改变，即当前物品被放入
	_t = package_content
	for i in range(N,0,-1):
		if value_map[i][_t] > value_map[i-1][_t]:
			print("index:",i-1,end=" ")
			_t -= wl[i-1]
	print()
	return value_map		



"""simplify(简化)
简化空间复杂
"""
def simplify_func(weight_list,value_list,package_content):
	if len(weight_list) != len(value_list):
		raise Exception("weight_list is not equle value_list")
	N = len(weight_list)
	wl,vl = weight_list,value_list
	value_map = [0 for _t in range(package_content+1)]
	for i in range(1,N+1):
		for _c in range(package_content,0,-1):
			if _c >= wl[i-1]:
				value_map[_c] = max(value_map[_c], value_map[_c - wl[i-1]] + vl[i-1])
	return value_map

"""m_simplify(再简化)
多余运算简化
"""
def m_simplify_func(weight_list,value_list,package_content):
	if len(weight_list) != len(value_list):
		raise Exception("weight_list is not equle value_list")
	N = len(weight_list)
	wl,vl = weight_list,value_list
	value_map = [0 for _t in range(package_content+1)]
	value_map[0] = 0
	obj_list = [0 for o in wl]
	for i in range(1,N+1):
		# 过滤超重物品
		if wl[i-1] <= package_content:
			for _c in range(package_content, wl[i-1]-1,-1):
				_max = max(value_map[_c], value_map[_c - wl[i-1]] + vl[i-1])
				if _max == value_map[_c]:
					obj_list[i-1] = 1
				value_map[_c] = _max
	print(obj_list)
	return value_map


def show(mmap):
	print("=="*10)
	for x in mmap:
		for i in x:
			print("%3d"%i,end=" ")
		print()
	print("=="*10)
	pass

mmap = base_func(wl,vl,package_content)
show(mmap)
mmap = simplify_func(wl,vl,package_content)
print(mmap)

mmap = m_simplify_func(wl,vl,package_content)
print(mmap)