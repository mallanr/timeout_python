

1. Regression test is in reg.sh 
2. The main python script is "timeout.py"
3. I expect 2 inputs - one a json file for "Users" and another for "Venues". 
   
   Example
   >> python timeout.py users.json venues.json [ the order of the jsons is immaterial ]
   
   
Places to go:

         Spice of life , 48  Timeout points
         The Cambridge , 34  Timeout points
         (Note : Higher the Timeout points for a Venue, more choices for food/drink)


Places to avoid:

         Tally Joe : [Robert Webb] gets no drinks
         Sultan Sofrasi : [Robert Webb] gets no drinks
         Twin Dynasty :  [David Lang] gets no food
         Spirit House : [Alan Allen] gets no drinks
         El Cantina : [Robert Webb] gets no drinks [Bobby Robson] gets no food
         Fabrique : [David Lang,Robert Webb] gets no drinks
         Wagamama : [Robert Webb] gets no drinks
