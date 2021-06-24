def mail(to, text):
    import smtplib  
    server = smtplib.SMTP_SSL( "smtp.gmail.com", 465 )
    server.login( "varunkushwah15@gmail.com", "XXXXXXXXXX" )
    server.sendmail( "varunkushwah15@gmail.com", to, text )
    server.quit()
