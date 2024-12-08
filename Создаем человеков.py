import file_operations
from faker import Faker
from random import randint,sample

random_name =Faker("ru_RU").first_name_male()
random_surname =Faker("ru_RU").last_name_male()
random_job =Faker("ru_RU").job()
random_city =Faker("ru_RU").city()
skills = (
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
    )

current_skills = sample(skills, 3)
context={
    "first_name":random_name,
    "last_name":random_surname,
    "job":random_job,
    "town":random_city,
    "strength":randint(3,18),
    "agility":randint(3,18),
    "endurance":randint(3,18),
    "intelligence":randint(3,18),
    "luck":randint(3,18),
    "skill_1":current_skills,
    "skill_2":current_skills,
    "skill_3":current_skills
}
file_operations.render_template("charsheet.svg","character.svg",context)