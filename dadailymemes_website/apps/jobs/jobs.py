# import smtplib

# from django.core.mail import send_mail
# from accounts.models import EmailJob, User, Genres
# from public.giphy import get_gif
# from datetime import time


# def scheduleTimer():
#     users = User.objects.all()
#     for user in users:
#         if hasEmailJob(user) is False:
#             genres = []
#             job = EmailJob()
#             job.user = user
#             job.job_time = time
            
#             for genre in Genres.objects.filter(user):
#                 if genre is True:
#                     genres.append(genre)
#             job.gif = get_gif(genres)
#         else:
#             EmailUser(user)

# def EmailUser(user_arg):
#     if checkTimer(user_arg):
#         sendEmail(user_arg)

# def sendEmail(user_arg):
#     user_email = user_arg.objects.get('email')
#     sender = 'jogta@csu.fullerton.edu'
#     receivers = [user_email]
#     gif = get_gif(user_arg.objects.get())

#     message = f"""From: From Person <{sender}>
#     To: To Person <{receivers}>
#     Subject: SMTP email test
    
#     {gif}

#     This is a test message.
#     """
#     try:
#         smtpObj = smtplib.SMTP('34.83.166.149')
#         smtpObj.sendmail(sender, receivers, message)      
#         has_job_val = user_arg.objects.get('has_job')
#         has_job_val.value = False
#         print("Successfully sent email")
#     except smtplib.SMTPException:
#         print("Error sending email")

# def checkTimer(user_arg):
#     time = EmailJob.objects.filter(user_arg).values('job time')
#     next_time = EmailJob.objects.filter(user_arg).values('next_job')
#     if time >= next_time:
#         return True
#     return False

# def hasEmailJob(user_arg):
#     if EmailJob.objects.filter(user_arg).values('has_job') is True:
#         return True
#     return False
        
    
        
        

    