import requests
from twilio.rest import Client
from keys import weather_api_key, weather_api_endpoint, account_sid, auth_token, FROM_NO, TO_NO
# TODO host somewhere

lat, lon = 8.279409, 77.182506

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": weather_api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(weather_api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12] # first 12 hrs
will_rain = False

for hour_data in weather_slice:
    weather_code = hour_data['weather'][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today. 🏄‍♂️",
        from_=FROM_NO,
        to=TO_NO
    )
    print(message.status)



