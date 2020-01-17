import pymsteams

myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/7ebfd00e-8085-4f53-a1e1-3c46b840fcda@945c199a-83a2-4e80-9f8c-5a91be5752dd/IncomingWebhook/611b022044984ab19ed740dfeb2d477d/839376f8-7b3b-46a0-90b7-4f61f7172ea3")
myTeamsMessage.title("Notification")
myTeamsMessage.text("The timeboard has been updated. Please access the following URL and check the timeboard. http://35.189.138.28:3000")
myTeamsMessage.send()