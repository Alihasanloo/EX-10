import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,500)
f1=pow(np.e,(-x/10))*np.sin(np.pi*x)
g1=x*pow(np.e,(-x/3))

plt.figure(1)

plt.subplot(2,1,1)
plt.plot(x,f1)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Fx diagram')
plt.legend('Fx')

plt.subplot(2,1,2)
plt.plot(x,g1)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Gx diagram')
plt.legend('Gx')

plt.show()

r0=0.8
teta = np.linspace(0, 2.*np.pi, 1000)
r=r0+np.cos(teta)
x=r*np.cos(teta)
y=r*np.sin(teta)

x1=(r+0.2)*np.cos(teta)
y1=(r+0.2)*np.sin(teta)

x2=(r+0.4)*np.cos(teta)
y2=(r+0.4)*np.sin(teta)
plt.figure(2)

plt.plot(x,y)
plt.legend('r0=0.8')
plt.plot(x1,y1)
plt.legend('r0=1.0')
plt.plot(x2,y2)
plt.legend('r0=1.2')




plt.show()
