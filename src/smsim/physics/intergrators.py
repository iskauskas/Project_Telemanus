#this is how we will numerically step an objects motion through time. This will be used to update the state of the system at each time step.
from smsim.simulation import state
from smsim.simulation.state import State
from smsim.physics.constants import g0

def euler_step(current_state: State, dt: float) -> State:
    #calculate the new state of the system after a time step dt using the Euler method, dt meaning delta time.
    a=-g0  #acceleration due to gravity
    new_t = current_state.t + dt
    new_x = current_state.x + current_state.v * dt
    new_v = current_state.v - g0 * dt  #assuming only gravity is acting on the system
    return State(new_t, new_x, new_v)