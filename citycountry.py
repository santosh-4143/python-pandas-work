import pandas as pd

citycountry = pd.read_csv("lyk_user_city_country.csv")

intwithoutid = citycountry.iloc[0:,1:4]


intsort = intwithoutid.sort_values(['userId','city','country'])

intNoDupl = intsort.drop_duplicates()


intNoDupUser = intNoDupl.iloc[0:,0:1]

intNoDupUser = intNoDupUser.drop_duplicates()

intNoDupUser = intNoDupUser.sort_values(['userId'])

#intNoDupUser.to_csv("sample1.csv",sep = ',')

allitems = intNoDupUser.values.tolist()


#intsort.to_csv("sample.csv",sep = ',')

someone = len(allitems)
intUserFinal = None

for no,item in enumerate(allitems):
    print(allitems[no],no)
    intUser1 = intNoDupl[intNoDupl.userId.isin(allitems[no])]
    
    intUser2 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+1)])]
    intUserJoined = pd.merge(intUser1,intUser2,        how='inner',on=['city','country'])

    intUser3 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+2)])]
    intUserJoined1 = pd.merge(intUser1,intUser3,       how='inner',on=['city','country'])
    
    intUser4 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+3)])]
    intUserJoined2 = pd.merge(intUser1,intUser4,       how='inner',on=['city','country'])
    
    intUser5 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+4)])]
    intUserJoined3 = pd.merge(intUser1,intUser5,       how='inner',on=['city','country'])

    intUser6 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+5)])]
    intUserJoined4 = pd.merge(intUser1,intUser6,       how='inner',on=['city','country'])
    
    intUser7 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+6)])]
    intUserJoined5 = pd.merge(intUser1,intUser7,       how='inner',on=['city','country'])
    
    intUser8 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+7)])]
    intUserJoined6 = pd.merge(intUser1,intUser8,       how='inner',on=['city','country'])
    
    intUser9 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+8)])]
    intUserJoined7 = pd.merge(intUser1,intUser9,       how='inner',on=['city','country'])
    
    intUser10 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+9)])]
    intUserJoined8 = pd.merge(intUser1,intUser10,      how='inner',on=['city','country'])
    
    intUser11 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+10)])]
    intUserJoined9 = pd.merge(intUser1,intUser11,      how='inner',on=['city','country'])

    intUser12 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+11)])]
    intUserJoined10 = pd.merge(intUser1,intUser12,      how='inner',on=['city','country'])

    intUser13 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+12)])]
    intUserJoined11 = pd.merge(intUser1,intUser13,      how='inner',on=['city','country'])

    intUser14 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+13)])]
    intUserJoined12 = pd.merge(intUser1,intUser14,      how='inner',on=['city','country'])

    intUser15 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+14)])]
    intUserJoined13 = pd.merge(intUser1,intUser15,      how='inner',on=['city','country'])

    intUser16 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+15)])]
    intUserJoined14 = pd.merge(intUser1,intUser16,      how='inner',on=['city','country'])

    intUser17 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+16)])]
    intUserJoined15 = pd.merge(intUser1,intUser17,      how='inner',on=['city','country'])

    intUser18 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+17)])]
    intUserJoined16 = pd.merge(intUser1,intUser18,      how='inner',on=['city','country'])

    intUser19 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+18)])]
    intUserJoined17 = pd.merge(intUser1,intUser19,      how='inner',on=['city','country'])

    intUser20 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+19)])]
    intUserJoined18 = pd.merge(intUser1,intUser20,      how='inner',on=['city','country'])

    intUser21 = intNoDupl[intNoDupl.userId.isin(allitems[someone-(no+20)])]
    intUserJoined19 = pd.merge(intUser1,intUser20,      how='inner',on=['city','country'])


    intUserFinal = pd.concat([intUserFinal,intUserJoined,intUserJoined1,intUserJoined2,intUserJoined3,intUserJoined4,intUserJoined5
        ,intUserJoined6,intUserJoined7,intUserJoined8,intUserJoined9,intUserJoined10,intUserJoined11,intUserJoined12,
        intUserJoined13,intUserJoined14,intUserJoined15,intUserJoined16,intUserJoined17,intUserJoined18,intUserJoined19])
    

    #break
    
    
    

    if no % 10000 == 0 :
         intUserFinal = intUserFinal.reset_index(drop=True)
         intUserFinal.to_csv("CityCountry" + str(no) + ".csv",sep = ',')
         intUserFinal = None
    
intUserFinal = intUserFinal.reset_index(drop=True)
intUserFinal.to_csv("CityCountry" + str(no) + ".csv",sep = ',')
intUserFinal = None



    





