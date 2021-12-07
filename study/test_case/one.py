import pytest
from string import Template

tpe = Template("name is $name, age $age")
d = {'name': 'zty', 'age': 'age'}
print(tpe.substitute(d))
