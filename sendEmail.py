import webbrowser
def sendEmail(recipient, subject):
    subject = subject.replace(' ', '%20')
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject, new =1)
