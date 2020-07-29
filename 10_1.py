import numpy as np
import matplotlib.pyplot as plt
vec1=np.array([-1.,4.,-9.])
mat1=np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
vec2=(np.pi/4)*vec1
vec2=np.cos(vec2)
vec3=vec1+2*vec2
"""
la.norm(vec3)
"""
vec4=np.multiply(mat1,vec3)

TRPmat1=mat1.transpose()

DTRmat1=np.linalg.det(mat1)

TRCmat1=np.trace(mat1)

MINvec1=np.amin(vec1)

Jvalue=np.where(vec1==np.amin(vec1))

print(Jvalue)

MINmat1=np.amin(mat1)

A=np.array([[17,24,1,8,15],
            [23,5,7,14,16],
            [4,6,13,20,22],
            [10,12,19,21,3],
            [11,18,25,2,9]])
sumrow=np.sum(A,axis=-1).min()
sumcol=np.sum(A,axis=1).min()
sumdiag=np.sum(np.diag(A))
sumflip=np.sum(np.fliplr(A).diagonal())

if sumrow== sumcol == sumdiag == sumflip:
    print('this is a magic matrix')
M=np.random.rand(10,10)
MUL=M[1,1]
