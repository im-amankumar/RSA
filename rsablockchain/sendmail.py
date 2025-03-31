import smtplib

def sendmail(toemail,pbk,blockkey):
    TO = toemail
    SUBJECT = 'blockchainkey'
    TEXT ="publickey:" + pbk +" ----------" +"blockhash:"+blockkey
     
    print(TEXT)
    # Gmail Sign In
    gmail_sender = "sathishproject256@gmail.com"
    gmail_passwd = "ikafwssxlfqhxpem"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()
