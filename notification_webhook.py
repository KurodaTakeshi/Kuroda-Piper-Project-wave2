import pymsteams

myTeamsMessage = pymsteams.connectorcard("Teams URL")
myTeamsMessage.title("Notification")
myTeamsMessage.text("The timeboard has been updated. Please access the following URL and check the timeboard. Time Board URL")
myTeamsMessage.send()
