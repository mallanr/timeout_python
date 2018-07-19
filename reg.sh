#-- Test Only one file given
#-- Expected : "Error: python a_args.py users.json venue.json"
python timeout.py users.json 

#-- Test file with wrong names 
#-- Expected : "Error:An error occured."
python timeout.py usersX.json venueX.json

#-- Test file with correct json files but with wrong "keys"
#-- Error:Expecting 2 json files - one with 'Users' and another with 'Venues' in it
python timeout.py users_vX.json venues_vX.json

#-- Test file with correct json files
#-- Error:Expecting 2 json files - one with 'Users' and another with 'Venues' in it
python timeout.py users_v0.json venues_v0.json

#-- Test file with correct json files
#-- Timeout people can go everywhere in this case, 
#-- the Timeout Points if higher means youhave higher choice here 
python timeout.py users_v1.json venues_v1.json

#-- Test file with correct json files
#-- Error:Expecting 2 json files - one with 'Users' and another with 'Venues' in it
python timeout.py users_v0.json venues_v0.json