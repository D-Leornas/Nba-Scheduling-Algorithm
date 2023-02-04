# Nba-Scheduling-Algorithm
A scheduling algorithm that creates an optimized schedule for the NBA in order to prevent back and forth traveling, back-to-backs, and load management.

## Restrictions
-Every team plays their:
&nbsp;&nbsp;&nbsp;&nbsp;-Division teams 4 times
&nbsp;&nbsp;&nbsp;&nbsp;-4 conference teams 4 times
&nbsp;&nbsp;&nbsp;&nbsp;-6 conference teams 3 times
&nbsp;&nbsp;&nbsp;&nbsp;-15 other conference teams 2 times
-82 games per season (October 18th to April 9th; Total of 173 games)  
-Mandatory Days Off:  
&nbsp;&nbsp;&nbsp;&nbsp;-Christmas Eve  
&nbsp;&nbsp;&nbsp;&nbsp;-Election Day  
&nbsp;&nbsp;&nbsp;&nbsp;-All star week  
&nbsp;&nbsp;&nbsp;&nbsp;-NCAA National Championship Game
-Mandatory Big Ticket Games:  
&nbsp;&nbsp;&nbsp;&nbsp;-Christmas Day  
&nbsp;&nbsp;&nbsp;&nbsp;-Thanksgiving  
&nbsp;&nbsp;&nbsp;&nbsp;-MLK Day  
&nbsp;&nbsp;&nbsp;&nbsp;-Rivals Week  
-Every team has a schedule they submit for home games  

## End Goal Is To Create An Algorithm That Minimizes:
-Back-to-back games  
-Consecutive long flights  
## And Maximizes:
-Game clustering (Clusters of nearby games)  

## Inputs:
-Team schedules  
-Tolerance for back-to-backs  
-Requirements for 2-day breaks  
-Length of season  
-Big Ticket Games for Special Occasions  
-Mandatory days off  
