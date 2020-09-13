# Uonet+ Vulcan integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

View your vulcan timetable as Home Assistant sensor and use it in automations.

# Timetable
You can get ten entities witch timetable. 
If you want to configure groups and student for which the information will be displayed (default is first on vulcan list), you must add this to your configuration.yaml file to configure groups you must add numbers before group.  
  
example:
```
vulcan:
  student_name: 'Jan Kowalski' #Optional, If is incorrect or none default is first in Vulcan list.
  groups: #optional
    1:
      'J. angielski- p.rozsz': 'A1'
    2:
      'Język niemiecki': 'NA'
    3:
      'Język francuski': 'None' 
    4:
      'Wychowanie fizyczne': 'WF-ch'
    5:
      'Religia': '1'
    6:
      'Informatyka': 'I1'
```
# Graders
Available soon
