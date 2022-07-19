import matplotlib.pyplot as plt
import numpy as np

# X,Y plt for N = # & Exact Solution
def pltXY(X,Y,/,Llabel=None,Xexact=None,Yexact=None,Yexactlabel=None,\
    xlabel='X',ylabel='f(x)',multi=False,\
        title=None,fname=None,ftype='.pdf',legend=True,\
            displayon=False,printon=True,closefig=True,\
            gridon=False,xrange=None,yrange=None,\
            multiExact=False):
    """
    X:  Number of Intervals (N)
    Y:  error values abs(exact - result)*sqrt(N)
    Optional:   by position or variable declaration
    Llabel: the label for legend. must be string
    Yexact: To plot the exact solution
    Yexactlabel:    to pass optional label for legend of
        the Yexact solution
    xlabel: the label for x-axis must be string
        default is 'X'
    ylabel: the label for y-axis must be string
        default is 'f(x)'
    multi:  default is False, set to true if passed
        X and Y are multidimensional and need to be
        plotted in the same fig
    title:  title to display on plt
        if nothing is passed then no title is shown
    fname:  name of the file to be saved
        if nothing is passed then not saved
    ftype:  type of file to save must pass as a string
        defualt is .png
        avaible: .png, .jpeg. .jpg, .pdf
    legend: shows legend with the convergence rates
        default is on with True
    displayon:  default is False, set to True to show plt
    printon:    default is True, set to false to turn off
        all printing to screen
    closefig:   defualt is True, closes figure when done
    gridon:     defualt is False, turns grid lines on
    xrange:     defulat is standard, add matrix [start,end]
        to add plot xrange
    yrange:     defulat is standard, add matrix [start,end]
        to add plot yrange
    """
    # begin function
    fig = plt.figure(1)
    if printon:
        pass
    if multi:
        Ny = len(Y)
        for n in range(Ny):
            plt.plot(X,Y[n],label=Llabel[n])
    else:
        plt.plot(X,Y,label=Llabel)
    if Yexact is not None:
        if Xexact is None:
            Xexact = X
        if multiExact:
            Ny = len(Yexact)
            for n in range(Ny):
                plt.plot(Xexact,Yexact[n],'--',label=Yexactlabel[n])
        else:
            plt.plot(Xexact,Yexact,'r--',label=Yexactlabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xrange is not None:
        plt.xlim(xrange)
    if yrange is not None:
        plt.ylim(yrange)
    if title is not None:
        plt.title(title)
    if legend is not None:
        plt.legend()
    if gridon:
        plt.grid()
    if displayon:
        plt.show()
    if fname is not None:
        plt.savefig(fname+ftype)
    if closefig:
        plt.close(fig)

# X,Y plt for N = # & Exact Solution
def pltXYscatter(X,Y,/,Llabel=None,Xexact=None,Yexact=None,Yexactlabel=None,\
    xlabel='X',ylabel='f(x)',multi=False,\
        title=None,fname=None,ftype='.pdf',legend=True,\
            displayon=False,printon=True,closefig=True,\
            gridon=False,xrange=None,yrange=None,\
            multiExact=False):
    """
    X:  Number of Intervals (N)
    Y:  error values abs(exact - result)*sqrt(N)
    Optional:   by position or variable declaration
    Llabel: the label for legend. must be string
    Yexact: To plot the exact solution
    Yexactlabel:    to pass optional label for legend of
        the Yexact solution
    xlabel: the label for x-axis must be string
        default is 'X'
    ylabel: the label for y-axis must be string
        default is 'f(x)'
    multi:  default is False, set to true if passed
        X and Y are multidimensional and need to be
        plotted in the same fig
    title:  title to display on plt
        if nothing is passed then no title is shown
    fname:  name of the file to be saved
        if nothing is passed then not saved
    ftype:  type of file to save must pass as a string
        defualt is .png
        avaible: .png, .jpeg. .jpg, .pdf
    legend: shows legend with the convergence rates
        default is on with True
    displayon:  default is False, set to True to show plt
    printon:    default is True, set to false to turn off
        all printing to screen
    closefig:   defualt is True, closes figure when done
    gridon:     defualt is False, turns grid lines on
    xrange:     defulat is standard, add matrix [start,end]
        to add plot xrange
    yrange:     defulat is standard, add matrix [start,end]
        to add plot yrange
    """
    # begin function
    fig = plt.figure(1)
    if printon:
        pass
    if multi:
        Ny = len(Y)
        for n in range(Ny):
            plt.plot(X,Y[n],label=Llabel[n])
    else:
        plt.plot(X,Y,label=Llabel)
    if Yexact is not None:
        if Xexact is None:
            Xexact = X
        if multiExact:
            Ny = len(Yexact)
            for n in range(Ny):
                plt.plot(Xexact,Yexact[n],'--',label=Yexactlabel[n])
        else:
            plt.plot(Xexact,Yexact,'ro',label=Yexactlabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xrange is not None:
        plt.xlim(xrange)
    if yrange is not None:
        plt.ylim(yrange)
    if title is not None:
        plt.title(title)
    if legend is not None:
        plt.legend()
    if gridon:
        plt.grid()
    if displayon:
        plt.show()
    if fname is not None:
        plt.savefig(fname+ftype)
    if closefig:
        plt.close(fig)

# LogLog plt for convergence studies
def pltloglog(X,Y,/,Yexact=None,Yexactlabel=None,\
    xlabel='Number of Intervals (N)',ylabel='Error (Exact - Result)',\
        title=None,fname=None,ftype='.pdf',legend=True,\
            displayon=False,printon=True,closefig=True,\
                gridon=False):
    """
    X:  Number of Intervals (N)
    Y:  error values abs(exact - result)*sqrt(N)
    Optional:   by position or variable declaration
    Yexact: To plot the exact solution
    Yexactlabel:    to pass optional label for legend of
        the Yexact solution
    xlabel: the label for x-axis must be string
        default is 'Number of Intervals (N)'
    ylabel: the label for y-axis must be string
        default is 'Error (Exact - Result)'
    title:  title to display on plt
        if nothing is passed then no title is shown
    fname:  name of the file to be saved
        if nothing is passed then not saved
    ftype:  type of file to save must pass as a string
        defualt is .png
        avaible: .png, .jpeg. .jpg, .pdf
    legend: shows legend with the convergence rates
        default is on with True
    displayon:  default is False, set to True to show plt
    printon:    default is True, set to false to turn off
        all printing to screen
    closefig:   defualt is True, closes figure when done
    gridon:     defualt is False, turns grid lines on
    """
    # begin function
    fig = plt.figure(1)
    # solve for convergence rate
    logx = np.log(X)
    logy = np.log(Y)
    m,_ = np.polyfit(logx,logy,1)
    if printon:
        print('Convergence Rate = %.2f'%(m))
    plt.loglog(X,Y,label='Rate=%.2f'%(m))
    if Yexact is not None:
        plt.loglog(X,Yexact,label=Yexactlabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    if legend is not None:
        plt.legend()
    if gridon:
        plt.grid()
    if displayon:
        plt.show()
    if fname is not None:
        plt.savefig(fname+ftype)
    if closefig:
        plt.close(fig)
# end of loglogplt()


# LogLog plt for convergence studies
def pltsemilogy(X,Y,/,Llabel=None,Yexact=None,Yexactlabel=None,\
    xlabel='Number of Iterations',ylabel='Error (Exact - Result)',\
        multi=False,title=None,fname=None,ftype='.pdf',legend=True,\
            displayon=False,printon=True,closefig=True):
    """
    X:  Number of Intervals (N)
    Y:  error values abs(exact - result)*sqrt(N)
    Optional:   by position or variable declaration
    Llabel: the label for legend. must be string
    Yexact: To plot the exact solution
    Yexactlabel:    to pass optional label for legend of
        the Yexact solution
    xlabel: the label for x-axis must be string
        default is 'Number of Iterations'
    ylabel: the label for y-axis must be string
        default is 'Error (Exact - Result)'
    multi:  default is False, set to true if passed
        X and Y are multidimensional and need to be
        plotted in the same fig
    title:  title to display on plt
        if nothing is passed then no title is shown
    fname:  name of the file to be saved
        if nothing is passed then not saved
    ftype:  type of file to save must pass as a string
        defualt is .png
        avaible: .png, .jpeg. .jpg, .pdf
    legend: shows legend with the convergence rates
        default is on with True
    displayon:  default is False, set to True to show plt
    printon:    default is True, set to false to turn off
        all printing to screen
    closefig:   defualt is True, closes figure when done
    """
    # begin function
    fig = plt.figure(1)
    # solve for convergence rate
    if multi:
        Nx = len(X)
        Ny = len(Y)
        assert Nx == Ny, "X and Y not same length"
        for n in range(Nx):
            logy = np.log(Y[n])
            m,_ = np.polyfit(X[n],logy,1)
            if printon:
                print(Llabel[n],'Convergence Rate = %.2f'%(m))
            plt.semilogy(X[n],Y[n],label=Llabel[n]+', Rate=%.2f'%(m))
    else:
        logy = np.log(Y)
        m,_ = np.polyfit(X,logy,1)
        if printon:
            print('Convergence Rate = %.2f'%(m))
        plt.semilogy(X,Y,label='Rate=%.2f'%(m))
    if Yexact is not None:
        plt.semilogy(X,Y,label=Yexactlabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    if legend is not None:
        plt.legend()
    if displayon:
        plt.show()
    if fname is not None:
        plt.savefig(fname+ftype)
    if closefig:
        plt.close(fig)
# end of loglogplt()

# LogLog plt for convergence studies
def pltsemilogx(X,Y,/,Llabel=None,Yexact=None,Yexactlabel=None,\
    xlabel='Number of Iterations',ylabel='Error (Exact - Result)',\
        multi=False,title=None,fname=None,ftype='.pdf',legend=True,\
            displayon=False,printon=True,closefig=True):
    """
    X:  Number of Intervals (N)
    Y:  error values abs(exact - result)*sqrt(N)
    Optional:   by position or variable declaration
    Llabel: the label for legend. must be string
    Yexact: To plot the exact solution
    Yexactlabel:    to pass optional label for legend of
        the Yexact solution
    xlabel: the label for x-axis must be string
        default is 'Number of Iterations'
    ylabel: the label for y-axis must be string
        default is 'Error (Exact - Result)'
    multi:  default is False, set to true if passed
        X and Y are multidimensional and need to be
        plotted in the same fig
    title:  title to display on plt
        if nothing is passed then no title is shown
    fname:  name of the file to be saved
        if nothing is passed then not saved
    ftype:  type of file to save must pass as a string
        defualt is .png
        avaible: .png, .jpeg. .jpg, .pdf
    legend: shows legend with the convergence rates
        default is on with True
    displayon:  default is False, set to True to show plt
    printon:    default is True, set to false to turn off
        all printing to screen
    closefig:   defualt is True, closes figure when done
    """
    # begin function
    fig = plt.figure(1)
    # solve for convergence rate
    if multi:
        Nx = len(X)
        Ny = len(Y)
        assert Nx == Ny, "X and Y not same length"
        for n in range(Nx):
            logx = np.log(X[n])
            m,_ = np.polyfit(X[n],logx,1)
            if printon:
                print(Llabel[n],'Convergence Rate = %.2f'%(m))
            plt.semilogx(X[n],Y[n],label=Llabel[n])#+', Rate=%.2f'%(m))
    else:
        logx = np.log(X)
        m,_ = np.polyfit(X,logx,1)
        if printon:
            print('Convergence Rate = %.2f'%(m))
        plt.semilogx(X,Y,label='Rate=%.2f'%(m))
    if Yexact is not None:
        plt.semilogx(X,Y,label=Yexactlabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    if legend:
        plt.legend()
    if displayon:
        plt.show()
    if fname is not None:
        plt.savefig(fname+ftype)
    if closefig:
        plt.close(fig)
# end of loglogplt()
