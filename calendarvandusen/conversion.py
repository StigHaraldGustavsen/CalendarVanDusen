def CVD_to_greek(A, B, C=0.0):
    alpha = A+(100*B)
    delta = (-10e4*B)/alpha
    beta = (-10e8*C)/alpha
    
    res = {'alpha':alpha,'delta':delta/10, 'beta':beta/10,} 
    # still not figuerd out why i get 1/10 on delta and beta
    
    return res 