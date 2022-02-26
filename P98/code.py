s1r=open('sample1.txt')
s1d=s1r.read()
s2r=open('sample2.txt')
s2d=s2r.read()

s1w=open('sample1.txt','w')
s2w=open('sample2.txt','w')
s1w.write(s2d)
s2w.write(s1d)