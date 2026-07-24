#This is where we can run the free fall tests. this will be used to test the physics of the simulation and make sure that the results are accurate. This will be used to test the integrators and make sure that they are working correctly.
print("Running free fall test...") #print a message to indicate that the free fall test is running.
from smsim.simulation.state import State
from smsim.simulation.simulator import run_simulation
from smsim.physics.integrators import euler_step

initial = State(t=0, x=100, v=0) #initial state of the system. 100 meters above the ground, with no initial velocity.

history = run_simulation(initial, dt=0.001, step_function=euler_step, max_time=100) #run the simulation with a time step of 0.1 seconds and a maximum time of 100 seconds.

final_state = history[-1] #get the final state of the system after the simulation has run.

print(f"Final state: t={final_state.t:.2f} s, x={final_state.x:.2f} m, v={final_state.v:.2f} m/s") #print the final state of the system after the simulation has run.
total_steps = len(history) #get the total number of steps taken in the simulation.
print(f"Total steps: {total_steps}") #print the total number of steps taken in the simulation.