import math
# 创建初始向量
z=[1,2,3,4,1,2,3]
# 对每个向量中每个值进行exp计算，  即 e^i , e的z[i]次幂 ，生成新的向量
z_exp = [math.exp(i) for i in z]
#  求和 exp后的向量中各个元素，
sum_z_exp = sum(z_exp)

# print(round(sum_z_exp , 2))
# z_exp 中每个数据除以 sum后的数据. 计算softmax的值
softmax = [round(i / sum_z_exp ,3) for i in z_exp]
print(softmax)
print(sum(softmax))
