''' WAY 1) Fail, TimeOut, Accuracy : 56%
def convert_list_to_model(players):
    return {
        value : index
        for index, value in enumerate(players)
    }

def call_uprank_position(model, player, calling):
    player.insert(model[calling]-1, player.pop(model[calling]))
    return player

def solution(players, callings):
    answer = []
    
    for calling in callings:
        players = call_uprank_position(convert_list_to_model(players), players, calling)
    
    answer = players
    return answer

'''

# WAY 2) Success
def convert_list_to_model(players):
    value = {}
    rank = {}

    for index, player in enumerate(players):
        value[player] = index
        rank[index] = player

    return {'value' : value, 'rank' : rank}

def call_uprank_position(model, calling):
    # init
    UPPER_CODE = 1
    calling_rank, upper_calling_rank = 0 , 0
    calling_value, upper_calling_value = None , None
     
    # get variable
    calling_rank = model['value'].get(calling) # 3, kai
    upper_calling_rank = model['value'].get(model['rank'].get(calling_rank-UPPER_CODE)) # 2, poe

    calling_value = model['rank'].get(calling_rank) # kai
    upper_calling_value = model['rank'].get(calling_rank-UPPER_CODE) # poe
    
    # set data
    model['value'][calling_value] = upper_calling_rank
    model['value'][upper_calling_value] = calling_rank

    model['rank'][calling_rank] = upper_calling_value
    model['rank'][upper_calling_rank] = calling_value
    
    return model
    
def solution(players, callings):
    answer = []
    model = None
    
    # init model 
    model = convert_list_to_model(players) 
    
    # logic
    for call in callings:
        model = call_uprank_position(model=model, calling=call)
    
    # resut set
    answer = list(model['rank'].values())
    return answer

if __name__ == '__main__':
    result = solution(
            players=["mumu", "soe", "poe", "kai", "mine"]
             ,callings=["kai", "kai", "mine", "mine"]
    )
    print(result)
    answer = ["mumu", "kai", "mine", "soe", "poe"]