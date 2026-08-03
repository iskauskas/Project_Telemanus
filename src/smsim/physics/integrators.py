#this is how we will numerically step an objects motion through time. This will be used to update the state of the system at each time step.
#now going to revamp it with the new drag

from typing import Callable
from smsim.simulation.state import State

def euler_step(
        state: State,
        dt: float,
        acceleration_function: Callable[[State], float],
) -> State:
    """ Advance the state forward a step
    
    Args:
        state: the current State (t, x, v)
        dt: the time step in seconds
        acceleration_function: a function that takes the state and returns the acceleration acting on it at that point
    Returns:
        The new State after stepping forward by dt
    """

    a = acceleration_function(state)

    new_v = state.v + a * dt
    new_x = state.x + state.v * dt
    new_t = state.t + dt

    return State(t=new_t, x=new_x, v=new_v)