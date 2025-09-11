alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200


def network_alert_failure_stub(celcius):
    """Stub that simulates network failures"""
    print(f'ALERT: Temperature is {celcius} celcius')
    # This stub always returns failure to test the counting logic
    return 500

def alert_in_celcius(farenheit, network_stub=network_alert_stub):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
