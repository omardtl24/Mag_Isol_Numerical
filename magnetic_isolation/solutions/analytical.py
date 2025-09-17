import numpy as np

cubic_poly = lambda k,b,u : u**3 + k*u**2 + u + b
theta_edo = lambda k, b, t : t**(3/2) + k*t + t**(1/2) + b
delta = lambda k,b : 18*k*b + k**2 - 4 - 4*k**3*b - 27*b**2

def u_values(k, b):
    """
    Calculate the roots of the cubic polynomial u^3 + k*u^2 + u + b = 0.
    The roots are the values of u that satisfy the equation.
    The function uses Cardano's method to find the roots.
    Args:
        k (float): Coefficient of u^2.
        b (float): Constant term.
    
    Returns:
        np.ndarray: An array containing the roots of the cubic polynomial.
    """
    delta = 18*k*b + k**2 - 4 - 4*k**3*b - 27*b**2

    if delta == 0:
        if (k == np.sqrt(3) and b == np.sqrt(3)/9) or (k == -np.sqrt(3) and b == -np.sqrt(3)/9):
            return np.array([-k/3, -k/3, -k/3])
        else:
            arg = 2*k**3 - 9*k + 27*b
            u1 = (arg / (9 - 3*k**2)) - k/3
            u2 = (arg / (6*k**2 - 18)) - k/3
            return np.array([u1, u2, u2])
    elif delta > 0:
        coef = (2/3) * np.sqrt(k**2 - 3)
        arg = ((2*k**3 - 9*k + 27*b) / (18 - 6*k**2)) * np.sqrt(9 / (k**2 - 3))
        u1 = coef * np.cos((1/3) * np.arccos(arg)) - k/3
        u2 = coef * np.cos((1/3) * np.arccos(arg) + (2*np.pi/3)) - k/3
        u3 = coef * np.cos((1/3) * np.arccos(arg) + (4*np.pi/3)) - k/3
        return np.array([u1, u2, u3])
    else:
        A1 = -(54*k**3 - 243*k + 729*b)
        A2 = np.sqrt(-19683*delta)
        C = np.cbrt
        u1 = -k/3 + (C(4)/18) * (C(A1 + A2) + C(A1 - A2))
        u2_real = -k/3 - (C(4)/36) * (C(A1 + A2) + C(A1 - A2))
        u2_imag = (np.sqrt(3) * C(4) / 36) * (C(A1 + A2) - C(A1 - A2))
        u2 = u2_real + 1j * u2_imag
        u3 = u2_real - 1j * u2_imag
        return np.array([u1, u2, u3])

def theta_values(k, b):
    """
    Calculate the solutions for the theta equuation for the given k and b.
    The theta values are gotten from the roots of the cubic polynomial.

    Args:
        k (float): Coefficient of u^2.
        b (float): Constant term.
    
    Returns:
        np.ndarray: An array containing the theta values.
    """
    u =  u_values(k, b)
    u = u[np.real(u)>0]
    return u**2