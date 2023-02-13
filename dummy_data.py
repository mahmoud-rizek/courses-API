import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

import random
from faker import Faker



from coursers.models import CourseReviews, Content, Courses, Instructor

# Functions

def seed_courses(n):
    images = ['1.png', '2.jpg', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.png']
    faker = Faker()
    
    # language = ['Arabic', 'English', 'Germany']

    for _ in range(n):
        fName = faker.name()
        rLang = 'Arabic' #language[random.randint(0,3)]
        fStudent =  random.randint(500,600000)
        # fRate = random.randint(0,5)
        fRequer = faker.text(max_nb_chars=90)
        fSummry = faker.text(max_nb_chars=500)
        fPrice = random.randint(200,5000)
        fImage = images[random.randint(0, 15)]
        Rteacher = Instructor.objects.get(id=random.randint(20,50))
       

        Courses.objects.create(
            name = fName,
            details=fSummry,
            lang= rLang,
            studients=fStudent,
            requerment= fRequer,
            price=fPrice,
            # rate = fRate,
            teacher= Rteacher ,
            created_at= timezone.now()
            
        )

        
    print(f"Successfully seeded {n} courses")


def seed_content(n):
    faker = Faker()
    for _ in range(n):
        fVideos = f"{faker}.mp4"
        fTests = f"{fVideos}_test"
        fFiles = f"{fVideos}.pdf"
        fCourse =  Courses.objects.get(id=random.randint(50, 4000))
        
        Content.objects.create(
            videos= fVideos,
            test= fTests,
            files= fFiles,
            course= fCourse
            
        )
    print(f"Successfully seeded {n} content")

def seed_instructors(n):
    faker = Faker()

    for _ in range(n):
        fName = faker.name()
        fEmail = f"{fName}@gmail.com"
        fStudent =  random.randint(50,600000)
        fRate = random.randint(0,5)
        fSummry = faker.text(max_nb_chars=500)

        Instructor.objects.create(
            name = fName,
            rate = fRate,
            email = fEmail,
            summry = fSummry,
            studients = fStudent
            
        )

    print(f"Successfully seeded {n} instructors")


from django.contrib.auth.models import User
from django.utils import timezone

def seed_reviews(n):
    faker = Faker()
    user = User.objects.get(username="win10")
    for _ in range(n):
        fRate = random.randint(0,6)
        fSummry = faker.text(max_nb_chars=70)
        Rcourse = Courses.objects.get(id=random.randint(2,5150))

        CourseReviews.objects.create(
            user= user,
            created_at= timezone.now(),
            rate = fRate,
            review = fSummry,
            course = Rcourse
        )
    print(f"Successfully seeded {n} reviews")


seed_content(5000)
# seed_instructors(500)
# seed_courses(5000)
# seed_reviews(60000)