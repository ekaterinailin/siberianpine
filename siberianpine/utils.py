import numpy as np

def generate_random_power_law_distribution(a, b, g, size=1, seed=None):
    """
    Power-law generator for pdf(x)\propto x^{g-1} for a<=x<=b
    """
    if seed is not None:
        np.random.seed(seed)
    r = np.random.random(size=size)
    ag, bg = a**g, b**g
    return (ag + (bg - ag)*r)**(1./g)
