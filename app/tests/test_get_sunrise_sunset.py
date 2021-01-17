import get_sunrise_sunset


def test_convert_to_24_hour():
    result_1 = get_sunrise_sunset.convert_to_24_hour('7:23:23 PM')
    result_2 = get_sunrise_sunset.convert_to_24_hour('7:23:23 AM')
    result_3 = get_sunrise_sunset.convert_to_24_hour('12:23:23 PM')

    assert result_1 == '19:23:23'
    assert result_2 == '07:23:23'
    assert result_3 == '12:23:23'


def test_get_solar_times_api_1():
    lat = 51.4146
    lon = -1.3749

    status_code, results = get_sunrise_sunset.get_solar_info_api1(lat=lat, lon=lon)

    assert status_code == 200
    assert 'PM' not in results['sunset']
    assert 'AM' not in results['sunrise']