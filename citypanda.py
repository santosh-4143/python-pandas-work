import pandas as pd

cities = pd.read_csv("lyk_user_city_country.csv",names=["id","userId","city"],index_col=[0],usecols=[0,1,2],header=0)
#coutries = pd.read_csv("lyk_user_city_country.csv",names=["id","userId","country"],index_col=[0],usecols=[0,1,3],header=0)
#cities.to_csv("correctcity.csv",sep = ',')
#coutries.to_csv("correctcountry.csv",sep = ',')
# first we work for only cities for 10
# then we work for countries for 10

interests = pd.read_csv("lyk_user_interestName.csv",names=["id","Interest","userId"],index_col=[0],usecols=[0,1,2],header=0)
intSortInterests = interests.sort_values(['userId','Interest'])
intSortInterests = intSortInterests.drop_duplicates()
#intSortInterests.to_csv("correctinterest.csv",sep = ',')


# sorting city wise
intSortCity = cities.sort_values(['userId','city'])
intSortCity = intSortCity.drop_duplicates()

intNoDupUserCity = intSortCity.iloc[0:,0:1]

intNoDupUserCity = intNoDupUserCity.drop_duplicates()
intNoDupUserCity = intNoDupUserCity.sort_values(['userId'])

allUsersCity = intNoDupUserCity.values.tolist()

someone = len(allUsersCity)
intUserFinal = None

repeat = 1
counter = 0

for no,user in enumerate(allUsersCity):
    print(allUsersCity[no],no)
    # with whom the map is required
    intCurrentUser = intSortCity[intSortCity.userId.isin(allUsersCity[no])]
    #intCurrentUser = intSortCity[intSortCity.userId.isin([6858])]
    
    cityname = intCurrentUser.city.values[0]
    if (cityname == "all" or cityname == "" or cityname == None):
        continue
    #check for every user
    while True:
        #print("someone --" + str(allUsersCity[no]))
        
        #if allUsersCity[no] == [65]:
            #print("someone --"+str(someone))
            #print("repeat --"+str(repeat))
    
        intNextUser = intSortCity[intSortCity.userId.isin(allUsersCity[someone - repeat])]
        #Here city is merged
        intUserJoined = pd.merge(intCurrentUser,intNextUser,        how='inner',on='city')
        
        if not intUserJoined.empty:
            #Now Interest Mapping
            intCurrentUserInterest = intSortInterests[intSortInterests.userId.isin(allUsersCity[no])]
            #print("intCurrentUserInterest")
            #print(intCurrentUserInterest)
            if intCurrentUserInterest.empty:
                repeat = 1
                counter = 0
                break    
            intNextUserInterest = intSortInterests[intSortInterests.userId.isin(allUsersCity[someone - repeat])]
            #print("intNextUserInterest")
            #print(intNextUserInterest)
            intUserInterestJoined = pd.merge(intCurrentUserInterest,intNextUserInterest,        how='inner',on='Interest')
            if not intUserInterestJoined.empty:
                #print("Done")
                intFinalUserJoined = pd.merge(intUserJoined,intUserInterestJoined,        how='inner',on=['userId_x','userId_y'])
                intUserFinal = pd.concat([intUserFinal,intFinalUserJoined])
                counter += 1
                repeat += 1
            else:
                repeat += 1    
        else:
            repeat += 1 
        if repeat == 500:
            repeat = 1
            counter = 0
            break
        if counter == 5:
            repeat = 1
            counter = 0
            break    
    
    if no % 10000 == 0 :
        if intUserFinal is not None:
            intUserFinal = intUserFinal.reset_index(drop=True)
            intUserFinal.to_csv("usercitymatch" + str(no) + ".csv",sep = ',')
            intUserFinal = None

if intUserFinal is not None:
    intUserFinal = intUserFinal.reset_index(drop=True)
    intUserFinal.to_csv("usercitymatchLast.csv",sep = ',')
    intUserFinal = None
    