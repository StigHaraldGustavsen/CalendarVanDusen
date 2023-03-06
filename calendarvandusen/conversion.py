import numpy as np

def CVD_to_greek(A, B, C=0.0):
    alpha = A+(100*B)
    delta = (-10e4*B)/alpha
    beta = (-10e8*C)/alpha
    
    res = {'alpha':alpha,'delta':delta/10, 'beta':beta/10,} 
    # still not figuerd out why i get 1/10 on delta and beta
    
    return res 

def CVD_to_latin(alpha, delta, beta=0.0):
    A = alpha+((alpha*delta)/100)
    B = -((alpha*delta)/(100**2))
    C = -((alpha*beta)/(109**4))
    
    res = {'A':A,'B':B, 'C':C} 
    return res 



#Move this out to tests later
if __name__ == '__main__':
    print('A = 3.9083e-3, B:-5.775e-7 C:-4.183e-12')
    print(CVD_to_greek(3.9083e-3,-5.775e-7,-4.183e-12))

    print('')
    print('another example calculation with SSE here:')
    
    R0 = 100.0044
    A = 3.91e-3
    B = -5.86e-7
    C = 0
    t = np.arange(-10,51)

    #The latin polynomial
    poly = R0*(1+((A*t)+(B*t**2)))
    
    #getting the greek coefisient
    print('Referance : A:'+str(A)+' B:'+str(B)+' C='+str(C))
    abg = CVD_to_greek(A,B,C)
    print('converted to: '+str(abg))

    #Calculate with the greek wierd polynomial.
    t_abg = R0+R0*abg['alpha']*(t-abg['delta']*((t/100)-1)*(t/100)-abg['beta']*((t/100)-1)*((t/100)**3))
    
    #Calculating the sum of the squared errors of points from -10°C to 50°C
    sse = 0 
    for i in range(len(t)):
        sse += (poly[i]-t_abg[i])**2
    print('Sum square error: '+str(sse))

    #covert back
    
    print('convert back ')
    
    abc = CVD_to_latin(abg['alpha'],abg['delta'],abg['beta'])
    t_abc = R0*(1+((abc['A']*t)+(abc['B']*t**2)))
    print(abg)
    
    print('Referance : A:'+str(A)+' B:'+str(B)+' C='+str(C))
    print(abc) 
    

    #Calculating the sum of the squared errors of points from -10°C to 50°C
    sse = 0 
    for i in range(len(t)):
        sse += (t_abg[i]-t_abc[i])**2
    print('Sum square error: '+str(sse))