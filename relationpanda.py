import pandas as pd
from copy import deepcopy

relations = pd.read_csv("lyk_relations_accept.csv")


intNoDupUser = relations.drop_duplicates()

intNoDupUser = intNoDupUser.sort_values(['userId','relativeId'])

intNoDupUserSingleCol = intNoDupUser['userId']

intNoDupUserSingleCol = intNoDupUserSingleCol.drop_duplicates()

allUsers = intNoDupUserSingleCol.values.tolist()

intSuggestiveUserFinal = None
intCommonUserFinal = None


for no,user in enumerate(allUsers):
    print(allUsers[no],no)
    someval = allUsers[no]
    arr = [allUsers[no]]
    intRelativeUserSetForFirstUser = intNoDupUser[intNoDupUser.userId.isin(arr)] 

    intRelativeUserSingleCol = intRelativeUserSetForFirstUser['relativeId']

    allRelUsers = intRelativeUserSingleCol.values.tolist()

    for index,relUser in enumerate(allRelUsers):
        #print(allRelUsers[index],index)
        arr2 = [allRelUsers[index]]
        intFirstRelativeUserFriendSet = intNoDupUser[intNoDupUser.userId.isin(arr2)]
        intFirstSetUserJoined = pd.merge(intRelativeUserSetForFirstUser,intFirstRelativeUserFriendSet,how='inner',on='relativeId')
        if intFirstSetUserJoined.empty:
            intFirstRelativeUserFriendSet = intFirstRelativeUserFriendSet.copy()
            intFirstRelativeUserFriendSet['suggUserId'] = someval
            intSuggestiveUserFinal = pd.concat([intSuggestiveUserFinal,intFirstRelativeUserFriendSet])
        else:
            intCommonUserFinal = pd.concat([intCommonUserFinal,intFirstSetUserJoined])
    #break
    if no % 10000 == 0 :
         intSuggestiveUserFinal = intSuggestiveUserFinal.reset_index(drop=True)
         intSuggestiveUserFinal.to_csv("SUGGESTION" + str(no) + ".csv",sep = ',')
         intCommonUserFinal = intCommonUserFinal.reset_index(drop=True)
         intCommonUserFinal.to_csv("COMMONUSER"+ str(no) + ".csv",sep = ',')

         intSuggestiveUserFinal = None
         intCommonUserFinal = None

intSuggestiveUserFinal = intSuggestiveUserFinal.reset_index(drop=True)
intSuggestiveUserFinal.to_csv("SUGGESTION" + str(no) + ".csv",sep = ',')
intCommonUserFinal = intCommonUserFinal.reset_index(drop=True)
intCommonUserFinal.to_csv("COMMONUSER"+ str(no) + ".csv",sep = ',')
