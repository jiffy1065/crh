# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:11:48 2020
@author: chenhj
"""
import json
# 圆括号()表示函数调用
# 方括号[]表示列表值的引用
import pygal_maps_world.maps
from pygal.style import RotateStyle,LightColorizedStyle

from 世界人口_2 import get_code

filename='population_data.json'

with open(filename) as f:
    pop_data=json.load(f)

# 创建一个空字典
get_population,get_pop_1,get_pop_2,get_pop_3={},{},{},{}

for pop_dict in pop_data:
    if pop_dict['Year']=="2010":
        country_name = pop_dict['Country Name']
        code=get_code(country_name)

# float将字符串转化为小数，int则是取整数
        population = int(float(pop_dict['Value']))
#        print(country_name + ": " + str(population))
       
        if code:
            get_population[code]=population

for keys,values in get_population.items():
    if values<100000000:
        get_pop_1[keys]=values
    elif values<1000000000:
        get_pop_2[keys]=values
    else:
        get_pop_3[keys]=values
        

# 创建实例
wm_style=RotateStyle('#331199',base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)   

wm.title='World Population'
# 方法.add为每个国家增加颜色
wm.add('<1e8',get_pop_1)
wm.add('1e8~10e8',get_pop_2)
wm.add('>10e8',get_pop_3)

wm.render_to_file('world population.svg') 
            
 
#            print(code + ':' +str(population))
#        else:
#            print('Error!' + country_name)