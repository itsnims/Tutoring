import csv
import os
# import operator

def satisfies_conditions(row, vehicle_type=None, from_year=None, to_year=
         None, years=None):
    if vehicle_type and not row['vehicle_type'] == vehicle_type:
        return False
    year = int(row['year'])
    if from_year and from_year > year:
        return False
    if to_year and to_year < year:
        return False
    if years and year not in years:
        return False
    return True

def municipalities_most_vehicles(file_name, limit=10, vehicle_type=None,
from_year=None, to_year=None, years=None):
    if not os.path.isfile(file_name):
        print('ERROR: "{0}" file not found'.format(file_name))
        exit()

        filtered_municipalities = {}
        with open(file_name,'r',encoding ='utf-8') as csv_file:
            reader = csv.DictTeader(csv_file)
            for row in reader:
                if satisfies_conditions(row, vehicle_type, from_year, to_year, years):
                    filtered_municipalities[row['municipality']] = filtered_municipalities.get(row['municipality'], 0) + int(row['count'])

    values = filtered_municipalities.values()
    values = sorted(values, reverse=True)[:limit]
    result = {}
    for value in values:
        for municipality, number in filtered_municipalities.items():
            if number == value and municipality not in result:
                result[municipality] = number
                if len(result) == limit:
                    return result

print(municipalities_most_vehicles('./vehicles.csv', limit=10, years=[1993]))
# expected printout {'Kloten': 8963, 'Winterthur': 37037, 'Adliswil': 8292, 'Uster': 12366, 'Duebendorf': 11538, 'Dietikon': 10757, 'Horgen': 8265, 'Zuerich': 144826, 'Waedenswil': 9428, 'Wetzikon': 8448}



