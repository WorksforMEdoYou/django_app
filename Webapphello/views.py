from django.shortcuts import redirect, render

#getting the data from success messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Create your views here.
def Homepage(request):
    return render(request, r'Home/HomePage.html') 

def Newsletter(request):

    def validate_email(email):
        import re
        email_regex = r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[@])[^@]+@[A-Za-z0-9]+\.[A-Za-z]+$"
        if re.match(email_regex, email):
            return True
        else:
            return False
        
    if request.method == "POST":
        email = request.POST.get('email')
        if email and validate_email(email):
            # email credientials
            sender_email = "rajeshkumar7102002@gmail.com"
            sender_password = "bejx ygae tukh ziuj"
            recipient_email = email
            # SMTP server settings
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            # Create the Email
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = "Thankyou for visiting my Website."
            body = """I hope this email finds you well. I recently noticed that you visited my website, and I wanted to take this opportunity to reach out to you.
I am currently seeking opportunities in the software development domain, and I understand that you may have knowledge and experience in this field. I am particularly interested in learning more about the roles of "Software Engineer," "Software Developer," "Fullstack Python Engineer," and "AI-ML Engineer."

If you have any insights or recommendations regarding these roles, I would greatly appreciate your guidance. Your expertise and advice would be invaluable to me as I navigate this career path. I assure you that I will always be grateful for your support, and I am committed to making the most of any opportunities that you may suggest.

I kindly request that you consider sharing your knowledge with me by replying to this email. Your assistance will be immensely helpful as I explore potential opportunities in the software development sector.

Thank you very much for taking the time to read my email, and I look forward to hearing from you soon.

Warm regards,
RajeshKumar
rajeshkumar7102002@gmail.com.
                    """
            message.attach(MIMEText(body, "plain"))
            # Set up the SMTP server to send Email
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls() # use the TLS encryption
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, message.as_string())
                server.quit()
                message = ["Subscribing be the first person to get the futurestic updates form us."]
                return render(request, r'Success/Success.html', {'Message': message})
            except Exception as e:
                message = ["Email Cannot Sent Please check again."]
                return render(request, r'Success/Error.html', {"Message": message, "Error": e})
        else:
            message = ["Email Cannot Sent Please check again."]
            return render(request, r'Success/Error.html', {"Message": message})
    else:
        return redirect('Homepage') 
           