import pytest
from alerter import alert_in_celcius, alert_failure_count


def network_alert_failure_stub(celcius):
    """Stub that simulates network failures"""
    print(f'ALERT: Temperature is {celcius} celcius')
    # This stub always returns failure to test the counting logic
    return 500


def test_alert_failure_count():
    """Test that failures are properly counted."""
    global alert_failure_count
    
    # Reset the counter by importing and setting it
    import alerter
    alerter.alert_failure_count = 0
    
    # Call alert with failure stub multiple times
    alert_in_celcius(400.5, network_alert_failure_stub)
    alert_in_celcius(500.0, network_alert_failure_stub)
    alert_in_celcius(600.0, network_alert_failure_stub)
    
    # The bug: alert_failure_count += 0 means failures are not counted
    # This test will fail because count will be 0 instead of 3
    expected_failures = 3
    actual_failures = alerter.alert_failure_count
    error_msg = f"Expected {expected_failures} failures, but got {actual_failures}"
    assert actual_failures == expected_failures, error_msg


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
