#this will test for numerical integrators and check them against the exact solutions
import math
import pytest
from smsim.simulation.state import State
from smsim.simulation.simulator import run_simulation
from smsim.physics.integrators import euler_step
from smsim.physics.constants import g0

def test_euler_step_free_fall():
    initial_height = 100.0  # meters
    initial = State(t=0, x=initial_height, v=0)  # initial state: 100 meters above the ground, with no initial velocity

    history = run_simulation(initial_state=initial, dt=0.001, step_function=euler_step, max_time=100)
    final = history[-1]  # get the final state of the system after the simulation has run

    # Calculate the exact solution for free fall
    expected_landing_time = math.sqrt(2 * initial_height / g0)
    expected_landing_velocity = -g0 * expected_landing_time

    #allow a tolerance of 0.05 due to a small tolerance rather than an exact match
    assert final.t == pytest.approx(expected_landing_time, abs=0.05)
    assert final.v == pytest.approx(expected_landing_velocity, abs=0.5) 
