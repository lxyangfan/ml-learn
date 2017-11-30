#encoding=utf-8
import math
import pdb

def entropy(p=None):
    """计算信息熵，p是float list,表示离散随机变量的概率分布"""
    if p == None:
        p = []
    res = 0.0
    for item in p:
        if item - 0.0 < 0.0000001:
            continue
        res += item * math.log(item, 2)
    return -res


def entropy_fromdict(p=None):
    """计算信息熵，p是float list,表示离散随机变量的概率分布"""
    if p == None:
        p = {}
    res = 0.0
    for item in p:
        if item - 0.0 < 0.0000001:
            continue
        res += item * math.log(item, 2)
    return -res

def info_gain(px=None,py=None, p_xy=None):
    """计算特征选择了x后的信息增益，px表示特征x的概率分布，py表示f分类Y的概率分布，p_xy是P(X|Y)条件概率分布
    
    px float list, size n, 
    py float list, size m,
    p_xy 2D list, size n*m
    
    """
    h_y = entropy(py)
    print h_y
    h_xy = 0.0
    for idx, val in enumerate(px):
        if val - 0.0 < 0.0000001:
            continue
        h_xy += val * entropy(p_xy[idx])
    print h_xy
    return h_y - h_xy
        

print info_gain([9.0/15, 6.0/15],[9.0/15, 6.0/15],[[1.0, 1.0/3], [0, 2.0/3]])
    
    
    

