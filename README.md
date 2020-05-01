# Exploratory Data Analysis of US Flight Data

![the_terminal_poster](/img/the_terminal_poster.jpg)

#### ![Click here](https://github.com/tchleung/The_Terminal/blob/master/The%20Terminal%20-%203%20Minutes%20Presentation.pdf) for a 3-minute summary presentation 

# Table of Contents
<!--ts-->
1. [Overview](#overview)
2. [Questions](#questions)
3. [Data](#data) 
4. [Analysis](#analysis)
    * [Cancellation](#cancellation)
    * [Delay](#delay)
    * [Hypothesis Testing 1](#hypothesis-testing-1)
    * [Weather](#weather)
    * [Hypothesis Testing 2](#hypothesis-testing-2)
    * [Runway](#runway)
    * [Airline](#airline)
5. [Conclusion](#conclusion)
6. [Credits](#credits)
<!--te-->

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

## **Analysis**
To get a sense of the airports, I started with looking at traffic volume. Here are the most trafficked airports (in terms of domestic flights). SFO barely missed out on top 10 (it ranked 11).<br/><br/>
![popular_us_airport](/img/most_popular_airport_US.png)

It is the second most trafficked in California, after LAX<br/><br/>
![popular_ca_airport](/img/most_popular_airport_CA.png)

### Cancellation

One metric I would use to determine if SFO is indeed the WAAT (Worst Airport of All Time) is flight cancellation. Here are the airports that cancelled the largest portion of their flights. I was glad that SFO did not make the top 10, but I was surprised to see a California Airport at the very top<br/><br/>
![cancel_rate_us](/img/highest_cancellation_rate_US.png)

Within the state, SFO ranked 8 in cancellation rate (less than 2.5%)<br/><br/>
![cancel_rate_ca](/img/highest_cancellation_rate_CA.png)

I was wondering if cancellation rate tends to be higher with the busier airport. Turns out, there is very weak correlation. In fact, the worst cancellation rates occured with the smallest airports in the country<br/><br/>
![flight_count_cancel_rate_us](/img/flight_count_cancel_rate_US.png)

Does it matter if the airport is located in a remote part of country, say at the Alaskan Yukon or Hawaii? I plotted the average flight distance by airport against their cancellation rate, and there is very weak correlation as well.<br/><br/>
![flight_dist_cancel_rate_us](/img/flight_dist_cancel_rate_US.png)


### Delay

The second key metric I looked at is delay in minutes. The Department of Transportation on-time statistics calculated it as the 'actual flight departure time' subtracted by 'scheduled flight departure time'.

Here are the US airports with the highest average delay time. I am once again relieved that it did not make the top 10. Notice our good friend Mammoth Lakes made top 10 again<br/><br/>
![avg_delay_US](/img/highest_avg_delay_US.png)

Focusing on California. Although SFO ranked 6th, the preceeding airports are all much smaller regional airports.<br/><br/>
![avg_delay_ca](/img/highest_avg_delay_CA.png)

In order to filter out the small airports, I decided to take a closer look at the busiest airports in the country and see how SFO compares. Despite having the 11th most domestic flight, it ranked 5th in average delay.<br/><br/>
![avg_delay_high_traffic_us](/img/avg_delay_high_traffic_US.png)

Looking at the distribution of all the flight delay across these 11 airports, I was suprised to find that over half of the flights were actually on time (and early!). Notice the middle black lines (indicating the median point) were all towards the left of 0.<br/><br/>
![delay_dist_zoomed_US](/img/delay_dist_zoomed_US.png)

The previous graph was purposely zoomed into the middle. Take a look at the full distribution here.<br/><br/>
![delay_dist_full_US](/img/delay_dist_full_US.png)
There were some extreme delays.

### Hypothesis Testing 1
I ran several two-samples, one-tailed t-test to test the null hypothesis that San Francisco Airport delay were no different comparing to:

1. National Average
2. Los Angeles Airport
3. Oakland Airport
4. San Jose Airport

Using an alpha of 0.05 (95% confidence), the t-tests rejected all the null hypotheses with p-val < 0.05

### Weather
San Francisco has reputation for being foggy. Let's see if this conventional wisdom is right, and whether fog plays a factor on flights.

I identified the NOAA weather stations located at/near the airports of San Francisco, Los Angeles, Oakland, and San Jose, and queried the daily climate data between the same timeframe as the flight data (Feb '19 - Jan '20)

In the dataset, there were four binary weather condition flags (Fog, Heavy Fog, Thunder, Smoke/Haze). Plotting them against cancellation rate, and there is no obvious pattern <br/><br/>
![cancel_weather_sfo](/img/cancel_weather_SFO.png)

Plotting the same weather flags against average delay, there seems to be longer delay on foggy and smokey days<br/><br/>
![delay_weather_sfo](/img/delay_weather_SFO.png)

The daily climate data also included quantitative weather metrics such as average temperature, average windspeed and precipitation. I plotted them against the cancellation rates, and observed fairly weak correlation<br/><br/>
![cancel_weather_sfo_2](/img/cancel_weather_SFO_2.png)

Equally weak correlation when plotted against average delay time<br/><br/>
![delay_weather_sfo_2](/img/delay_weather_SFO_2.png)

Given that we are not observing much with the quantitative metrics, I decided to focus more on the binary conditions. Here is a comparison of the weather conditions at 5 major California airports <br/><br/>
![weather_ca](/img/weather_CA.png)
<br/><br/>
A few observations from the graphics above<br/><br/>

1- San Francisco and Oakland airports had similar number of days that were foggy<br/>
2- Los Angeles had the most days with heavy fog<br/>
3- San Francisco had the most days with either smoke or haze, likely a result of the historic wildfire in 2019<br/>
4- San Jose airport had the best weather out of the five

### Hypothesis Testing 2
First, I wanted to answer two questions:<br/>
1. At SFO, are delays longer when it is foggy compared to days that are not?<br/>
2. At SFO, are delays longer when it is smokey compared to days that are not?<br/>

I ran two two-samples, one-tailed t-test to test the null hypothesis that the delays are the same regardless of the conditions, using an alpha of 0.05 (95% confidence), the t-tests rejected both null hypotheses with p-val < 0.05

Second, I wanted to address whether SFO has longer delay on foggy days than:
1. Los Angeles Airport
2. Oakland Airport
3. San Jose Airport
4. San Diego Airport

I ran 4 two-samples, one-tailed t-test to test the null hypothesis that the delays on foggy days are the same between SFO and the other airports. Using an alpha of 0.05 (95% confidence), the t-tests rejected all null hypotheses with p-val < 0.05

### Runway
Before we head to the airline section, let's take a some runway statistics

There is a myth that we don't have enough runways. However, San Francisco Airport has a standard four runway design, same as Los Angeles and Oakland<br/><br/>
![runway_ca_1](/img/runway_ca_1.png)

Moreover, it does not handle nearly as many flights as Los Angles <br/><br/>
![runway_ca_2](/img/runway_ca_2.png)

So what's the deal? It is not something that is obvious when looking at the raw data, let's look at the configuration<br/><br/>
![sfo_runway_configuration](/img/sfo_runway_configuration.jpg)

When the weather is foggy, planes cannot land in San Francisco side-by-side on the parallel runways, effectively cutting the runway by half. It is not that we do not have as many runway, rather that bad weather conditions force us to fly with half the capacity

### Airline
Due to the amount needed for capital investment and regulatory hurdles that one needs to go through, the airline industry is largely an oligopoly. At the individual airport level, some airlines have close to a monopoly

For instance, SFO is dominated by United Airline. Even the second place airline (SkyWest) is a contractor that operates under the United Airline banner<br/><br/>
![airline_SFO_2](/img/airline_SFO_2.png)

Anedoctally, most people who lives in San Francisco would agree that United Airline is the worst airline due to the delay. But is it true statistically?

Let's take a look at the same cancellation rate and average delay metric<br/><br/>
![airline_SFO_3](/img/airline_SFO_2.png)

Southwest airline, which has a bigger presence at Oakland than San Francisco, had the highest cancellation rate of its domestic flight. Meanwhile, budget airline Frontier had the worst average delay despite having a miniscule footprint at San Francisco
 
Just how bad is Frontier? Let's run a few hypothesis tests to find out

### Hypothesis Testing 3

I ran several two-samples, one-tailed t-test to test the null hypothesis that Frontier's delay time was no different comparing to the following airlines:

1. SkyWest
2. American
3. JetBlue
4. United
5. Southwest
6. Alaska

Using an alpha of 0.05 (95% confidence), the t-tests rejected all the null hypotheses with p-val < 0.05

## **Conclusion**

We have looked at a lot of data trying to find evidence to prove two things

1. Which airport should we avoid
2. Which airline is the worst

SFO may not be *the* worst, but it is one of the worst major airports in terms of delay. A combination of runway design and weather condition are the culprit. I have once been told by a flight attendant at the gate that if I treasure my time, "honey, you should stop flying at SFO." Perhaps we should all take her advice, and consider the Oakland airpotr or San Jose airport if it is an option.

Contrary to popular (and my personal) belief, United Airline is not the worst offender of cancellation or delay. However, the sheer volume of flight means that even if an average of 1% of flights are cancelled, it is still a large number of flight impacted in absolute number.

Same applies to delay. The average delay time of United Flights may not be the worst, but multiplying it by its total number of flights, the result is a lot of time and money wasted

An alternative would be Alaska Airlines. Its volume of domestic flights ranked behind United Air and SkyWest, but its delay metric is second best after Hawaiian Airline

## **Tools**
![tools](/img/tools.png)

## **Credits**
- The Terminal movie poster from Google Image Search
- Domestic Flight Data provided by the United States Department of Transportation, Bureau of Transportation Statistics (BTS). See more [by clicking here.](https://www.transtats.bts.gov/tables.asp?Table_ID=236&SYS_Table_Name=T_ONTIME_REPORTING)
- Climate Data provided by the United States National Centers For Environmental Information, National Oceanic and Atmopheric Administration (NOAA). See more [by clicking here.](https://www.ncdc.noaa.gov/cdo-web/)
- Airport Runway Data provided by the United States Department of Transportation, Federal Aviation Adminstration (FAA). See more [by clicking here.](https://www.faa.gov/airports/airport_safety/airportdata_5010/)

