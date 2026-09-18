import math

def calculate_bouguer_anomaly(latitude, elevation, observed_gravity, reduction_density=2.67, terrain_correction=0.0):
    """
    Calculate Bouguer gravity anomaly based on input parameters.
    
    Args:
        latitude (float): Latitude in decimal degrees
        elevation (float): Station elevation above sea level in meters
        observed_gravity (float): Observed gravity in mGal
        reduction_density (float): Reduction density in g/cm³ (default 2.67)
        terrain_correction (float): Terrain correction in mGal (default 0.0)
    
    Returns:
        dict: Dictionary containing calculated values
    """
    # Convert latitude to radians
    phi_rad = math.radians(abs(latitude))
    
    # Calculate theoretical sea-level gravity using IGF 1967
    sin_phi_sq = math.sin(phi_rad) ** 2
    sin_phi_4th = sin_phi_sq ** 2
    g_theory = 978031.846 * (1 + 0.005278895 * sin_phi_sq + 0.000023462 * sin_phi_4th)
    
    # Calculate free-air correction (0.3086 mGal/m)
    free_air_correction = 0.3086 * elevation
    
    # Calculate free-air anomaly
    free_air_anomaly = observed_gravity - g_theory + free_air_correction
    
    # Calculate simple Bouguer correction (0.04193 * density * h mGal)
    bouguer_correction = 0.04193 * reduction_density * elevation
    
    # Calculate simple Bouguer anomaly
    simple_bouguer_anomaly = free_air_anomaly - bouguer_correction
    
    # Calculate complete Bouguer anomaly (with terrain correction)
    complete_bouguer_anomaly = simple_bouguer_anomaly + terrain_correction
    
    return {
        'g_theory': g_theory,
        'free_air_correction': free_air_correction,
        'bouguer_correction': bouguer_correction,
        'free_air_anomaly': free_air_anomaly,
        'simple_bouguer_anomaly': simple_bouguer_anomaly,
        'complete_bouguer_anomaly': complete_bouguer_anomaly
    }
