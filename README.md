# Nba-Scheduling-Algorithm
A scheduling algorithm that creates an optimized schedule for the NBA in order to prevent back and forth traveling, back-to-backs, and load management.

## Restrictions
-82 games per season (October 18th to April 9th; Total of 173 games)
-Mandatory Days Off:
  -Christmas Eve
  -Election Day
  -All star week
-Mandatory Big Ticket Games:
  -Christmas Day
  -Thanksgiving
  -MLK Day
  -Rivals Week
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
