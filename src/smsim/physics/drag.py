#Aerodynamic drag calculations

def drag_acceleration(
        v: float,
        mass: float,
        drag_coefficient: float,
        area: float,
        air_density: float,
) -> float:

    '''calculate the acceleration caused by the opposing drag

    Args:
        v: current velocity, in m/s. positive is up.
        mass: mass of the object in kg
        drag_coefficient: no dimension drag coefficient of the object
        area: cross sectional area facing the air, in m^2
        air_density: density of the surrounding air in kg/m^3

    Returns:
        the acceleration due to drag opposing the velocity
        '''
    return -(0.5 * air_density * drag_coefficient * area / mass) * v * abs(v)  # the abs(v) is to make sure that the drag is always opposing the motion