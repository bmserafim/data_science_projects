# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East Coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# creating a function that converts numbers with "Prefix-B/M" format (like 100M) to "pure" integers like (1000000)
def get_converted_damages(lst):

  conversion = {"M": 1000000, "B": 1000000000}
  converted_damages = []

  for item in lst:
    if item.isalpha() == True:
      converted_damages.append("Damages not recorded")
    elif "M" in item:
      new_itemM = int(float(item.strip("M")) * conversion["M"])
      converted_damages.append(new_itemM)
    elif "B" in item:
      new_itemB = int(float(item.strip("B")) * conversion["B"])
      converted_damages.append(new_itemB)
    else: converted_damages.append(item)

  return converted_damages

# testing function by updating damages
updated_damages = get_converted_damages(damages)
#print(updated_damages)

# creating a dictionary with all hurricanes, and their respective data
def get_hurricanes_dict():

  hurricanes_dict = {names[i]: {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]} for i in range(len(names))}

  return hurricanes_dict

hurricanes_dict = get_hurricanes_dict()
#print(hurricanes_dict)

# creating a dictionary with hurricanes organized by year:
def get_year_dict():
  
# creating a list with all years (unique values) in which a hurricane was spotted
  years_lst = []
  for (item) in hurricanes_dict.values():
    year = item["Year"]
    years_lst.append(year)
  years_lst = list(dict.fromkeys(years_lst))

#converting the original dict to one with years as keys
  hurricanes_by_year = {}

  for year in years_lst:
    temp_list = []
    for key in hurricanes_dict:
      if hurricanes_dict[key]["Year"] == year:
        temp_list.append(hurricanes_dict[key])
    hurricanes_by_year[year] = temp_list

  return hurricanes_by_year

hurricanes_by_year = get_year_dict()
#print(hurricanes_by_year)

# creating a dictionary with number of times that each area was affected
def get_times_by_areas_dict():

  hurricanes_by_area = {}

  for key in hurricanes_dict:
    for area in hurricanes_dict[key]["Areas Affected"]:
      if area in hurricanes_by_area: hurricanes_by_area[area] += 1
      else: hurricanes_by_area[area] = 1

  return hurricanes_by_area

hurricanes_by_area = get_times_by_areas_dict()
#print(hurricanes_by_area)

#creating a function that finds the most affected area, with the number of times hit by a hurricane
def get_most_affected():

  sort_hurricanes_by_area = sorted(hurricanes_by_area.items(), key=lambda x:x[1], reverse=True)

  most_area = sort_hurricanes_by_area[0][0]
  times_hit = sort_hurricanes_by_area[0][1]

  return most_area, times_hit

most_area, times_hit = get_most_affected()
#print("The area most affected by hurricanes was {}, with {} hits".format(most_area, times_hit))

#creating a dictionary with hurricanes and the respective deaths caused, then finding the deadliest one
def get_deadliest_hurricane():

  hurricanes_by_deaths = {key: values["Deaths"] for key, values in hurricanes_dict.items()}
  sort_hurricanes_by_deaths = sorted(hurricanes_by_deaths.items(), key=lambda x:x[1], reverse=True)

  deadliest_hurricane = sort_hurricanes_by_deaths[0][0]
  deaths = sort_hurricanes_by_deaths[0][1]

  return deadliest_hurricane, deaths, sort_hurricanes_by_deaths

deadliest_hurricane, deaths, sort_hurricanes_by_deaths = get_deadliest_hurricane()
#print("{} was the deadliest hurricane, with {} casualties.". format(deadliest_hurricane, deaths))

#creating a dictionary with hurricanes organized by mortality scale
def get_hurricanes_by_mortality():

  mortality_scale = {0: 0,
                     1: 100,
                     2: 500,
                     3: 1000,
                     4: 10000}

  mortality_ranking = {key:[] for key in mortality_scale.keys()}

  for item in sort_hurricanes_by_deaths:
    if item[1] == mortality_scale[0]: mortality_ranking[0].append(hurricanes_dict[item[0]])
    elif item[1] <= mortality_scale[1]: mortality_ranking[1].append(hurricanes_dict[item[0]])
    elif item[1] <= mortality_scale[2]: mortality_ranking[2].append(hurricanes_dict[item[0]])
    elif item[1] <= mortality_scale[3]: mortality_ranking[3].append(hurricanes_dict[item[0]])
    elif item[1] <= mortality_scale[4]: mortality_ranking[4].append(hurricanes_dict[item[0]])

  return mortality_ranking

mortality_ranking = get_hurricanes_by_mortality()
#print(mortality_ranking)

# finding the hurricane that caused the greatest damage
def get_greatest_damage():

  damages_only_int = []

  #creating a list only with damages as integers
  for item in updated_damages:
    if isinstance(item, int) == True: damages_only_int.append(item)

  #geting the maximum damage registered by a hurricane
  greatest_damage = max(damages_only_int)

  #finding what hurricane caused the maximum damage
  greatest_damage_hurricane = list(hurricanes_dict.keys())[updated_damages.index(greatest_damage)]

  return greatest_damage_hurricane

greatest_damage_hurricane = get_greatest_damage()
#print("Hurricane {} caused the greatest damage.".format(greatest_damage_hurricane))

#creating a dictionary with hurricanes organized by damage scale
def get_hurricanes_by_damage():

  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}

  damage_ranking = {key:[] for key in damage_scale.keys()}

  for key in hurricanes_dict:
    if isinstance(hurricanes_dict[key]["Damage"], int) != True: continue
    if hurricanes_dict[key]["Damage"] == damage_scale[0]: damage_ranking[0].append(hurricanes_dict[key])
    elif hurricanes_dict[key]["Damage"] <= damage_scale[1]: damage_ranking[1].append(hurricanes_dict[key])
    elif hurricanes_dict[key]["Damage"] <= damage_scale[2]: damage_ranking[2].append(hurricanes_dict[key])
    elif hurricanes_dict[key]["Damage"] <= damage_scale[3]: damage_ranking[2].append(hurricanes_dict[key])
    elif hurricanes_dict[key]["Damage"] <= damage_scale[4]: damage_ranking[4].append(hurricanes_dict[key])

  return damage_ranking

damage_ranking = get_hurricanes_by_damage()
#print(damage_ranking)


