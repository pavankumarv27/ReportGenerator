from datetime import datetime
import calendar
import random
from create_report import write_excel


def get_dates(month, year):
    num_of_days_in_month = calendar.monthrange(year, month)[1]

    calculate_starting_day_of_month = datetime.strptime('1-4-2022', '%d-%m-%Y')
    print(calculate_starting_day_of_month.strftime('%A'))

    print(num_of_days_in_month)
    month_dates = []
    everything = []
    for n in range(1, num_of_days_in_month+1):
        date = f"{n}.{month}.{year}"
        day = datetime.strptime(date, '%d.%m.%Y').strftime('%A')
        if day not in ['Saturday', 'Sunday']:
            #print(date, ':', day)
            pass
        date_and_day = date, day
        print(date, ':', day)
        month_dates.append(date_and_day)
    return month_dates


def calculate_duration(dur, dt):

    ##################################################################################
    # Morning
    dt += f'.9:30'
    rand = [00, 10, 20, 30, 45, 15, 50]
    rand2 = [5, 10]

    rand_choice = random.choice(rand)
    final_rand = random.choice([rand_choice +
                               random.choice(rand2), abs(rand_choice - random.choice(rand2))])

    if final_rand == 60:
        final_rand -= 5

    dep_tim = f'.{9 - int(dur)}:{rand_choice}'
    arr_time = f'.{9}:{final_rand}'

    updated_dep_time = datetime.strptime(
        dep_tim, '.%H:%M').strftime('%H:%M') + ' AM'
    updated_arr_time = datetime.strptime(
        arr_time, '.%H:%M').strftime("%H:%M") + ' AM'

    ##################################################################################
    # Evening

    dt = dt[:-5]
    dt += f'.5:30'

    rand_choice = random.choice(rand)
    final_rand = random.choice([rand_choice +
                               random.choice(rand2), abs(rand_choice - random.choice(rand2))])

    if final_rand == 60:
        final_rand -= 5

    ending_dep_time = f'.{5}:{final_rand}'
    ending_arr_time = f'.{5 + int(dur)}:{rand_choice}'

    updated_ending_dep_time = datetime.strptime(
        ending_dep_time, '.%H:%M').strftime('%H:%M') + ' PM'
    updated_ending_arr_time = datetime.strptime(
        ending_arr_time, '.%H:%M').strftime("%H:%M") + ' PM'

    #print("ending_dep_time:", updated_ending_dep_time)
    #print("ending_arr_time", updated_ending_arr_time)

    return updated_dep_time, updated_arr_time, updated_ending_dep_time, updated_ending_arr_time


def get_text(month, year):
    month_days = get_dates(month, year)
    x = 6
    with open('places.txt') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split('-')

            possible_holiday = False

            if len(data) > 4:
                from_date = int(data[0])
                to_date = int(data[1])
                from_place = data[2]
                to_place = data[3]
                duration_to_travel = data[4]
                travel_mode = data[5]
                distance_km = data[6]
                fare = data[7]
                lodge_bill = data[8]
                DA_amount = data[9]
            else:
                from_date = int(data[0])
                to_date = int(data[1])
                possible_holiday = True

            #x = 6
            #input("Check 1")
            for i in range(from_date, to_date+1):
                date_value = f'{i}.{month}.{year}'
                day = datetime.strptime(date_value, '%d.%m.%Y').strftime('%A')

                dep_time, arr_time, ending_dep_time, ending_arr_time = calculate_duration(
                    duration_to_travel, date_value)

                if possible_holiday:
                    print(date_value, 'Possible Holiday')
                    possible_holiday = False
                    write_excel(r=i+x, c=1, v=date_value)
                    write_excel(r=i+x, c=2, v='Holiday / Leave')

                elif day not in ['Saturday', 'Sunday']:

                    row_val_1 = date_value, from_place, to_place, dep_time, arr_time, travel_mode, distance_km, fare, lodge_bill, DA_amount

                    row_val_2 = date_value, to_place, from_place, ending_dep_time, ending_arr_time, travel_mode, distance_km, fare, lodge_bill, DA_amount

                    print(row_val_1)
                    print(row_val_2)

                    write_excel(r=i+x, c=1, v=date_value)
                    write_excel(r=i+x, c=2, v=from_place)
                    write_excel(r=i+x, c=3, v=to_place)
                    write_excel(r=i+x, c=4, v=dep_time)
                    write_excel(r=i+x, c=5, v=arr_time)
                    write_excel(r=i+x, c=6, v=travel_mode)
                    write_excel(r=i+x, c=7, v=distance_km)
                    write_excel(r=i+x, c=8, v=fare)
                    write_excel(r=i+x, c=9, v=lodge_bill)
                    write_excel(r=i+x, c=10, v=DA_amount)
                    x += 1
                    write_excel(r=i+x, c=1, v=date_value)
                    write_excel(r=i+x, c=2, v=to_place)
                    write_excel(r=i+x, c=3, v=from_place)
                    write_excel(r=i+x, c=4, v=ending_dep_time)
                    write_excel(r=i+x, c=5, v=ending_arr_time)
                    write_excel(r=i+x, c=6, v=travel_mode)
                    write_excel(r=i+x, c=7, v=distance_km)
                    write_excel(r=i+x, c=8, v=fare)
                    write_excel(r=i+x, c=9, v=lodge_bill)
                    write_excel(r=i+x, c=10, v='')

                    #input('1 row updated')

                else:
                    print(date_value, 'Saturday or Sunday')
                    write_excel(r=i+x, c=1, v=date_value)
                    write_excel(r=i+x, c=2, v='Saturday or Sunday')

                #input("Checking for 2--------------------------------------")


if __name__ == '__main__':
    get_text(8, 2022)
