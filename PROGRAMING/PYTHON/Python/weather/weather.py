# Weather Forcast APP, API: https://www.youtube.com/watch?v=Oz3W-LKfafE
import requests

def make_request():
    API_KEY = '5aafe39944d5682b9668ef0bfe1f38d5'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    city = input('Enter city name: ')
    print()
    parameters = {'appid':API_KEY, 'q':city, 'units':'metric'}
    reques_url = f'{base_url}?appid={API_KEY}&q={city}'

    r = requests.get(base_url, parameters)
    if r.status_code == 200:
        data = r.json()
        return data

    return 'An error occured'

def handle_date_nice_output(data):
    city_country = f"|{data['name']}, {data['sys']['country']}|\n{'-'*12}"
    temperature = f"Temperature: {round(data['main']['temp'])} C"
    wind = data['wind']['speed']
    weather = f"{data['weather'][0]['main']}, {data['weather'][0]['description']}, w{wind}m/s."
    for item in city_country, temperature, weather: print(item)

def main():
    keep_ask = True
    while keep_ask:
        handle_date_nice_output(make_request())
        keep_ask = True if input(f'\nContinue Y/N?: ').lower() == 'y' else False

if __name__ == '__main__':
    main()
