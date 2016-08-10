## Inspiration
This project was inspired by the fact that my friend (who lives across the country) has a very hard time getting up in the morning.  We installed the app "Phone Schedule", which turns on her cell phone up to full volume at 4:00 AM each night.  We also set her text alarm to be an annoying loud noise.  When the textBombAlarmClock.py script reaches wake up time, it texts her repeatedly.  The incoming text messages are loud enough to act as an alarm clock, and now my friend must call me to turn the incoming messages off.  Between the annoying messages and mandatory conversation to shush them, textBombAlarmClock.py acted as a successful alarm clock alternative.  

## About TextBombAlarmClock
- The host email address (to send messages from) must be a Gmail.  You must allow less secure apps to use SMTP server (https://www.google.com/settings/security/lesssecureapps).
- The victim phone number needs to be constructed as an email address (http://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/).
- textBombAlarmClock.py was meant as a one time alarm clock, and will have to be relaunched for every use.

## Preparation & Inputs & Outputs
- 1) Set Gmail account for SMTP usage (link above)
- 2) Set victimPhoneEmail (link above)
- 3) Open textBombAlarmClock.py and set the alarm time (victimRingTime) and time zone difference (host_to_victim_timeDiff).
- 4) Run using: python textBombAlarmClock.py
- 5) The current time information will be output to the terminal.  Alarm sounds when victim time equals alarm time.  When text messages start sending, the current message number sent will output to the terminal.

## Other
Good luck, and tell me how it works!
