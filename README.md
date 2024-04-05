# Finding the best Open-Source Python API/library for financial data.
Data is the foundamental brick of any financial study and project so, before getting started with one, each developer should firstly choose the right tool that enables him to find good quality data.

This paper presents a systematic evaluation of various open-source financial APIs, aiming to provide clarity and guidance to developers and researchers seeking to integrate financial data into their Python projects.

Our study assesses each API across multiple metrics, including response time, error handling, handling of null values and data cost. By rigorously analyzing these factors, we offer an objective comparison to aid users in selecting the optimal API for their and our specific requirements.


## Code structure
api_functionspy: This folder contains a python script for each API we evaluated. Each script has three function with the same input/output values  in order to have stardard methods to compare APIs.
helpers.py: This small file contains some methods that can be useful to clean, pickle and load dataframe.
evalutators.py: This file contains all the functions used in main.py to evalute APIs.
main.py: The mail file contains the process and the calculations we used to compare the APIs as we will describe in README.
README.md: This file, providing an overview of the project and instructions.

Usage to replicate this script:

Install the required Python libraries listed in `requirements.txt`.

Execute the main.py `script`.

## Performance metrics
As we said before, we focused on different performance metrics for different usages.
If not clearly specified, we will consider only APIs that offer free access to their data.
This is the list of parameters and features we are going to discuss and evaluate.

<ul> 
    <li>Last update of a quote price</li>
    <li>Longest daily timeserie available</li>
    <li>Minimum time frequency available </li>
    <li>Nan values in a timeserie</li>
    <li>Deviation from the average values in a timeserie</li>
    <li>Time delay of the request </li>
    <li>Minimum time frequency available </li>

</ul>

In main.py we will create a simple dataframe containing in the rows all the api or libraries we will consider and in the columns all the parameters we previously mentioned in order to have a overview of the comparison and in order to be able to filter specific caratteristics.


