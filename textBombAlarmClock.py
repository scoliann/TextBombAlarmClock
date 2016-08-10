import smtplib
import datetime


def sendMessages(hostUsername, hostPassword, victimPhoneEmail, message, numMessages):

	# Log into server
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(hostUsername, hostPassword)

	# Send messages
	for i in range(numMessages):
		print "Message #: ",str(i + 1)
		server.sendmail(hostUsername, victimPhoneEmail, message)


def setAlarm(hostUsername, hostPassword, victimRingTime, host_to_victim_timeDiff, victimPhoneEmail, message, numMessages):

	# Run until time is found
	while True:

		# Get the current hour, minute, and second
		hostTimeStamp = str(datetime.datetime.now())
		hostMinute = int(hostTimeStamp.split(":")[1])
		hostHour = int(hostTimeStamp.split(":")[0].split(" ")[1])

		# Adjust for victim's time zone
		victimHour = (hostHour + host_to_victim_timeDiff) % 24

		# Pring present time info
		print "Host Time:\t", str(hostHour) + ":" + str(hostMinute)
		print "Victim Time:\t", str(victimHour) + ":" + str(hostMinute)
		print "Alarm Time:\t", str(victimRingTime[0]) + ":" + str(victimRingTime[1])
		print ""

		# If the victimRingTime is reached, then send texts
		if (victimHour == victimRingTime[0]) and (hostMinute == victimRingTime[1]):

			# Send text messages
			sendMessages(hostUsername, hostPassword, victimPhoneEmail, message, numMessages)

			# Break out of while loop
			break


if __name__ == "__main__":

	# Text bombing email account details
	#	Host email must allow less secure apps before SMTP server usage:
	#	https://www.google.com/settings/security/lesssecureapps
	hostUsername = "yourEmail@gmail.com"
	hostPassword = "yourEmailsPassword"

	# Victim alarm time details 
	victimRingTime = [1, 10]	# Use military time [hour, minute]
	host_to_victim_timeDiff = 3	# In hours

	# Victim phone details
	#	Details on constructing the proper email address:
	#	http://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/
	victimPhoneEmail = "yourVictimsPhone@messaging.sprintpcs.com"
	
	# Text message parameters
	message = "Ring!"
	numMessages = 100


	# Set text bomb alarm clock
	setAlarm(hostUsername, hostPassword, victimRingTime, host_to_victim_timeDiff, victimPhoneEmail, message, numMessages)

				



















