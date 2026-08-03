#free fall simulation including atmospheric drag.

from smsim.simulation.state import State
from smsim.simulation.simulator import run_simulation
from smsim.physics.integrators import euler_step
from smsim.physics.constants import g0, rho0
from smsim.physics.drag import drag_acceleration
from smsim.visualisation.plots import plot_free_fall

#we will use a rough bowling ball for this example to keep it simple

mass = 7.0  # kg
drag_coefficient = 0.47  # dimensionless
radius = 0.11  # m
area = 3.14159 * radius ** 2  # m^2

def total_acceleration(state: State) -> float:
    """Net acceleration due to gravity and drag"""
    a_drag = drag_acceleration(state.v, mass, drag_coefficient, area, rho0)
    return -g0 + a_drag  # gravity acts downward, drag acts opposite to velocity

def step(state: State, dt: float) -> State:
    """Wraps euler_step, binding in our specific acceleration model."""
    return euler_step(state, dt, total_acceleration)

initial = State(t=0.0, x=100.0, v=0.00)  # initial state: 100 meters above ground, no initial velocity
history = run_simulation(initial_state=initial, dt=0.01, step_function=step)

final = history[-1]
print(f"Landed after {final.t:.2f} s, at velocity of {final.v:.2f} m/s, at height {final.x:.2f} m"  )

plot_free_fall(history, acceleration_function=total_acceleration)  # plot the results of the simulation to be graphed