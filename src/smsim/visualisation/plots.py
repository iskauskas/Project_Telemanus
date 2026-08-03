#this is where I will try plot the graph of the simulation results
from typing import Callable
import matplotlib.pyplot as plt
from smsim.simulation.state import State
from smsim.physics.constants import g0

def plot_free_fall(
    history: list[State],
    acceleration_function: Callable[[State], float] | None = None,
) -> None:
    """Plot altitude, velocity, and acceleration over time.

    Args:
        history: the list of States recorded during the simulation.
        acceleration_function: the function used to compute acceleration
            during the simulation (e.g. gravity alone, or gravity + drag).
            If not provided, assumes constant gravity only (-g0), matching
            the original free-fall-only model.
    """
    times = [state.t for state in history]
    altitudes = [state.x for state in history]
    velocities = [state.v for state in history]

    if acceleration_function is not None:
        accelerations = [acceleration_function(state) for state in history]
    else:
        accelerations = [-g0 for _ in history]

    fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

    axes[0].plot(times, altitudes, color="tab:blue")
    axes[0].set_ylabel("Altitude (m)")
    axes[0].set_title("Free-Fall Simulation (Euler Integration)")
    axes[0].grid(True)

    axes[1].plot(times, velocities, color="tab:orange")
    axes[1].set_ylabel("Velocity (m/s)")
    axes[1].grid(True)

    axes[2].plot(times, accelerations, color="tab:green")
    axes[2].set_ylabel("Acceleration (m/s²)")
    axes[2].set_xlabel("Time (s)")
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()