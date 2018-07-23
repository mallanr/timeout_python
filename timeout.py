import time
import sys
import re
import json
from pprint import pprint

l_dbg = 0;
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
l_timestr = time.strftime("%Y%m%d-%H%M%S")


def dbg_print(i,j=None,k=None,l=None,m=None):
    if l_dbg > 0:
        print(i,j,k,l,m)
		
for x in sys.argv:
    dbg_print ("Argument: ", x) 

if len (sys.argv) != 3 :
    print ("Error: Need names of 2 files to proceed. Usage :python timeout.py users.json venue.json")
    sys.exit (1)

f1 = sys.argv[1]
dbg_print("f1", f1)
f2 = sys.argv[2]
dbg_print("f2",f2)

r1 = re.search('.json$',f1)
dbg_print(r1);
r2 = re.search('.json$',f2)
dbg_print(r2);

d_dict = dict();
d_ven = dict();
d_user = dict();
#tgtFile = open(l_timestr+"_timeout.log", 'w');


if r1 != None and r2 != None:
    dbg_print("Both are JSON files")

#-- function to check if the files are there or not 
def f_file_exists(l_file):
    global d_user
    global d_ven
    try:
        v_fil = open(l_file, 'rb')
    except IOError :
        raise
    try:
        with open(l_file) as f:
            d_dict = json.load(f)
            if 'Users' in d_dict.keys():
                d_user = d_dict
                dbg_print("users dict pop: ", 'Users' in d_user.keys(), len(d_user["Users"]))
            if 'Venues' in d_dict.keys():
                d_ven = d_dict
                dbg_print("venues dict pop: ", 'Venues' in d_ven.keys(), len(d_ven["Venues"]))
    except FileNotFoundError:
        raise
    except IOError:
        raise
    except:
        raise

try:
    f_file_exists(f1);
except FileNotFoundError:
    print("Error:No such file :", f1 );
    sys.exit(1)
except IOError:
    print("Error:Could not find the file :", f1 );
    sys.exit(1)
except:
    print('Error:An error occured.')
    sys.exit(1)

try:
    f_file_exists(f2);
except IOError:
    print("Error:No such file :", f2 );
    sys.exit(1)
except FileNotFoundError:
    print("Error:No such file :", f2 );
    sys.exit(1)
except:
    print('Error:An error occured.')
    sys.exit(1)

dbg_print('Users' in d_user.keys())
dbg_print('Venues' in d_ven.keys())
#-- do the validation to check if we have got 2 properly formed json files 
if (('Users' not in d_user.keys()) and ('Venues' not in d_ven.keys())):
	print("Error:Expecting 2 json files - one for 'Users' and another for 'Venues'");
	sys.exit(1)
elif not(('Users' in d_user.keys())):
	print("Error:Cannot find a proper json file for 'Users'");
	sys.exit(1)
elif not(('Venues' in d_ven.keys())):
	print("Error:Cannot find a proper json file for 'Venues'");
	sys.exit(1)

dbg_print ("Validation Completed")

    
#pprint(d_user)
#pprint(d_ven)

#-- populate the dictionary object by stripping off any trailing spaces and lowercasing 

		
def prc_pop_dict(l_key,s_set,d_dict):
    ls2= set(w.lower().strip('\t').strip('\n') for w in s_set)
    d_dict[l_key] = ls2


