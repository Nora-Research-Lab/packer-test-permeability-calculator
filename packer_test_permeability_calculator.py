import math

def lugeon_value(Q, L, P):
    """
    Compute Lugeon value.
    Q: flow rate (L/min)
    L: test section length (m)
    P: injection pressure (bar)
    Returns Lu (dimensionless)
    """
    return Q / (L * P)

def hydraulic_conductivity_constant_head(Q, L, D, P):
    """
    Compute hydraulic conductivity K (m/s) for constant head packer test.
    Q: flow rate (L/min) -> converted to m^3/s
    L: test section length (m)
    D: borehole diameter (m)
    P: injection pressure (bar)
    Uses effective radius r_e = 0.5 m.
    """
    # Convert Q to m^3/s
    Q_m3s = Q / 60000.0  # 1 L/min = 1.6667e-5 m^3/s, 1/60000 = 1.6667e-5
    r_w = D / 2.0
    r_e = 0.5  # common assumption
    # Water head from pressure: 1 bar = 10.2 m water
    dh = P * 10.2
    if dh <= 0 or L <= 0:
        raise ZeroDivisionError("Non-positive length or pressure head")
    K = (Q_m3s / (2 * math.pi * L * dh)) * math.log(r_e / r_w)
    return K

def hydraulic_conductivity_falling_head(d, h1, h2, t, L, D):
    """
    Compute K (m/s) for falling head packer test.
    d: standpipe inner diameter (m)
    h1: initial head (m)
    h2: final head (m)
    t: elapsed time (s)
    L: test section length (m)
    D: borehole diameter (m)
    Returns K in m/s.
    """
    a = math.pi * (d/2)**2  # standpipe cross-section area (m^2)
    A = math.pi * (D/2)**2  # borehole cross-section area (m^2)
    if h2 >= h1 or t <= 0 or A <= 0:
        raise ZeroDivisionError("Invalid falling head parameters")
    K = (a * L) / (A * t) * math.log(h1 / h2)
    return K

def permeability_classification(K):
    """Classify permeability based on K (m/s)."""
    if K < 1e-7:
        return "Very low"
    elif K < 1e-5:
        return "Low"
    elif K < 1e-3:
        return "Moderate"
    elif K < 1e-1:
        return "High"
    else:
        return "Very high"

def lugeon_classification(Lu):
    """Classify Lugeon value."""
    if Lu < 1:
        return "Tight"
    elif Lu <= 5:
        return "Low"
    elif Lu <= 25:
        return "Moderate"
    else:
        return "High"
