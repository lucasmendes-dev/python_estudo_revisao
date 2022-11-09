from twilio.rest import Client

account_sid = "AC5809954ad2f8226e7a735d9bbd9ababd"
token = "484a6884d6699f38d65ce684b7bcdc16"
client = Client(account_sid, token)

number = "+18176704359"
destino = "+5531992467832"

message = client.messages.create(
                              body='Hello World!',
                              from_=number,
                              to=destino
                          )

print(message.sid)


#necessário autenticar o nº de telefone que será enviado o SMS