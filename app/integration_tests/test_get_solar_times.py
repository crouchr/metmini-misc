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
    query['lat'] = -1.375
    query['lon'] = 51.414
    #query['lon'] = -1.375

    status_code, response_dict = call_rest_api.call_rest_api(integration_definitions.endpoint_base + '/get_solar_times', query)

    assert status_code == 200


