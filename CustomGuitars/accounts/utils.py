import pyotp
import qrcode
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.conf import settings

def send_otp(request,data):
    otp_secret_key = data.get('otp_secret_key', '')
    totp=pyotp.TOTP(otp_secret_key,interval=30)
    otp = totp.at(datetime.now())
    request.session['otp_secret_key']=totp.secret
    valid_date = datetime.now()+timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)
    print(f"One Time Password:{otp}")
    return otp
    
def email_otp(request,otp):
    recipient = request.session['email']
    subject = " Custom Guitars Authentication code"
    message = "Your Authentication code is:"+otp+". Please use this code to complete your login process. Do not share this code with anyone."
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient],fail_silently=False)

    
def generate_qr(data,issuer_name, account_name):
    otp_secret_key = data.get('otp_secret_key', '')

    totp = pyotp.TOTP(otp_secret_key,interval=30)
    
    uri = totp.provisioning_uri(
        name=account_name,
        issuer_name=issuer_name,
    )
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,)
    
    
    qr.add_data(uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img