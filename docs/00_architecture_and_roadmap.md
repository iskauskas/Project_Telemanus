# Project Telemanus — Architecture & Roadmap

William Iskauskas

July 2026

Timeline has been fixed to around **3 months, with average 10-15 hrs/week** when planning what Concepts I wanted to include I came to the conclusion of using a braod range of concepts in moderate detail instead of few concpets with higher detail so that when investigating them I may discover which I like the ideas of and have more of an intrest in as this project is also for me to explore more physics that I cannot in my current A level classes. (get from launch to orbital mechanics). Section 5 below reflects the compressed plan. Phases 4-6 are moved to an explicit **Future Work** backlog rather than dropped, this is due to time restraints and so that I can always come back to this project.
---

## 1. Engineering Philosophy

My rules;

1. **Every idea in the code must be traceable to an equation I understand and can derive.**
2. **Build it simply and correct first, then improve it** 
3. **Git history is a lab notebook, log almost everything I do.**

## 2. Repository Architecture

Project Telemanus/
│
├── README.md                 # Project overview/current status
├── requirements.txt           # dependencies
├── .gitignore
│
├── src/
│   └── smsim/                 # This is the Space Mission SIMulation package which the code can refer to when needed
│       ├── __init__.py
│       │
│       ├── physics/           
│       │   ├── constants.py       # G, g0, R_earth, atmosphere constants and many more
│       │   ├── kinematics.py      # displacement/velocity/acceleration relationships
│       │   └── integrators.py     # Euler, RK4 — generic ODE steppers - as of now I am not too sure about these but am aware they are needed and that RK4 may be better
│       │
│       ├── rocket/            # everything about the vehicle itself
│       │   ├── rocket.py          # mass, thrust, fuel state
│       │   └── stage.py           # (Phase 6) multi-stage support for when i get to it one day
│       │
│       ├── atmosphere/        # air density, drag
│       │   └── earth_atmosphere.py
│       │
│       ├── gravity/            # gravity models 
│       │   └── gravity.py
│       │
│       ├── orbit/             # Phase 3+: orbital elements, conics - again not sure as of now truly what conics are but i am aware they are needed
│       │   └── orbital_mechanics.py
│       │
│       ├── planets/           # Phase 4: planet data (mass, radius, atmosphere)
│       │   └── planet.py
│       │
│       ├── simulation/        applies the physics context to the rocket code
│       │   ├── simulator.py       # time-stepping loop, state history recording
│       │   └── state.py           # SimulationState dataclass
│       │
│       ├── guidance/          # Phase 2+: pitch yaw roll, gravity turn, autopilot
│       │   └── guidance.py
│       │
│       ├── visualisation/     # plotting / pygame rendering — presentation layer only
│       │   ├── plots.py           # matplotlib altitude/velocity/accel graphs
│       │   └── render_2d.py       # (Phase 2+) pygame trajectory view
│       │
│       └── utils/             # logging, unit conversions
│           └── units.py
│
├── tests/                     # pytest — mirrors src/smsim structure exactly
│   ├── physics/
│   ├── rocket/
│   └── ...
│
├── docs/                      # this is where i will derive equations; understand and utilise them
│   │                         
│   ├── 00_architecture_and_roadmap.md   (this file)
│   ├── physics_notes/
│   │   ├── newtons_second_law.md
│   │   ├── rocket_equation_derivation.md
│   │   └── ...
│   └── decisions/              
│       
│
└── assets/                    # rocket sprites, planet textures, icons (Phase 2+)
```

### 2.1 — One deliberate change from your proposed layout

Because of my current understanding (not full) of gravity fields and inverse square law etc, i have decided to seperate gravity from the others as i feel it will be a larger concept in itself both during the atmospheric escape and orbit.


### 2.2 — Why this structure, generally

- I wanted to make the physics section completely seperate to the rocket section, mostly for its use in other scenarios that dont involve rockets, if I wanted to test other things in the future.
- Create a testing space so that i can go back and look at prior test aswell as being able to create tests, leading to me having access to more previous data.

---



---

## . Development Roadmap — 3-Month Compressed Plan

**Constraints:** 12 weeks (likely less), ~10-15 hrs/week (~130-180 hrs total), breadth-priority (reach orbital mechanics; accept lighter rigor early on rather than deep polish at every step).


### ** — Phase 0: Bootstrap + first physics**
- Repo skeleton, git init, `.gitignore`, `requirements.txt`, virtual environment, package structure, empty modules.
- First working code: single point mass in free-fall under constant gravity, Euler integration, no rocket yet. This establishes the simulation-loop pattern (time step → state update → history recording) every later phase reuses.
- *Commits:* `chore: initial project skeleton`, `feat(physics): free-fall simulation with Euler integration`.

### ** Phase 1 — Drag, then the Rocket class**
- Add atmospheric drag to the free-fall model; briefly note where Euler starts to show error (no need for a full numerical-methods essay yet — that comes in Week 4).
- Introduce `Rocket` class: constant thrust, fixed mass. No fuel depletion yet.

### * — The rocket equation**
- Derive and implement Tsiolkovsky's rocket equation: changing mass from fuel consumption.
- Combine thrust + gravity + drag + changing mass into one full vertical-ascent simulation.
- *This is Phase 1's centrepiece — budget the most time here.*

###  RK4 and Phase 1 wrap-up**
- Implement RK4, quantitatively compare it against Euler on the ascent simulation (a strong, cheap-to-produce portfolio plot).
- Altitude/velocity/acceleration graphs, matplotlib polish.
- Unit tests for the integrators and the rocket equation specifically (not exhaustive coverage — these are the two places a silent bug would be worst).
- Docs notes: Newton's 2nd law, drag equation, rocket equation derivations.
- *Deliverable: complete, tested, documented single-stage vertical launch simulator.*

###  Phase 2: 2D flight & gravity turn**
- Extend state to 2D (downrange distance + altitude, or x/y).
- Re-derive equations of motion in vector form.
- Implement a simple pitch-over / gravity-turn guidance program — this is what gets the rocket from "straight up" to "sideways enough to eventually orbit."
- 2D trajectory plot.
- Keep this phase lean: one guidance strategy, not several alternatives compared.




---

## 6. Future Work (explicit backlog, not silently dropped)

Cut from the 3-month scope by design, not oversight — worth stating this plainly to an interviewer:

- **Multi-stage rockets** — would require extending `Rocket` to `Stage`-composed vehicles and handling stage-separation events in the simulation loop.
- **Multiple planets/moons** (Mars, Moon, differing g and atmosphere) — the `planets/` and `gravity/` module split in §2.1 was specifically designed so this could be added later without restructuring existing code.
- **Mission planner / delta-v budgeting** — natural extension once the rocket equation and orbital mechanics modules both exist.
- **Hohmann transfers, simple autopilot, 3D visualisation** — meaningful next steps if the project continues beyond the application cycle.

---
### 3. Notebook and Process

That was the initial roadmap, anything note worthy and new will be addedd from here on out;


So my inital plan is too simply make an enviroment where I will drop a ball, for now only gravity will act on it. Initially I thought that I could use constant 9.81 gravity but then remembered that drag, fuel burns and altitude all have effects on it, so we have to go back to base principles. we can use 9.81 to make sure that the equation is correct however. Eulers intergration is able to solve differential equations numerically by seperating it into many steps, letting you estimate where you will be a tiny biy ahead. So to make this work we will clearly need a class which can contain time, displacement and velocity. we will also need to be able to create the next small step after each calculation so a step function is needed. then simply loop this.
Ok after testing a free fall under eulers integration to find gravity at a dt of 0.1 i ended up with -45.11 as the final velocity even though it should be -44.3 when using SUVAT equations. So i want to reduce this error gap, maybe by reducing the dt. with a dt of 0.01 i got an answer of -44.42 which is a lot closer, now I will try with a dt of 0.001 and see what I get. With this new dt I got the answer exactly correct, which makes sense as the smaller the dt the closer the tangents will be to the actual curve. there is a slight over shoot with the displacement due to it not being a perfect curve that I am making, but the lower the dt the closer it gets to this curve and the less overshoot occurs.

Overhalled the README section so that it briefly talks about what I have done in this project so far and some goals I have hit, also linked this document to it for more in depth review.

Next job is to go into drag and thrust modelling now I have a basic simulator set up.

Before I move on I forgot I made a tests folder, I will test the integration works properly, this can be used for any value and makes the validity of results a lot easier to get, instead of just knowing it works for one result.

Ok now I am going to use Matplotlib to plot the graph of the motion using the history feature I added to plot a poit every delta t.
