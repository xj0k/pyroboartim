'''
from pyowm import OWM

API_key = '2ca9531f67ec5094e09d41b81e6b55ab'
owm = OWM(API_key)
#obs = owm.weather_at_place('London,GB')
obs = owm.weather_at_id(1790437)
print(obs.get_reception_time() )
w = obs.get_weather()
print("cloud:%s, rain:%s, temperature:%s" % (w.get_clouds(),w.get_rain(),w.get_temperature(unit='celsius')))

'''

import PySimpleGUIQt as sg

# Demo of how columns work
# window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to window layouts, they are a list of lists of elements.

window = sg.Window('Columns')                                   # blank window

# Column layout
col = [[sg.Text('col Row 1')],
       [sg.Text('col Row 2'), sg.Input('col input 1')],
       [sg.Text('col Row 3'), sg.Input('col input 2')],
       [sg.Text('col Row 4'), sg.Input('col input 3')],
       [sg.Text('col Row 5'), sg.Input('col input 4')],
       [sg.Text('col Row 6'), sg.Input('col input 5')],
       [sg.Text('col Row 7'), sg.Input('col input 6')]]

layout = [[sg.Slider(range=(1,100), default_value=10, orientation='v', size=(8,20)), sg.Column(col)],
          [sg.In('Last input')],
          [sg.OK()]]

# Display the window and get values

window = sg.Window('Compact 1-line window with column', layout)
event, values = window.read()
window.Close()

sg.Popup(event, values, line_width=200)
