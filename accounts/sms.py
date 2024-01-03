from ippanel import Client, Error, HTTPError, ResponseCode

client = Client("8en9TUYaGHPVU-gCdUSCCe4XxHuZhZUp62SQTIkY7ho=")
phone = "09129740477"
otp = 5546
pattern = {
    "code" : otp
}
try:
    bulk_id = client.send_pattern('zz9qp2vzfbtairt', "+983000505", str(phone), patter)
    print(bulk_id)
except Error as e:
    print("Error handled => code: %s, message: %s" % (e.code, e.message))

    if e.code == ResponseCode.ErrUnprocessableEntity.value:
        for field in e.message:
            print("Field: %s , Errors: %s" % (field, e.message[field]))
except HTTPError as e:
    print("Error handled => code: %s" % (e))