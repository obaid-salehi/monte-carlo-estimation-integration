# Monte Carlo Estimation of Integrals

A Python simulation illustrating how random sampling and direct averaging can be used to estimate definite integrals, visualising the convergence of the estimate as more samples are drawn.

---

## Overview
This project applies the **Monte Carlo method** to approximate definite integrals using uniform random sampling.  
The simulation shows how averaging over a growing number of random points leads to an increasingly stable estimate of the integral — a direct visualisation of the **Law of Large Numbers** in action.

---

## Tools & Libraries
- **Python**
- **NumPy** — random number generation & vectorised arithmetic  
- **matplotlib** — visualising the direct averaging process  
- **time** — measuring runtime for performance comparison

---

## Methodology
1. Generate a uniform random sample of n values that are the x co-ordinates
2. Apply the vectorised function that is to be integrated on the sample
3. Calculate the average value of f(x) using np.mean()
4. Multiply average value by range of bounds to get an estimate

---

## Results
- Most of the simulations carried out came within **<1%** off of the actual value of the integral. 
- Vectorised implementation with **NumPy** reduced runtime by **~99.6%** compared to a standard loop-based version.  

---

## Key Takeaways
- Monte Carlo integration provides a probabilistic method for numerical estimation of integrals.
- The process of direct averaging heavily simplifies the computation of the integral. 
- Vectorisation significantly improves computational efficiency without changing estimator accuracy.

