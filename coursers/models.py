from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    details = models.TextField(_("details"), max_length=1000)
    teacher = models.ForeignKey("Instructor", related_name='instractor_course',verbose_name=_("Instructor"), on_delete=models.CASCADE)
    image = models.ImageField(_("images"), upload_to='courses_images')
    lang = models.CharField(_("Language"), max_length=50)
    created_at = models.DateTimeField(_("created_at"), default=timezone.now)
    requerment = models.TextField(_("Requerment"), max_length=1000)
    price = models.IntegerField(_("price"))
    studients = models.IntegerField(_("Studient's count"))
    content = models.OneToOneField("Content", verbose_name=_("Content"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(_("Name"), max_length=50)  
    studients = models.IntegerField(_("Studient's count"))
    summry = models.TextField(_("Summry"), max_length=1000)
    email = models.EmailField(_("Email"), max_length=254)
    rate = models.IntegerField(_("Rate"))

    def __str__(self):
        return self.name

class CourseReviews(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user_review"), related_name='user_review',on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    rate = models.IntegerField(_("Rate"))
    review = models.TextField(_("course_review"), max_length=1000)
    course = models.ForeignKey(Courses, verbose_name=_("Course"), related_name='course_review', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course)


class Content(models.Model):
    videos = models.URLField(_("Lessons"), max_length=200)
    files = models.FileField(_("Files"), upload_to="course_files", max_length=100)
    test = models.URLField(_("Test"), max_length=200)

