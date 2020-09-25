# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:37:22 2020

@author: chenhj
"""

import pygal_maps_world.maps

# 创建实例
wm=pygal_maps_world.maps.World()   

wm.title='American Population'

# 方法.add为每个国家增加颜色
wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])

wm.render_to_file('america.svg')