def f_check(l_chk_ven):
    l_err_drink="";
    l_err_food="";
    l_ok = 1;
    l_d_ok = 1;
    l_f_ok = 1;
    l_timeout_points =0;
    for key in d_user_drink:
        dbg_print("------------------------------------------")
        dbg_print("Drinks Menu : ", key, "for ", l_chk_ven)
        s1 = d_ven_drink[l_chk_ven];
        s2 = d_user_drink[key];
        s = s1.intersection(s2)
        dbg_print ("Drinks User Choices : ", s, s1)
        if len(s) == 0:
           if l_d_ok == 1:
               l_err_drink = key
           else:
               l_err_drink = l_err_drink+","+key  
           l_d_ok = 0
        else:
		   #-- Timeout Points if higher means your team have higher choice here 
           l_timeout_points += len(s);
        dbg_print("Food Menu : ", key, "for ", l_chk_ven)
        fs1 = d_ven_food[l_chk_ven];
        fs2 = d_wont_eat[key];
        fs = fs1 - fs2
        dbg_print ("Food User Choices : ",fs)
        if len(fs) == 0:
           if l_f_ok == 1:
               l_err_food = key
           else:
               l_err_food = l_err_food+","+key                   
           l_f_ok = 0
        else:
		   #-- Timeout Points if higher means your team have higher choice here 
           l_timeout_points += len(s);
    #print(l_err_food, " " , l_err_drink)
    if l_d_ok == 0:
       l_err_drink = "[" + l_err_drink + "] gets no drinks" 
       l_timeout_points = 0;
    if l_f_ok == 0:
       l_err_food = "[" + l_err_food + "] gets no food"
       l_timeout_points = 0; 
    if l_d_ok == 0 or l_f_ok == 0:
       l_ok = 0;
    return(l_ok,l_timeout_points,l_err_drink + " " + l_err_food)

l_num_users=len(d_user["Users"])
dbg_print(l_num_users)
l_num_vens=len(d_ven["Venues"])
dbg_print(l_num_vens)

d_user_drink=dict()
d_wont_eat = dict()

for i in range(l_num_users):
    l_username = d_user["Users"][i]["name"]
    #-- the food/drinks name should be standardised for comparison later
    ls1=d_user["Users"][i]["drinks"]   
    prc_pop_dict(l_username,ls1,d_user_drink)
    #-- the food/drinks name should be standardised for comparison later
    lw1=d_user["Users"][i]["wont_eat"]
    prc_pop_dict(l_username,lw1,d_wont_eat)

dbg_print("###########################################")
for key in d_user_drink:
    dbg_print(key, " " , d_user_drink[key]);
dbg_print("###########################################")
for key in d_wont_eat:
    dbg_print(key, " " , d_wont_eat[key]);

d_ven_drink=dict()
d_ven_food= dict()
for i in range(l_num_vens):
    l_username = d_ven["Venues"][i]["name"]
    #-- the food/drinks name should be standardised for comparison later    
    ls1=d_ven["Venues"][i]["drinks"]
    prc_pop_dict(l_username,ls1,d_ven_drink)
    #-- the food/drinks name should be standardised for comparison later
    lw1=d_ven["Venues"][i]["food"]
    prc_pop_dict(l_username,lw1,d_ven_food)

dbg_print("###########################################")
for key in d_ven_drink:
    dbg_print(key, " " , d_ven_drink[key]);
dbg_print("###########################################")
for key in d_ven_food:
    dbg_print(key, " " , d_ven_food[key]);
dbg_print("########## Finally checking user preferences vs venues ##############")

d_avoid = dict()
d_ok_to_eat = dict()
for v in range(l_num_vens):
    l_chk_ven = d_ven["Venues"][v]["name"]
    (l_yes_no, l_pts, l_str) = f_check(l_chk_ven)
    if l_yes_no == 0:
        dbg_print(l_chk_ven , ":" ,l_str)
        d_avoid[l_chk_ven] = l_str
    else:
        dbg_print(l_chk_ven , ":" ,"Ok to eat ,( Timeout Points: ",l_pts," )")
        d_ok_to_eat[l_chk_ven] = l_pts

print(" ")
print("Places to go:")
print(" ")
if len(d_ok_to_eat) == 0:
	print("\t","We are sorry to note that we cannot find any venue which can satisfy your drinks/food list");
else:	
	for key in d_ok_to_eat:
		print("\t", key, "," , str(d_ok_to_eat[key]) ," Timeout points ");
	print("\t","(Note : Higher the Timeout points for a Venue, more choices for food/drink)");
print(" ")
print(" ")
print("Places to avoid:")
print(" ")
for key in d_avoid:
    print("\t",key, ":" , d_avoid[key]);
    #for l_val in d_avoid[key]:
    #    print("\t",l_val);	
