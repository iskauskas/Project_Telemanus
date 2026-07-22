#this will be the time stepping loop that will run the simulation using the intergrator. it will also create a history of the states of the system at each time step. This will be used to plot the results of the simulation.
from typing import Callable, Callable
from smsim.simulation.state import State

def run_simulation(
        initial_state: State,
        dt: float,
        step_function: Callable[[State, float], State], #basically telling it that any state or float that gets put in will be turned into a State object
        max_time: float = 100,
) -> list[State]:
    """
    Run the simulation using the provided step function and initial state.

    :param initial_state: The initial state of the system.
    :param dt: The time step for the simulation.
    :param step_function: A callable that takes the current state and dt, and returns the new state.
    :param max_time: The maximum time to run the simulation.
    :return: A list of states representing the simulation over time.
    """
    history: list[State] = [initial_state]
    current_state = initial_state

    while current_state.x > 0 and current_state.t < max_time: #the max time part is just a safety measure to prevent infinite loops in case something goes wrong. The current_state.x > 0 part is to stop the simulation when the object hits the ground.
        current_state = step_function(current_state, dt)
        history.append(current_state)
    return history