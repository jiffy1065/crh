# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:15:15 2020

@author: chenhj
"""

from pygal_maps_world.i18n import COUNTRIES
   
def get_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code