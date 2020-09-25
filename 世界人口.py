# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:21:50 2020
@author: chenhj
"""
import json



# pip install pygal_maps_world 需要安装模块

filename='population_data.json'

with open(filename) as f:
    pop_data=json.load(f)
    
for pop_dict in pop_data:
    if pop_dict['Year']=="1998":
        country_name = pop_dict['Country Name']
        
 # float将字符串转化为小数，int则是取整数
        population = int(float(pop_dict['Value']))
#        print(country_name + ": " + str(population))
        
for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])
    

    
    
    
