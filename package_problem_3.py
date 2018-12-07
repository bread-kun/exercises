#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""package problem
动态规划的经典应用场景 @背包九讲

第三讲:多重背包

object list = {
	{'weight':5,'value':20,'limit':3},
	{'weight':2,'value':08,'limit':8},
	{'weight':9,'value':53,'limit':5},
	{'weight':8,'value':50,'limit':4},
	{'weight':4,'value':12,'limit':6},
	{'weight':6,'value':35,'limit':2},
	{'weight':7,'value':23,'limit':1},
}
问题特点:
	1.物品数量有限
	注:理解完 完全背包，基本也就能理解并解决 多重背包问题
公式：
																					(0<= k <= limit[i])
	value_map[i][content] = max{value_map[i-1][content], value_map[i-1][content-object[i].weight * k] + object[i].value * k}
	value_map[i][content]:表示前i件物品恰放入一个容量为 content 的背包可以获得的最大价值
优化：
	1. 物品选用比值高的，例如有物品 i,j weight[i] <= weight[j] && value[i] >= value[j], 则去除低比值物品 j
	2.转化为 1 类package problem, 设置 object[i] 物品上限 k = content//weight[i], 并添加入
思路:
	运行后可以看见一个规划表格 max_value_map，表格代表的含义 横:容量，纵:第 i 个物品
	来回切换 完全与一般 package_problem


# 看图理解
# object weight list and value list
  0   1   2   3   4   5   6   7   8   9  10  11  12

  0   0   0   0   0   0   0   0   0   0   0   0   0 
  0   0   0   0   5   5   5   5 +10 +10 +10 +10 *10  
  0   1  +2  *3   5   6  +7  *8  10  11 +12 *13 *13
  0   1  +2   4   5   6  *8  ##  ##  ##  ##   #   #  
  0   1  +2   4   5   6  ##  ##  ##  ##  ##   #   #  
  0   1  +2   4   5   6  ##  ##  ##  ##  ##   #   #  
  0   1  +2   4   5   6  ##  ##  ##  ##  ##   #   #  
  0   1  +2   4   5   6  ##  ##  ##  ##  ##   #   #  

  wl [ 4, 1, 3,  8]
  vl [ 5, 1, 4, 12]
  ll [ 2, 3, 2,  2]
  pak = 12 

"""

"""base_func 未经优化的计算方法 时空(时间空间)复杂度为 O(N*V)
"""
def base_func(w,v,l,pkg):
	if len(w) != len(v):
		raise Exception("w is not equle v")
	_map = [[0 for _t in range(pkg+1)] for i in range(len(w)+1)]
	for i in range(1,len(w)+1):
		# 统计一下数量
		_k = 0
		for _c in range(1,pkg+1):
			# 默认不放置物品，设置最大值为前一个状态
			_map[i][_c] = _map[i-1][_c]
			# 满足最低放置的重量条件
			# 由于 i 由 0 出发，即 当前对象在 object_list 中对应的 index 为 i-1
			if  _c >= w[i-1]:
				# _map[i-1][_c - w[i-1]]+vl[i-1] 着重理解这个对比对象
				# 即：_map[i-1]上一个状态
				if _k >= l[i-1]:
					_max = max(_map[i][_c], _map[i-1][_c - w[i-1]]+vl[i-1])
				else:
					_max = max(_map[i][_c], _map[i][_c - w[i-1]]+vl[i-1])
					_map[i][_c] = 
				_max = max(_map[i][_c], _map[i][_c - w[i-1]]+vl[i-1])
				if _max is _map[i][_c]:
					continue
				if _map is _map[i][_c - w[i-1]]+vl[i-1]:
					_k += 1
					_k = 0
				if _k <= l[i-1]:
					_map[i][_c] = _max
				if
					
	# 回溯获取物品
	# 思路，跟上一个状态做对比，如果值被改变，即当前物品被放入
	_t = package_content
	for i in range(N,0,-1):
		_k = 0
		while _map[i][_t] > _map[i-1][_t]:
			_t -= w[i-1]
			_k += 1
		if _k > 0:
			print("index:%3dx%d ;"%(i-1,_k),end=" ")
	print()
	return _map		


def show(mmap):
	print("=="*10)
	for x in mmap:
		for i in x:
			print("%3d"%i,end=" ")
		print()
	print("=="*10)
	pass
wl = [ 5, 1,  4,  9, 2]
vl = [14, 3, 13, 27, 6]
# limit list
ll = [ 3, 2,  8,  9, 4]
package_content = 10

mmap = base_func(wl,vl,ll,package_content)
show(mmap)