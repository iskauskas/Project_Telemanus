'''test for aerdynamic drag module'''

import pytest
from smsim.physics.drag import drag_acceleration
from smsim.simulation.state import State
from smsim.simulation.simulator import run_simulation
from smsim.physics.integrators import euler_step
from smsim.physics.constants import g0, rho0

def test_drag_is_zero_when_stationary():
    a = drag_acceleration(v=0.0, mass=7.0, drag_coefficient=0.47, area=0.038, air_density=rho0)
    assert a == pytest.approx(0.0)


def test_drag_opposes_downward_motion():
    """A falling object (negative velocity, by our 'up is positive'
    convention) should experience drag acting upward (positive)."""
    a = drag_acceleration(v=-20.0, mass=7.0, drag_coefficient=0.47, area=0.038, air_density=rho0)
    assert a > 0


def test_drag_scales_with_velocity_squared():
    """Doubling velocity should roughly quadruple the drag magnitude,
    since drag force is proportional to v^2."""
    a_slow = drag_acceleration(v=-10.0, mass=7.0, drag_coefficient=0.47, area=0.038, air_density=rho0)
    a_fast = drag_acceleration(v=-20.0, mass=7.0, drag_coefficient=0.47, area=0.038, air_density=rho0)

    ratio = a_fast / a_slow
    assert ratio == pytest.approx(4.0, rel=0.01)


def test_drag_makes_falling_object_land_slower_than_no_drag():
    """A falling object with drag must land at a lower speed than the
    same object falling with gravity alone, since drag always opposes
    motion and therefore can only reduce speed, never increase it."""

    mass = 7.0
    drag_coefficient = 0.47
    area = 0.038

    def no_drag_acceleration(state: State) -> float:
        return -g0

    def with_drag_acceleration(state: State) -> float:
        return -g0 + drag_acceleration(state.v, mass, drag_coefficient, area, rho0)

    initial = State(t=0.0, x=100.0, v=0.0)

    history_no_drag = run_simulation(
        initial_state=initial,
        dt=0.01,
        step_function=lambda s, dt: euler_step(s, dt, no_drag_acceleration),
    )
    history_with_drag = run_simulation(
        initial_state=initial,
        dt=0.01,
        step_function=lambda s, dt: euler_step(s, dt, with_drag_acceleration),
    )

    landing_speed_no_drag = abs(history_no_drag[-1].v)
    landing_speed_with_drag = abs(history_with_drag[-1].v)

    assert landing_speed_with_drag < landing_speed_no_drag