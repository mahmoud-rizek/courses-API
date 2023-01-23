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
        fStudent =  random.randint(50,600000)
        # fRate = random.randint(0,5)
        fRequer = faker.text(max_nb_chars=90)
        fSummry = faker.text(max_nb_chars=500)
        fPrice = random.randint(200,5000)
        fImage = images[random.randint(0, 15)]
        Rteacher = Instructor.objects.get(id=random.randint(0,49))
        Rcontent = Content.objects.get(id=random.randint(0, 101))

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


def seed_instructors(n):
    faker = Faker()

    for _ in range(n):
        fName = faker.name()
        fEmail = f"{random.randint(81, 300)}@gmail.com"
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
    for _ in range(n):
        fRate = random.randint(0,6)
        fSummry = faker.text(max_nb_chars=50)
        Rcourse = Courses.objects.get(id=random.randint(0,101))

        CourseReviews.objects.create(
            user= User(),
            created_at= timezone.now(),
            rate = fRate,
            review = fSummry,
            course = Rcourse
        )
    print(f"Successfully seeded {n} reviews")


def seed_content(n):
    videos = ['lesson_1.mp4', 'lesson_2.mp4', 'lesson_3.mp4', 'lesson_4.mp4', 'lesson_5.mp4', 'lesson_6.mp4', 'lesson_7.mp4', 'lesson_8.mp4', 'lesson1.mp_9','lesson_10.mp4']

    tests = ['https://www.youtube.com/watch?v=ExCP4S-DHkQ&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z',
    'https://www.youtube.com/watch?v=bJlxZaCq9e4&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=2',
    'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=3',
    'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=4',
    'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=5',
    'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=6','https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=7',
    'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=8', 'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=9', 'https://www.youtube.com/watch?v=EukekRxwWns&list=PLjM43R2pHZ8XfvO1D6o8DSToE3vOm3N2Z&index=10']

    files = ['file_1.pdf','file_2.pdf','file_3.pdf','file_4.pdf','file_5.pdf','file_6.pdf','file_7.pdf','file_8.pdf','file_9.pdf','file_10.pdf']


    for _ in range(n):
        fVideos = videos[random.randint(0,9)]
        fTests = tests[random.randint(0,9)]
        fFiles = files[random.randint(0,9)]
        
        Content.objects.create(
            videos= fVideos,
            test= fTests,
            files= fFiles,
            
        )
    print(f"Successfully seeded {n} content")

# seed_content(100)
seed_instructors(500)
# seed_courses(5)
# seed_reviews(6000)