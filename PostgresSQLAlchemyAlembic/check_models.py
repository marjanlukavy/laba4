from datetime import datetime

from crud import s
from models import Admin, Student

ad1 = Admin(
        first_name='Admin',
        last_name='Admin',
        right=1,
)
st1 = Student(
        first_name='Marian',
        last_name='Lukavyi',
        student_rating=88,
        right=0,
        published=datetime(2016, 11, 18),
        students=ad1
)

st2 = Student(
        first_name='John',
        last_name='Luddkavyi',
        student_rating=75,
        right=0,
        published=datetime(2016, 11, 18),
        students=ad1
)


st3 = Student(
        first_name='John',
        last_name='Luddkavyi',
        student_rating=75,
        right=0,
        published=datetime(2016, 11, 18),
)


s.add(ad1)
s.add(st1)
s.add(st2)
s.add(st3)

s.commit()
s.close()