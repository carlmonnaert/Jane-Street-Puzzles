import numpy as np
from itertools import combinations

def simulate_parade(n_sims=10_000_000, theta=1e-2):
    # 1. Generate uniform points on a 3D sphere using normalized Gaussian vectors
    vecs = np.random.normal(size=(n_sims, 6, 3))
    planets = vecs / np.linalg.norm(vecs, axis=2, keepdims=True)
    
    # 2. Event A: Planets are visible from the base (z > 0)
    base_visible = np.all(planets[:, :, 2] > 0, axis=1)
    
    # 3. Event A': Planets are visible from the tower
    # A tower extends the horizon angle by theta. The new z-bound is -sin(theta).
    tower_visible = np.all(planets[:, :, 2] > -np.sin(theta), axis=1)
    
    # 4. Event E: Planets share SOME hemisphere
    some_hemisphere = np.zeros(n_sims, dtype=bool)
    
    # Check all 15 boundary planes formed by pairs of planets
    for i, j in combinations(range(6), 2):
        normals = np.cross(planets[:, i, :], planets[:, j, :])
        dots = np.einsum('nij,nj->ni', planets, normals)
        
        # If all 6 planets are on the same side of the plane, a shared hemisphere exists
        valid_pos = np.all(dots >= -1e-8, axis=1)
        valid_neg = np.all(dots <= 1e-8, axis=1)
        
        some_hemisphere |= valid_pos | valid_neg

    # 5. Calculate conditional probabilities given Event E occurred
    valid_sims = np.sum(some_hemisphere)
    
    # Alpha = P(Base | Some)
    # Note: base_visible is strictly a subset of some_hemisphere
    alpha_sim = np.sum(base_visible) / valid_sims
    
    # Extended probability = P(Tower | Some)
    tower_given_some = np.sum(tower_visible & some_hemisphere) / valid_sims
    
    # Beta is the linear coefficient: (P_new - P_old) / theta
    beta_sim = (tower_given_some - alpha_sim) / theta
    
    # 6. Output results
    print(f"Simulations: {n_sims:,}")
    print(f"Theta:       {theta}")
    print("-" * 40)
    print(f"Alpha (sim):    {alpha_sim:.5f} | Exact: {1/32:.5f} | Rel Error: {abs(alpha_sim - 1/32) / (1/32):.2%}")
    print(f"Beta  (sim):    {beta_sim:.5f} | Exact: {3/16:.5f} | Rel Error: {abs(beta_sim - 3/16) / (3/16):.2%}")

if __name__ == "__main__":
    simulate_parade()