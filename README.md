# Exploratory Data Analysis of US Flight Data

![the_terminal_poster](/img/the_terminal_poster.jpg)

# Table of Contents
1. [Overview](#overview)
2. [Questions](#questions)
3. [Data](#Data)
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


## **Conclusion**

## **Credits**
- The Terminal movie poster from Google Image Search
- Domestic Flight Data provided by the United States Department of Transportation, Bureau of Transportation Statistics (BTS). See more [by clicking here.](https://www.transtats.bts.gov/tables.asp?Table_ID=236&SYS_Table_Name=T_ONTIME_REPORTING)
- Climate Data provided by the United States National Centers For Environmental Information, National Oceanic and Atmopheric Administration (NOAA). See more [by clicking here.](https://www.ncdc.noaa.gov/cdo-web/)
- Airport Runway Data provided by the United States Department of Transportation, Federal Aviation Adminstration (FAA). See more [by clicking here.](https://www.faa.gov/airports/airport_safety/airportdata_5010/)
