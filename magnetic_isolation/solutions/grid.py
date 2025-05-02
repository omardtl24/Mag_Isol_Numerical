import numpy as np
import pandas as pd
from .analytical import u_values

def get_fixed_k(k=1, minb=-1,maxb=1,num_points = 100,fun = u_values):
    """
    Calculate the roots of the specified equation for a fixed value of k.
    
    Args:
        k (float): Coefficient of u^2.
        minb (float): Minimum value of b.
        maxb (float): Maximum value of b.
        num_points (int): Number of points to sample between minb and maxb.
        fun (function): Function to calculate the roots.
        
    Returns:
        pd.DataFrame: A DataFrame containing the values of b, u_real, and u_complex.
    """
    bparams = np.linspace(minb,maxb,num_points)
    expanded_results = {'b': [], 'u_real': [], 'u_complex':[]}

    for b in bparams:
        u_vals = fun(k, b)
        for u in u_vals:
            expanded_results['b'].append(b)
            expanded_results['u_real'].append(np.real(u))
            expanded_results['u_complex'].append(np.imag(u))

    final_df =  pd.DataFrame(expanded_results)
    final_df['k'] = k
    return final_df

def get_fixed_b(b=1, minb=-1,maxb=1,num_points = 100, fun = u_values):
    """
    Calculate the roots of the specified equation for a fixed value of b.
    
    Args:
        b (float): Coefficient of u^2.
        minb (float): Minimum value of b.
        maxb (float): Maximum value of b.
        num_points (int): Number of points to sample between minb and maxb.
        fun (function): Function to calculate the roots.
    
    Returns:
        pd.DataFrame: A DataFrame containing the values of k, u_real, and u_complex.
    """
    kparams = np.linspace(minb,maxb,num_points)
    expanded_results = {'k': [], 'u_real': [], 'u_complex':[]}

    for k in kparams:
        u_vals = fun(k, b)
        for u in u_vals:
            expanded_results['k'].append(k)
            expanded_results['u_real'].append(np.real(u))
            expanded_results['u_complex'].append(np.imag(u))

    final_df =  pd.DataFrame(expanded_results)
    final_df['b'] = b
    return final_df

def get_grid(mink = -1, maxk = 1, minb = -1, maxb = 1, num_points = 100, fun = u_values):
    """
    Calculate the roots of the specified equation for a grid of k and b values.
    
    Args:
        mink (float): Minimum value of k.
        maxk (float): Maximum value of k.
        minb (float): Minimum value of b.
        maxb (float): Maximum value of b.
        num_points (int): Number of points to sample between mink and maxk, and minb and maxb.
        fun (function): Function to calculate the roots.
        
    Returns:
        pd.DataFrame: A DataFrame containing the values of k, b, u_real, and u_complex.
    """
    kparams = np.linspace(mink,maxk,num_points)
    bparams = np.linspace(minb,maxb,num_points)
    K,B = np.meshgrid(kparams, bparams)

    k_flat = K.flatten()
    b_flat = B.flatten()

    expanded_results = {'k': [], 'b': [], 'u_real': [], 'u_complex':[]}

    for k,b in zip(k_flat, b_flat):
        u_vals = fun(k, b)
        for u in u_vals:
            expanded_results['k'].append(k)
            expanded_results['b'].append(b)
            expanded_results['u_real'].append(np.real(u))
            expanded_results['u_complex'].append(np.imag(u))

    final_df =  pd.DataFrame(expanded_results)
    return final_df