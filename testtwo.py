# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:04:45 2021

@author: Shivam Saxena
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Shivam Saxena/Desktop/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 15, False, path, 15)