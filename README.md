# Neo-Feed-Retrieve-a-list-of-Asteroids-based-on-their-closest-approach-date-to-Earth-

Retrieve a list of Asteroids based on their closest approach date to Earth. 

This application retrives the list of asteroids from NASA's Neo - Feed, sorted with respect to their relative velocity (in miles_per_hour).

This application retrieves the name of the asteroid with closest proximity to earth based on the data between the input date range.

The unit test cases are designed in order to make the application accurate and acceptable.

For running the application as well as test cases, run only one file named test_application.py.

For running just the application, use the file application.py.

Please use python 3.6.3 interpreter to run the programs.

Please install all the following python libraries (if necesary):
1. urllib
2. json
3. datetime
4. sys
5. unittest
6. requests

While running the program, please keep in mind that:

The hourly counters for NASA API key reset on a rolling basis.

Example: If you made 500 requests at 10:15AM and 500 requests at 10:25AM, your API key would become temporarily blocked. This temporary block of your API key would cease at 11:15AM, at which point you could make 500 requests. At 11:25AM, you could then make another 500 requests.

Please input the date range according to the API requirements. Limits are placed on the number of API requests you may make using your API key. Rate limits may vary by service, but the defaults are:
Hourly Limit: 1,000 requests per hour

