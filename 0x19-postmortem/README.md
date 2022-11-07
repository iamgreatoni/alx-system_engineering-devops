# ISSUE SUMMARY

On 23/10/2022 from about 12:15 AM to 6:45 AM (wat), our web-01 server was down, causing all of our users inability to access our services. 

# TIMELINE 

12:15 am: Server breakdown  
01:13 am: The problem was noticed
01:14 am: The PM was notified
01:20 am: All teams were called up to look into the problem
01:30 am – 06:30 am: Server debugging  
06:40 am: Problem fixed and changes were pushed 
06:45 am: Server restart
06:45 am: 93% users were back online  

# ROOT CAUSE AND RESOLUTION

Our platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a result of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards.

The issue was fixed when the master server was temporarily disconnected for memory clean-up then connected back to the load balancer and a round-robin algorithm was configured so that both the master and client servers can handle an equal amount of requests.

# MEASURE AGAINST FUTURE OCCURRENCE  

To prevent similar problems from happening again we will
Create an automated test pipeline for every update push
Add a monitoring software to our servers which will monitor lot of things and one of them Network Traffic requests and responses and configure it to make an alert to the teams when too much non desired responses were sent like 404
Create a tests for every new update and the teams should not push until those tests pass

