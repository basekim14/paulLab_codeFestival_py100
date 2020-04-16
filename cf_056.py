# Code Festival - Python Practice 056
# Author : ㄱㄱㅊ
# Title : List Fx
# Date : 20-04-14

nationWidth = {
    'Korea' : 220877,
    'Rusia' : 17098242,
    'China' : 9596961,
    'France' : 543965,
    'Japan' : 377915,
    'England' : 242900 }

nations = list(nationWidth.keys())[1:]
widths = list(nationWidth.values())[1:]
abs_widths = [abs(width - nationWidth['Korea']) for width in widths]

print(nations[abs_widths.index(min(abs_widths))] + ' ' + str(min(abs_widths)))
