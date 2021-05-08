重点为实现并查集，关键又在find()函数

设定一个dic p = {i:i for i in len(s)} 即为i这个节点的根为哪个节点

f(x)找根

​	if x!=p[x]:#x不是根节点

​		p[x]=f(p[x]) #递归，找到最终的根节点

return p[x]

#初始化p

for i,j in pairs:

​	p[f(j)] = f(i) #i，j相连通，则这里操作是将j的根节点移动给i的根节点，做其子节点

#合并，将在一起的放在一个list里

d = collections.defaultdict(list)

for i,j in enumerate(map(f,p)):

​	d[j].append(i)

ans = list(s)

for i in d.values():

​	m_s = sorted([ ans[j] for j in i ])

​	m_i = sorted(i)

​	for x,y in zip(m_s,m_i):

​		ans[y]=x

return ans