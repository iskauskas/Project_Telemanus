#defines the state of the simulation at a given time step. This includes the current time, the state of the system, and any other relevant information needed to describe the simulation at that point in time.
from dataclasses import dataclass
@dataclass
class State:
    t:float #time since start of simulation
    x:float #vertical displacement of the system
    v:float #vertical velocity of the system