import pytest

from ..controllers.utils import compute_hour_difference
@pytest.mark.parametrize("date1_str, date2_str, expected_hour_difference", [
    ("2024-04-16T12:00:00", "2024-04-17T12:00:00", 24.0),
    ("2024-04-17T12:00:00", "2024-04-16T12:00:00", 24.0),
])

def test_compute_hour_difference(date1_str, date2_str, expected_hour_difference):
    actual_hour_difference = compute_hour_difference(date1_str, date2_str)
    assert actual_hour_difference == expected_hour_difference

