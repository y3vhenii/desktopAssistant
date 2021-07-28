import webbrowser

# Send email using browser
def sendEmail(recipient, subject):
    subject = subject.replace(' ', '%20')
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject, new =1)
