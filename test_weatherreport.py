import pytest
from weatherreport import report


def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def highPrecipitationStub():
    """Stub that provides high precipitation and low wind speed to expose bug."""
    return {
        'temperatureInC': 30,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 40  # Low wind speed
    }


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(highPrecipitationStub)

    # strengthen the assert to expose the bug
    # With high precipitation (70) and low wind (40), it should predict rain
    # But the function incorrectly returns "Sunny Day" due to a logic bug
    expected_msg = f"Expected rain prediction, but got: '{weather}'"
    assert "rain" in weather.lower(), expected_msg


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
