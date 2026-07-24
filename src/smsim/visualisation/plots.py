#this is where I will try plot the graph of the simulation results
import matplotlib.pyplot as plt
from smsim.simulation.state import State
from smsim.physics.constants import g0

def plot_free_fall(history: list[State]) -> None:
    """ plot altitude, velocity and acceleration over time for a free-fall simulation
    Args:
        history: The list of states recorded during the simulation
    """
    times = [state.t for state in history]
    altitudes = [state.x for state in history]
    velocities = [state.v for state in history]
    #for this current free fall model I will just use acceleration as a constant -g0 since for now gravity is the only force acting on it.
    accelerations = [-g0 for _ in history]

    fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

    axes[0].plot(times, altitudes, color="tab:blue")
    axes[0].set_ylabel("Altitude (m)")
    axes[0].set_title("Free-Fall simulation (Euler Integration)")
    axes[0].grid()

    axes[1].plot(times, velocities, color="tab:orange")
    axes[1].set_ylabel("Velocity (m/s)")
    axes[1].grid()

    axes[2].plot(times, accelerations, color="tab:green")
    axes[2].set_ylabel("Acceleration (m/s²)")
    axes[2].grid()


    plt.tight_layout()
    plt.show()