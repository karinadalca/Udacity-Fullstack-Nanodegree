from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa2ccab4450079eeec2c16d5c64387e53"
# Your Auth Token from twilio.com/console
auth_token  = "auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16468326987", 
    from_="+12392300453 ",
    body="Hello from Python!")

print(message.sid)
