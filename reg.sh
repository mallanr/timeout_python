#-- "Error:Expecting 2 json files - one for 'Users' and another for 'Venues'"
python timeout.py users_vX.json venues_vX.json

#-- Error:Cannot find a proper json file for 'Users'
python timeout.py users_vX.json venues_v0.json

#-- Error:Cannot find a proper json file for 'Venues'
python timeout.py users_v0.json venues_vX.json

#-- Error:No such file : userss.json
python timeout.py userss.json abc

#-- We are sorry to note that we cannot find any venue which can satisfy your drinks/food list
python timeout.py users_v0.json venues_none.json

#-- proper json files provided, 2 veunes should be ok to eat 
python timeout.py users_v0.json venues_v0.json

#-- proper json files provided , 2 veunes should be ok to eat 
#-- the order of the json files is switched , result should match above 
python timeout.py venues_v0.json users_v0.json 