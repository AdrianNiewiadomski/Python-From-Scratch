import requests


def get_current_weather():
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=your_city,your_country&APPID=your_appid')
    if response.ok:
        return response.json()


if __name__ == '__main__':
    get_current_weather()
