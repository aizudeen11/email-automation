import pandas as pd
import requests as r
import datetime as dt

def get_random_quote():
    df = pd.read_csv('Quotes.csv')
    lists = ['quotes', 'authors', 'URL']
    quotes_only = df.loc[:,lists]
    random_df = quotes_only.sample()   
    dicts = random_df.to_dict('list')
    return dicts

def get_weather_forecast():                        
    api_key = 'enter your API key here'
    location = 'sungai besar' 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    data = r.get(url).json()
    kelvin = data['main']['temp']
    celcius = kelvin - 273.15
    weather_discription = data['weather'][0]['description']
    # [0] for list of dict
    country_code = data['sys']['country']
    location_name = data['name']
    sun_rise = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sun_set = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    weather_data = {
        'celcius' : celcius,
        'weather_discription' : weather_discription,
        'country_code' : country_code,
        'location_name' : location_name, 
        'sun_rise' : sun_rise,
        'sun_set' : sun_set
    }
    return weather_data

content1 = get_random_quote()
content2 = get_weather_forecast()
content =  f""" 
<!DOCTYPE html>
<html>
    <body>
    <body>
        <div style="background-color:#eee;padding:10px 20px; text-align:center;">
            <h2 style="font-size: 32px;
            font-family: Georgia, 'Times New Roman', Times, serif;
            color: #454349;">Python Email Automation</h2>
        </div>
        <div style="padding:20px 0px">
            <div>
                <div style="text-align:center;">
                    <h3 style="font-size: 27px;">Inspirational Quotes</h3>
                    <p style="font-size: 20px;">{content1['quotes'][0]} by {content1['authors'][0]}</p>
                    <a href="{content1['URL'][0]}" style="margin: 12px">Read more</a>
                    <hr>
                    <h3 style="font-size: 27px;">Weather Today</h3>
                    <p style="font-size: 20px;">Weather location: {content2["country_code"]}, {content2["location_name"]}</p>
                    <p style="font-size: 20px;">Weather condition is {content2["weather_discription"]} with temperature {content2["celcius"]:.2f}°C</p>
                    <p style="font-size: 20px;">Sunrise time: {content2["sun_rise"]}</p>
                    <p style="font-size: 20px;">Sunset time: {content2["sun_set"]}</p>
                    <hr>               
                </div>
            </div>
            <div style="font-size: 20px;
            margin: 12px 12px">
                Contact Number: 012-345 6789 | <a href="#">Whatsapp</a>
                <br>
                Email Address: <a href="mailto:email@gmail.com">email@gmail.com</a>
            </div>
        </div>
    </body>
</html>
 """
