# Exploratory Data Analysis of US Flight Data

![the_terminal_poster](/img/the_terminal_poster.jpg)

# Table of Contents
1. [Overview](#overview)
2. [Questions](#questions)
3. [Data](#data) 
4. [Visualization](#visualization)
5. [Conclusion](#conclusion)
6. [Credits](#credits)

## **Overview**
Airplane has become a commoditized mode of transportation over the years in the U.S.. Millions of travelers travel across the country and around the globe for both business and leisure.

If you have been one of these travelers, chances are you have been blessed by either a delay or cancellation at least a few times in your life. Being stuck at an airport terminal is a terrible feeling. The seats at the gate are uncomfortable. The wifi can get spotty. A burger causes $15 plus tax, tips, and some tacked on health tax.

In this project, let us pretend to be Tom, stuck at a San Francisco International Airport (SFO) terminal with no end in sight. We have all the time in the world and the power of free wifi. Let's take a look at some flight data!

## **Questions**
1. Which airport should Tom avoid next time, and why is it SFO?

2. Which airline is the worst, and why is it United?

## **Data**

Main Dataset
- Flight data: obtained from the "Airline On-Time Performance Data" database hosted by the Bureau of Transportation Statistics (BTS). The database tracks every non-stop U.S. domestic flights by month and year, by carrier and by origin and destination airport. Includes scheduled and actual departure and arrival times, canceled and diverted flights. I queried the trailing 12 months between February 2019 to January 2020. In aggregate, the dataset contains 7,445,398 flight entries between 354 U.S. airports

Minor Datasets
- Climate data: obtained from the National Oceanic and Atmopheric Administration (NOAA). Daily climate data collected by weather station, data point such as wind speed, temperature, condition flags for snow, fog, and thunder. I queried the trailing 12 months data from stations located near a selected number of California airports between February 2019 to January 2020.

- Runway data: obtained from the Federal Aviation Adminstration (FAA). Dataset contains technical specs of all U.S. airfield runways, not limited to international airports. I queried the latest runway specs available of a selected number of California airports.

## **Visualization**
To get a sense of the airports, I started with looking at traffic volume. Here are the most trafficked airports (in terms of domestic flights). SFO barely missed out on top 10 (it ranked 11).
![popular_us_airport](/img/most_popular_airport_US.png)

It is the second most trafficked in California, after LAX
![popular_ca_airport](/img/most_popular_airport_CA.png)

### Cancellation

One metric I would use to determine if SFO is indeed the WAAT (Worst Airport of All Time) is flight cancellation. Here are the airports that cancelled the largest portion of their flights. I was glad that SFO did not make the top 10, but I was surprised to see a California Airport at the very top 
![cancel_rate_us](/img/highest_cancellation_rate_US.png)

Within the state, SFO ranked 8 in cancellation rate (less than 2.5%)
![cancel_rate_ca](/img/highest_cancellation_rate_CA.png)

I was wondering if cancellation rate tends to be higher with the busier airport. Turns out, there is very weak correlation. In fact, the worst cancellation rates occured with the smallest airports in the country
![flight_count_cancel_rate_us](/img/flight_count_cancel_rate_US.png)

Does it matter if the airport is located in a remote part of country, say at the Alaskan Yukon or Hawaii? I plotted the average flight distance by airport against their cancellation rate, and there is very weak correlation as well.
![flight_dist_cancel_rate_us](/img/flight_dist_cancel_rate_US.png)


### Delay

The second key metric I looked at is delay in minutes. The Department of Transportation on-time statistics calculated it as the 'actual flight departure time' subtracted by 'scheduled flight departure time'.

Here are the US airports with the highest average delay time. I am once again relieved that it did not make the top 10. Notice our good friend Mammoth Lakes made top 10 again
![avg_delay_US](/img/highest_avg_delay_US.png)

Focusing on California. Although SFO ranked 6th, the preceeding airports are all much smaller regional airports.
![avg_delay_ca](/img/highest_avg_delay_CA.png)

In order to filter out the small airports, I decided to take a closer look at the busiest airports in the country and see how SFO compares. Despite having the 11th most domestic flight, it ranked 5th in average delay.
![avg_delay_high_traffic_us](/img/avg_delay_high_traffic_US.png)

Looking at the distribution of all the flight delay across these 11 airports, I was suprised to find that over half of the flights were actually on time (and early!). Notice the middle black lines (indicating the median point) were all towards the left of 0.
![delay_dist_zoomed_US](/img/delay_dist_zoomed_US.png)

The previous graph was purposely zoomed into the middle. Take a look at the full distribution here.
![delay_dist_full_US](/img/delay_dist_full_US.png)
There were some extreme delays.

### Hypothesis Testing #1
I ran several two-samples, one-tailed t-test to test the null hypothesis that San Francisco Airport delay were no different comparing to:

1. National Average
2. Los Angeles Airport
3. Oakland Airport
4. San Jose Airport

Using an alpha of 0.05 (95% confidence), the t-tests rejected all the null hypotheses with p-val < 0.05

### Weather
San Francisco has been an infamous reputation for being foggy. I was wondering if weather condition had an effect on the flight.

I identified the NOAA weather stations located at/near the airports of San Francisco, Los Angeles, Oakland, and San Jose, and queried the daily climate data between the same timeframe as the flight data (Feb '19 - Jan '20)

Plotting four binary weather condition flags (Fog, Heavy Fog, Thunder, Smoke/Haze) against cancellation rate. No obvious pattern observed
![cancel_weather_sfo](/img/cancel_weather_SFO.png)

Plotting the same weather flags against average delay, it seems to have longer delay on foggy and smokey days
![delay_weather_sfo](/img/delay_weather_SFO.png)

The daily climate data also included average temperature, average windspeed and precipitation. Fairly weak correlations with cancellation rates
![cancel_weather_sfo_2](/img/cancel_weather_SFO_2.png)

Same applied to average delay time
![delay_weather_sfo_2](/img/delay_weather_SFO_2.png)

### Hypothesis Testing #2
The visualization between statistical

## **Conclusion**

## **Credits**
- The Terminal movie poster from Google Image Search
- Domestic Flight Data provided by the United States Department of Transportation, Bureau of Transportation Statistics (BTS). See more [by clicking here.](https://www.transtats.bts.gov/tables.asp?Table_ID=236&SYS_Table_Name=T_ONTIME_REPORTING)
- Climate Data provided by the United States National Centers For Environmental Information, National Oceanic and Atmopheric Administration (NOAA). See more [by clicking here.](https://www.ncdc.noaa.gov/cdo-web/)
- Airport Runway Data provided by the United States Department of Transportation, Federal Aviation Adminstration (FAA). See more [by clicking here.](https://www.faa.gov/airports/airport_safety/airportdata_5010/)
