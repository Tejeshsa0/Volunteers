from django.db import models
from helper import keys


class MasterDistrictData(models.Model):
    district = models.CharField(max_length=40)
    dist_prefix = models.CharField(max_length=3)
    
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.district
    

class MasterBlockData(models.Model):
    block = models.CharField(max_length=40)
    block_prefix = models.CharField(max_length=2)
    district = models.ForeignKey(MasterDistrictData, on_delete=models.CASCADE, related_name='blocks')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.block


class MasterCourseData(models.Model):
    title = models.CharField(max_length=90)
    author = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    added_by = models.ForeignKey('user.UserData', null=True, on_delete=models.SET_NULL)
    flag_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class MasterBlogData(models.Model):
    title = models.CharField(max_length=90)
    author = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    added_by = models.ForeignKey('user.UserData', null=True, on_delete=models.SET_NULL)
    flag_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title    

    
class MasterCourseBlogImageData(models.Model):

    class ContentChoices(models.Choices):
        COURSE = keys.COURSE
        BLOG = keys.BLOG

    image = models.ImageField(upload_to='blogs/images/%y/%b/')
    content_type = models.CharField(max_length=20, choices=ContentChoices.choices, default=keys.BLOG)
    course = models.ForeignKey(MasterCourseData, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(MasterBlogData, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.id    
    
    
class MasterCourseBlogVideoData(models.Model):

    class ContentChoices(models.Choices):
        COURSE = keys.COURSE
        BLOG = keys.BLOG

    video = models.FileField(upload_to='blogs/videos/%y/%b/')
    content_type = models.CharField(max_length=20, choices=ContentChoices.choices, default=keys.BLOG)
    course = models.ForeignKey(MasterCourseData, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(MasterBlogData, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.id    