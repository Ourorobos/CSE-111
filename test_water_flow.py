import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

PIPE_ONE = 0.048692
PIPE_TWO = 0.286870

def test_water_column_height():
    assert water_column_height(0,0) == pytest.approx(0, abs = 0.001)
    assert water_column_height(0,10) == pytest.approx(7.5, abs = 0.001)
    assert water_column_height(25,0) == pytest.approx(25, abs = 0.001)
    assert water_column_height(48.3,12.8) == pytest.approx(57.9, abs = 0.001)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == pytest.approx(0, abs = 0.001)
    assert pressure_gain_from_water_height(30.2) == pytest.approx(295.628, abs = 0.001)
    assert pressure_gain_from_water_height(50) == pytest.approx(489.450, abs = 0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(PIPE_ONE, 0, 0.018, 1.75) == pytest.approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(PIPE_ONE, 200, 0, 1.75) == pytest.approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(PIPE_ONE, 200, 0.018, 0) == pytest.approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(PIPE_ONE, 200, 0.018, 1.75) == pytest.approx(-113.008, abs = 0.001)
    assert pressure_loss_from_pipe(PIPE_ONE, 200, 0.018, 1.65) == pytest.approx(-100.462, abs = 0.001)
    assert pressure_loss_from_pipe(PIPE_TWO, 1000, 0.013, 1.65) == pytest.approx(-61.576, abs = 0.001)
    assert pressure_loss_from_pipe(PIPE_TWO, 1800.75, 0.013, 1.65) == pytest.approx(-110.884, abs = 0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 3) == pytest.approx(0, abs = 0.001)
    assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0, abs = 0.001)
    assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, abs = 0.001)
    assert pressure_loss_from_fittings(1.75, 2) == pytest.approx(-0.122, abs = 0.001)
    assert pressure_loss_from_fittings(1.75, 5) == pytest.approx(-0.306, abs = 0.001)

def test_reynolds_number():
    assert reynolds_number(PIPE_ONE, 0) == pytest.approx(0, abs = 1)
    assert reynolds_number(PIPE_ONE, 1.65) == pytest.approx(80069, abs = 1)
    assert reynolds_number(PIPE_ONE, 1.75) == pytest.approx(84922, abs = 1)
    assert reynolds_number(PIPE_TWO, 1.65) == pytest.approx(471729, abs = 1)
    assert reynolds_number(PIPE_TWO, 1.75) == pytest.approx(500318, abs = 1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(PIPE_TWO, 0, 1, PIPE_ONE) == pytest.approx(0, abs = 0.001)
    assert pressure_loss_from_pipe_reduction(PIPE_TWO, 1.65, 471729, PIPE_ONE) == pytest.approx(-163.744, abs = 0.001)
    assert pressure_loss_from_pipe_reduction(PIPE_TWO, 1.75, 500318, PIPE_ONE) == pytest.approx(-184.182, abs = 0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])