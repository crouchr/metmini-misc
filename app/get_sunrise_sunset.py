# https://sunrise-sunset.org/api
import requests
import json


def get_solar_info_api1(lat, lon):
    """

    :param lat:
    :param lon:
    :return:
    >>> get_solar_info_api1(51.4146, -1.3749)

    """
    url = "https://api.sunrise-sunset.org/json?" +\
        "lat=" + lat.__str__() + \
        "&lng=" + lon.__str__() + \
        "&date=today"

    response = requests.get(url)

    if response.status_code != 200:
        return response.status_code, None

    response_dict = json.loads(response.content.decode('utf-8'))

    return response.status_code, response_dict['results']


# testing
if __name__ == '__main__':

    my_lat = 51.4146
    my_lon = -1.3749

    print('lat = ' + my_lat.__str__())
    print('lon = ' + my_lon.__str__())

    status_code, response = get_solar_info_api1(my_lat, my_lon)

    if status_code != 200:
        print('status_code=' + status_code.__str__())

    print('civil_twilight_begin = ' + response['civil_twilight_begin'])
    print('sunrise = ' + response['sunrise'])
    print('solar_noon = ' + response['solar_noon'])
    print('sunset = ' + response['sunset'])
    print('civil_twilight_end = ' + response['civil_twilight_end'])
    print('day_length = ' + response['day_length'])

    print('finished')



