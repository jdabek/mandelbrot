import matplotlib.pyplot as plt
import numpy as np

def complexSquare(z):
    return [z[0]**2-z[1]**2, 2.0*z[0]*z[1]]

def getMandelbrot(scaler,rotation,xcent,ycent):
    npt = 300
    xmin = xcent - scaler*2.0
    xmax = xcent + scaler*2.0
    dx = (xmax-xmin)/npt
    x = np.arange(xmin, xmax+dx/2., dx)
    ymin = ycent - scaler*2.0
    ymax = ycent + scaler*2.0
    dy = (ymax-ymin)/npt
    y = np.arange(ymin, ymax+dy/2., dy)
    xnpt = len(x)
    ynpt = len(y)
    mat = []
    
    for i in range(0,xnpt):
        vec = []
        a0 = x[i]
        for j in range(0,ynpt):
            b0 = y[j]
            a1 = a0 - xcent
            b1 = b0 - ycent
            a = xcent + a1*np.cos(2.0*np.pi*rotation) - b1*np.sin(2.0*np.pi*rotation)
            b = -ycent + a1*np.sin(2.0*np.pi*rotation) + b1*np.cos(2.0*np.pi*rotation)
            z = [0., 0.]
            zz = 0.0
            for n in range(0,40):
                z = complexSquare(z)
                z[0] += a
                z[1] += b
                zz = np.sqrt(z[0]**2+z[1]**2)
                if zz > 2.0:
                    break
            if zz < 1.0:
                zz = 0.0
            else:
                zz = np.log(zz)
            vec.append(zz)
        mat.append(vec)
    return [mat,x,y]

n = 0
for p in np.arange(0.0, 1.0, 0.001):
    n += 1
    weight = 1.0-np.cos(np.pi*p/0.99)**4
    [mat,x,y] = getMandelbrot(1.0e-6+np.abs(1.0-2.0*p)**3,2.0*p,-1.2390001*weight,0.41830152*weight)
    fig = plt.figure()
    fig.set_size_inches((1,1))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.set_cmap('jet')
    im = ax.imshow(np.array(mat).T, aspect='equal')
    im.set_clim(0.0,np.exp(1.0))
    plt.savefig('img_{:04d}.png'.format(n), dpi=300)
    plt.show()
