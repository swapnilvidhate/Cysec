from django.db import models

# Create your models here.

    # home page models here 

class Heading(models.Model):
    heading_small_title = models.CharField(max_length=250)
    heading_title = models.CharField(max_length=250)
    heading_details = models.TextField()
    heading_image = models.ImageField(upload_to='static/')
    heading_video = models.TextField()

class Feature(models.Model):
    feature_image = models.ImageField(upload_to='static/')
    feature_title = models.CharField(max_length=250)
    feature_details = models.TextField()

class About(models.Model):
    about_heading = models.CharField(max_length=250)
    about_details = models.TextField()
    about_image = models.ImageField(upload_to='static/')
    about_point_1_title = models.CharField(max_length=250)
    about_point_1_details = models.TextField()
    about_point_2_title = models.CharField(max_length=250)
    about_point_2_details = models.TextField()
    about_point_3_title = models.CharField(max_length=250)
    about_point_3_details = models.TextField()
    about_point_4_title = models.CharField(max_length=250)
    about_point_4_details = models.TextField()

class ServicesHomePageModel(models.Model):
    service_heading = models.CharField(max_length=250)
    service_details = models.TextField()

class ServiceTab(models.Model):
    service_tab_image = models.ImageField(upload_to='static/')
    service_tab_heading = models.CharField(max_length=250)

class Challenge(models.Model): 
    challege_title = models.CharField(max_length=250)
    challenge_image = models.ImageField(upload_to='static/')
    challenge_1_title = models.CharField(max_length=250)
    challenge_1_details = models.TextField()
    challenge_2_title = models.CharField(max_length=250)
    challenge_2_details = models.TextField()
    challenge_3_title = models.CharField(max_length=250)
    challenge_3_details = models.TextField()
    challenge_4_title = models.CharField(max_length=250)
    challenge_4_details = models.TextField()
    
class Protect(models.Model): 
    protect_heading = models.CharField(max_length=250)
    protect_details_main = models.TextField()

class ProtectTwo(models.Model):
    protect_title = models.CharField(max_length=250)
    protect_details = models.TextField()

class Solutions(models.Model):
    solution_title = models.CharField(max_length=250)
    solution_details = models.TextField()

    # home page models end here


    # about page models start here 

class Counter(models.Model):
    counter_heading = models.CharField(max_length=250)
    counter_details = models.TextField()
    counter_image = models.ImageField(upload_to='static/')
    count_1_title = models.CharField(max_length=250)
    count_1_value = models.CharField(max_length=250)
    count_2_title = models.CharField(max_length=250)
    count_2_value = models.CharField(max_length=250)
    count_3_title = models.CharField(max_length=250)
    count_3_value = models.CharField(max_length=250)
    count_4_title = models.CharField(max_length=250)
    count_4_value = models.CharField(max_length=250)

class Benefits(models.Model):
    benefits_title = models.CharField(max_length=250)
    benefits_details = models.TextField()

class MiniService(models.Model):
    miniservice_image = models.ImageField(upload_to='static/')
    miniservice_title = models.CharField(max_length=250)
    miniservice_details = models.TextField()

class Testimonial(models.Model):
    client_name = models.CharField(max_length=250)
    client_image = models.ImageField(upload_to='static/')
    client_position = models.CharField(max_length=250)
    client_review = models.TextField()
    client_city = models.CharField(max_length=250)

class Members(models.Model):
    members_image=models.ImageField(upload_to='static/')
    members_name=models.CharField(max_length=250)
    members_post=models.CharField(max_length=250)
    members_facebook_link=models.URLField()
    members_twitter_link=models.URLField()
    members_linkedin_link=models.URLField()
    members_instagram_link=models.URLField()

    # about page models end here 

    # services page models start here 

class ServicesPageModel(models.Model):
    services_heading = models.CharField(max_length=250)
    services_image = models.ImageField(upload_to='static')
    services_title = models.CharField(max_length=250)
    services_details = models.TextField()

class SecondServices(models.Model):
    secondTitle = models.CharField(max_length=250)
    secondParagraph = models.TextField()
    secondImage = models.ImageField(upload_to='static/')

class Partners(models.Model):
    logo = models.ImageField(upload_to='static/')

    # services page models end here 

    # contact us page model start here 

class Contact(models.Model):
    user_name = models.CharField(max_length=250)
    user_phone_number = models.IntegerField()
    user_email = models.EmailField()
    user_msg_subject = models.CharField(max_length=250)
    user_message = models.TextField()

    # contact us page models end here