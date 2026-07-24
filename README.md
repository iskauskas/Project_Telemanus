# Space Mission Simulator — Project Telemanus

I'm building my own rocket launch and orbital mechanics simulator from scratch in Python, as a portfolio project for my Aerospace Engineering university applications. The goal is to model a full mission — from vertical launch through to a stable orbit — deriving every equation from first principles rather than relying on black-box physics libraries.

This project uses A-level maths and physics as a starting point, then pushes into concepts beyond my current syllabus: numerical integration methods, orbital mechanics, and rocket propulsion theory.

## Project Journal & Roadmap

The full architecture, 3-month roadmap, and a running journal of my decisions, experiments, and results (including things that didn't work first time) are documented here:

**[docs/00_architecture_and_roadmap.md](docs/00_architecture_and_roadmap.md)**

I'd genuinely recommend reading that over this README if you want to see the actual thinking behind the project, not just the end result.

##  Highlights so far

- Built a simulation engine from scratch: a time-stepping loop that advances a physical system through discrete time steps, recording its full history.
- Implemented **Euler integration** to simulate a point mass in free-fall under gravity, then **verified it numerically** against the exact analytical (SUVAT) solution.
- Confirmed experimentally that Euler's error shrinks as the time step (`dt`) decreases — e.g. landing velocity converged from -45.11 m/s (dt=0.1) to -44.30 m/s (dt=0.001), against an exact answer of -44.3 m/s.
- Diagnosed and explained *why* the simulation overshoots the ground slightly on landing, as a direct consequence of discrete time-stepping — not a bug, but a genuine numerical modelling limitation.

*(This list will grow as the project progresses — see the roadmap for what's next.)*

## Status

 In development — Phase 0 (project setup) complete. Phase 1 (vertical launch physics) in progress: free-fall under gravity working and verified; drag and thrust modelling next.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .
```

## Project structure

See [docs/00_architecture_and_roadmap.md](docs/00_architecture_and_roadmap.md) for the full design rationale and roadmap. In brief:

```
src/smsim/       # the simulator package itself, organised by physics domain
tests/           # pytest tests, mirroring src/smsim structure
docs/            # architecture notes, physics derivations, decision log
```