import sys
import numpy as np
import matplotlib.pyplot as plt

def plotHist(data):
    xmin=data.min()
    xmax=data.max()
    nbins=100
    xwidth=(xmax-xmin)/nbins/2
    y,x = np.histogram(data,bins=nbins,range=[xmin,xmax],density=False)
    x=x[:-1]

    fig=plt.figure()
    plt.bar(x,y,width=xwidth)
    plt.xlim([xmin-xwidth,xmax+xwidth])

    plt.savefig("hist.pdf")
    plt.savefig("hist.png")
    return

data=np.loadtxt(sys.argv[1])
plotHist(data)
