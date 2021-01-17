import integration_definitions
import call_rest_api


# parameterize
def test_get_solar_times():
    """
    Test /status
    :return:
    """
    query = {}
    query['app_name'] = 'integration_tests'
    query['lat'] = 51.414
    query['lon'] = -1.375

    status_code, response_dict = call_rest_api.call_rest_api(integration_definitions.metminimisc_service_endpoint_base + '/get_solar_times', query)

    assert status_code == 200
    assert 'AM' not in response_dict['sunrise']
    assert 'PM' not in response_dict['sunset']
