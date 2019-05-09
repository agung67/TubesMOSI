#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import random
from random import uniform, shuffle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import matplotlib.animation as animation
from IPython.display import HTML


# In[4]:


#inisialisasi
M    = 100   #batas maksimum lintasan
p    = 0.3  #probability
v0   = 0    #kecepatan awal
N    = 10   #jumlah kendaraan
tmax = 100  #batas waktu untuk di iterasikan
dt   = 1    #jarak antar waktu
vmax = 5    #batas kecepatan maksimum
val  = 0    #kepadatan per satuan waktu
x    = []   #Letak x pada tiap mobil
y    = []   #inisialisasi y agar titik mobil nya berada di tengah simulasi
xi   = []   #simpan tiap iterasi array x
yi   = []   #simpan nilai y
v    = []   #inisialisasi nilai v
w    = []
warna= []
data = []
nilai_awal = []
lewat = []  #berapa kali mobil melewati posisi awal
simpan = []  #mengecek apakah mobil sudah melewati posisi awal
cek = []
density = 0

for i in range(N):
    x.append(np.random.uniform(0,M))
    y.append(5)
    v.append(np.random.uniform(0,vmax))
    lewat.append(-1)
    simpan.append(-1)
    cek.append(0)
    w.append(np.random.uniform(0,M))

x.sort()
nilai_awal = x.copy()


# In[5]:


for i in range(tmax):
    j = 0
    for j in range(N):
        d = 0 
        d1 = 0
        d2 = 0
        if((j + 1) in range(N)):
            d2 = x[j + 1]
            d1 = x[j]
            if(d2 < d1):
                d1 = M - d1
                d  = d1 + d2
            else:
                d  = d2 - d1
        else:
            d2 = x[0]
            d1 = x[j - 1]
            if(d2 < d1):
                d1 = M - d1
                d  = d1 + d2
            else:
                d  = d2 - d1
        v[j] = min((v[j] + 1), vmax)
        v[j] = min(v[j], (d - 1))
        v[j] = max(0, (v[j] - 1)) if uniform(0,1) < p else v[j] 
        x[j] = x[j] + v[j]
        cek[j] = cek[j] - v[j]
        if(x[j] >= M):
            x[j] = x[j] - M
        
        
        if((cek[j] >= 0) and (simpan[j] != lewat[j])):
            simpan[j] += 1
        
        if((simpan[j] == lewat[j]) and (x[j] >= nilai_awal[j]) and (cek[j] < 0)):
            lewat[j] += 1
            cek[j] = (M - x[j]) + nilai_awal[j]
        
    xi.append(np.array(x))
    yi.append(np.array(y))
    data.append(np.array([x,y]))
    warna.append(np.array(w))
    
    
    if(i in range(80,90)):
        j = 0
        for j in range(N):
            if((x[j] >= 80) and (x[j] <= 90)):
                density += 1
        
    


# In[6]:


print(density)


# In[7]:


density = density/M
print("nomor 2 : ",density)
print("nomor 3 : ")


# In[8]:


i = 0
for i in range(N):
    print("mobile ke-",i+1, ":",lewat[i]/tmax)


# In[9]:


#simulation
def update_line(num, xi, line,) : #Fungsi untuk mengupdate grafik
        line.set_xdata(xi[num])
        line.set_ydata(5)
        return line,

fig = plt.figure()
ax = fig.add_subplot(111)
l, = ax.plot([], [], 'o')

ax.set_ylim(4,6)
ax.set_xlim(0,M)

ani = animation.FuncAnimation(fig, update_line, frames = 50, fargs = (xi,l,))


# In[9]:


HTML(ani.to_jshtml())


# In[10]:


# showing image

plt.figure()
plt.scatter(xi[0], yi[0], marker=".", c=warna[0])
plt.show()


# In[11]:


# showing image

plt.figure()
plt.scatter(xi[2], yi[2], marker=".", c=warna[1])
plt.show()


# In[12]:


# showing image

plt.figure()
plt.scatter(xi[3], yi[3], marker=".", c=warna[3])
plt.show()


# In[13]:


# showing image

plt.figure()
plt.scatter(xi[4], yi[4], marker=".", c=warna[4])
plt.show()


# In[14]:


# showing image

plt.figure()
plt.scatter(xi[5], yi[5], marker=".", c=warna[3])
plt.show()


# In[ ]:





# In[15]:


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=-1)


# In[ ]:




