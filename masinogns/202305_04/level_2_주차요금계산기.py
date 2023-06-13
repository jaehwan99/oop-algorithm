import math

def solution(fees, records):
    answer = []
    
    record_in = {}
    record_out = {}
    car_number_list = []
    
    # initialize varibles
    hour_to_minute = 60 # 60minute = 1hour
    end_of_time = (23 * hour_to_minute) + 59
    default_time, default_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    
    # time을 분으로 통일
    for record in records:
        time, car_number, inout = record.split(' ')
        hour, minute = time.split(':')
        
        time = (int(hour) * hour_to_minute) + int(minute)
        # print(time, car_number, inout)
        
        # car_number_unique_set
        if car_number not in car_number_list:
            car_number_list.append(car_number)
        
        # data split using inout
        if inout == 'IN':
            if record_in.get(car_number) is None:
                record_in[car_number] = []
            record_in[car_number].append(time)
        else:
            if record_out.get(car_number) is None:
                record_out[car_number] = []
        
            record_out[car_number].append(time)
    
    # 마지막 출차 X case
    for car_number in record_in.keys() :
        len_in = len(record_in.get(car_number))
        if record_out.get(car_number) is None:
            len_out = 0
            record_out[car_number] = []
        else:
            len_out = len(record_out.get(car_number))
        
        if len_in > len_out:
            record_out[car_number].append(end_of_time)
    
    # print(car_number_list, record_in, record_out)
    
    # cal
    for car_number in sorted(car_number_list):
        total_time = 0
        total_fee = 0
        
        for in_time, out_time in zip(record_in[car_number], record_out[car_number]):
            total_time += (out_time-in_time)
        # print('car_number: ', car_number, 'total_time: ', total_time)
        
        if (total_time - default_time) >= 1:
            numbers = math.ceil((total_time - default_time)/unit_time)
            total_fee += (numbers * unit_fee)
        
        total_fee += default_fee
        
        answer.append(total_fee)
        # print(car_number, total_fee)
    return answer

if __name__ == '__main__':
    # assert [14600, 34400, 5000] == solution(
    #     fees=[180, 5000, 10, 600]
    #     , records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT"
    #                , "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN"
    #                , "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
    
    # assert [0, 591] == solution(
    #     fees=[120, 0, 60, 591]
    #     ,records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
    # )
    
    assert [14841] == solution(fees=[1, 461, 1, 10],records=["00:00 1234 IN"])