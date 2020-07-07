import streamlit as st
import requests
import json

def main():

    # Title
    st.title("☀️ ⚡️ WEATHER APP ❄️ ☔️")
    st.title("🌈 Try out with different locations in the world !! 🔅")
    st.title("Enter the name of the city : ")
    city = st.text_input("")
    st.title("Weather Report of {}".format(city))

    # Api call
    url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
    "q" : {city},
    "appid" : {"ca**************************91"},
    "units" : {"metric"}
    }

    # conditions
    st.sidebar.title(" ☂️ Select the parameters you wanna know 🌄")

    conditions = st.sidebar.multiselect(" 🌟 Choose from various options : 🪐 ", ["Temperature","Wind","Other","Clouds"])


    if st.sidebar.button("Go", key='weather report'):
        r = requests.get(url, params=params)

        # Checking the conditions
        check = str(r)
        if check == '<Response [404]>':
            st.title("City not found !")

        else:
            weather = json.loads(r.content.decode('utf-8'))

            if "Temperature" in conditions:
                st.markdown("Temperature : {}°C".format(weather['main']['temp']))
                st.markdown("Min Temperature : {}°C".format(weather['main']['temp_min']))
                st.markdown("Max Temperature : {}°C".format(weather['main']['temp_max']))

            if "Wind" in conditions:
                st.markdown("Wind Speed (m/s) : {}".format(weather['wind']['speed']))
                st.markdown("Wind Direction (in degrees) : {}°".format(weather['wind']['deg']))

            if "Clouds" in conditions:
                st.markdown("Cloudiness (in %) : {}".format(weather['clouds']['all']))

            if "Other" in conditions:
                st.markdown("Humidity (in %): {}".format(weather['main']['humidity']))
                st.markdown("Pressure (in hPA): {}".format(weather['main']['pressure']))


if __name__ == '__main__':
    main()
