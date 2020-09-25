# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:11:48 2020
@author: chenhj
"""
import json
# 圆括号()表示函数调用
# 方括号[]表示列表值的引用
import pygal_maps_world.maps
from 世界人口_2 import get_code

filename='population_data.json'

with open(filename) as f:
    pop_data=json.load(f)

# 创建一个空字典
get_population={}
for pop_dict in pop_data:
    if pop_dict['Year']=="2010":
        country_name = pop_dict['Country Name']
        code=get_code(country_name)

# float将字符串转化为小数，int则是取整数
        population = int(float(pop_dict['Value']))
#        print(country_name + ": " + str(population))
        
        if code:
            get_population[code]=population

# 创建实例
wm = pygal_maps_world.maps.World()   
wm.title='World Population'
# 方法.add为每个国家增加颜色
wm.add('2010',get_population)

wm.render_to_file('world population.svg') 
            
 
#            print(code + ':' +str(population))
#        else:
#            print('Error!' + country_name)