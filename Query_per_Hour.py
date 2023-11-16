import datetime
import xlsxwriter as writer


def queries_per_hour():
    try:
        time_dict = {"00-01": 0,
                     "01-02": 0,
                     "02-03": 0,
                     "03-04": 0,
                     "04-05": 0,
                     "05-06": 0,
                     "06-07": 0,
                     "07-08": 0,
                     "08-09": 0,
                     "09-10": 0,
                     "10-11": 0,
                     "11-12": 0,
                     "12-13": 0,
                     "13-14": 0,
                     "14-15": 0,
                     "15-16": 0,
                     "16-17": 0,
                     "17-18": 0,
                     "18-19": 0,
                     "19-20": 0,
                     "20-21": 0,
                     "21-22": 0,
                     "22-23": 0,
                     "23-00": 0}
        first_time = datetime.datetime.strptime("2019-10-24 00:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        second_time = datetime.datetime.strptime("2019-10-24 01:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        third_time = datetime.datetime.strptime("2019-10-24 02:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        forth_time = datetime.datetime.strptime("2019-10-24 03:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        fifth_time = datetime.datetime.strptime("2019-10-24 04:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        sixth_time = datetime.datetime.strptime("2019-10-24 05:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        seventh_time = datetime.datetime.strptime("2019-10-24 06:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        eighth_time = datetime.datetime.strptime("2019-10-24 07:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        ninth_time = datetime.datetime.strptime("2019-10-24 08:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        tenth_time = datetime.datetime.strptime("2019-10-24 09:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        eleventh_time = datetime.datetime.strptime("2019-10-24 10:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        twelfth_time = datetime.datetime.strptime("2019-10-24 11:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        thirteenth_time = datetime.datetime.strptime("2019-10-24 12:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        fourteenth_time = datetime.datetime.strptime("2019-10-24 13:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        fifteenth_time = datetime.datetime.strptime("2019-10-24 14:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        sixteenth_time = datetime.datetime.strptime("2019-10-24 15:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        seventeenth_time = datetime.datetime.strptime("2019-10-24 16:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        eighteenth_time = datetime.datetime.strptime("2019-10-24 17:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        nineteenth_time = datetime.datetime.strptime("2019-10-24 18:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        twentieth_time = datetime.datetime.strptime("2019-10-24 19:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        twenty_first_time = datetime.datetime.strptime("2019-10-24 20:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        twenty_second_time = datetime.datetime.strptime("2019-10-24 21:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        twenty_third_time = datetime.datetime.strptime("2019-10-24 22:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        twenty_forth_time = datetime.datetime.strptime("2019-10-24 23:00:00.0", '%Y-%m-%d %H:%M:%S.%f').time()
        date_and_time = open("E:/Projects/Shared_Files/Queries_per_Hour.txt", 'r', encoding="utf8")
        query_per_hour_wb = writer.Workbook("E:/Projects/Shared_Files/query_per_hour.xlsx")
        query_per_hour_ws = query_per_hour_wb.add_worksheet()
        for date_time in date_and_time:
            date_time_obj = datetime.datetime.strptime(date_time.strip("\n"), '%Y-%m-%d %H:%M:%S.%f')
            time = date_time_obj.time()
            if first_time <= time < second_time:
                time_dict["00-01"] += 1
            elif second_time <= time < third_time:
                time_dict["01-02"] += 1
            elif third_time <= time < forth_time:
                time_dict["02-03"] += 1
            elif forth_time <= time < fifth_time:
                time_dict["03-04"] += 1
            elif fifth_time <= time < sixth_time:
                time_dict["04-05"] += 1
            elif sixth_time <= time < seventh_time:
                time_dict["05-06"] += 1
            elif seventh_time <= time < eighth_time:
                time_dict["06-07"] += 1
            elif eighth_time <= time < ninth_time:
                time_dict["07-08"] += 1
            elif ninth_time <= time < tenth_time:
                time_dict["08-09"] += 1
            elif tenth_time <= time < eleventh_time:
                time_dict["09-10"] += 1
            elif eleventh_time <= time < twelfth_time:
                time_dict["10-11"] += 1
            elif twelfth_time <= time < thirteenth_time:
                time_dict["11-12"] += 1
            elif thirteenth_time <= time < fourteenth_time:
                time_dict["12-13"] += 1
            elif fourteenth_time <= time < fifteenth_time:
                time_dict["13-14"] += 1
            elif fifteenth_time <= time < sixteenth_time:
                time_dict["14-15"] += 1
            elif sixteenth_time <= time < seventeenth_time:
                time_dict["15-16"] += 1
            elif seventeenth_time <= time < eighteenth_time:
                time_dict["16-17"] += 1
            elif eighteenth_time <= time < nineteenth_time:
                time_dict["17-18"] += 1
            elif nineteenth_time <= time < twentieth_time:
                time_dict["18-19"] += 1
            elif twentieth_time <= time < twenty_first_time:
                time_dict["19-20"] += 1
            elif twenty_first_time <= time < twenty_second_time:
                time_dict["20-21"] += 1
            elif twenty_second_time <= time < twenty_third_time:
                time_dict["21-22"] += 1
            elif twenty_third_time <= time < twenty_forth_time:
                time_dict["22-23"] += 1
            elif twenty_forth_time <= time:
                time_dict["23-00"] += 1
        date_and_time.close()
        i = 0
        for key, value in time_dict.items():
            query_per_hour_ws.write(i, 0, key)
            query_per_hour_ws.write(i, 1, round(value / 3))
            i += 1
        query_per_hour_wb.close()
    except NotADirectoryError:
        print("Sorry, no such a file!!!!")


# queries_per_hour()