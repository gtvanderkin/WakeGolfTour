# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GolfCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.TextField()
    course_total_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolfCourse'
        verbose_name = "Golf Course"
        verbose_name_plural = "Golf Courses"

    def getParList(self):
        holes = Hole.objects.filter(hole_course_id = self.course_id)

        parlist = []

        for hole in holes:
            parlist.append(hole.hole_par)

        return parlist

    def __str__(self):
        return self.course_name


class Hole(models.Model):
    hole_id = models.AutoField(primary_key=True)
    hole_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Hole'

    def __str__(self):
        return "{}, Hole {}, Par {}".format (self.hole_course.course_name,
                                             self.hole_number, self.hole_par)
