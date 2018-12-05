#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""package problem
动态规划的经典应用场景 @背包九讲

第二讲:完全背包

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
	1.物品数量无限
	2.问题可以要求[恰好]背包装满与不装满(稍微有些不同)
公式：
																							（0 <= k <= content/object[i].weight）
	value_map[i][content] = max{value_map[i-1][content], value_map[i-1][content-object[i].weight * k] + object[i].value * k}
	value_map[i][content]:表示前i件物品恰放入一个容量为 content 的背包可以获得的最大价值
优化：
	1. 物品选用比值高的，例如有物品 i,j weight[i] <= weight[j] && value[i] >= value[j], 则去除低比值物品 j
	2.转化为 1 类package problem, 设置 object[i] 物品上限 k = content//weight[i], 并添加入
思路:
	运行后可以看见一个规划表格 max_value_map，表格代表的含义 横:容量，纵:第 i 个物品
简化：
	二维压为一维
简化后的回溯：
	（待解决）额，，，好像没法回溯，最好还是在跑的时候记录吧, 
类似图的路径最短
"""