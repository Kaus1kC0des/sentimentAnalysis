from google.cloud import translate_v2 as translate

import os, json

cred= ({
  "type": "service_account",
  "project_id": "swift-capsule-398908",
  "private_key_id": "e51815e0deb263d2d10412d8769a3bf20a986eee",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCad6yUed7+MKjH\nz3W5zDKZLG/FA/OwgFtMpRR1EqocmXLWGmJsEzDPv6UDvWFHzd95q3u5iSP6yOWD\nNCwV5oDEwbQahiDJ0Wlpg4GUd238Q+T6VgJCSEODAxOR4olJafs+NUWLHdM7IqhC\nc44ODH5rBnVvebT3u+2Uq5eQtP3en4EJEjE3xHhADxidN5wjipKuci0gwKkwWOGo\nvTiSRDHnBvw0eKjR5YqfcBhsEfvU6kB5ajwOd8pJG3DkPH6SaGdKxseVXSq/c+je\nLP/ApaxJ6r7VNrjFnbPRpHUz9yMGz6oSOU9Cw3jTHcxHRvlFrtgPV4jJ1XYi8pcB\nNwmHABVFAgMBAAECggEAEatiY7qcKk4VJIQkBpyn5hMp9uq4j8ZjCz2v/SNlL6/S\n7dBnVU8NrJoSzX52mBDiASg/Vy4rnjaoYG2RpHCxZrB0wnr42bU5fm8jXcEapPp8\nQTGhAQWEqYIq1SuJgkscCRXtblg7Tz6r6iwPQiamOGZs/RM6QwNtji3hwNUfXD2L\nlpaw04puxF8njeOFvg0qDaQ07AeaQNNltlKrucxL14yNzjc3KGpne4OCFE+IlgZH\nDq0HjCt4rw6rKwRzeyEViba8sIhgFuXlCg90IMMsGkZOLktC5ID4qfRx76UHuZgm\nL3vQ99Tdxom0UqWwPkWZ4dQZxIkvZC7jbILaQ+rmaQKBgQDV8OXUPX2WVurxOv7t\nUxwcKLuGQg9COtOI+KtikKlZhCihcXfBvztkeCwnppAEI/H/c7Q4WvZ1Z4mh/QUO\n3gMFSFvSRmxi4D7ZGHDrb2a3OAMZ1Wrqa0DZC/BRL41ytIy81VgO1tNoXX6WnkZW\nTEPEFBh0V+BRDIPPmLwNHR24yQKBgQC41aBKW+f1DINI1r2iVsyN+L26FCR68ltn\nFzw0HpzqO9/9dbeQt2JzMcH6Y/FPoRhz8FKgkiZ+dsscECXF9cmX5u+toXlv+UwH\nQzQlc81XsQnNftihf7eFSyI/HFfijIodsrDdiml9y+gJBmw/6XNnqfC3FFnDy6oV\nATCgpfqynQKBgQCG1lp0BwFVNJjEyzMKrrvjv4RZHN9zFZJnHJsf9x7VDWdyQQqC\ncR1kuBzULLVN9r26C9mFP0dgPY5QKyD5+tEajj1Y7Qu40a6qsy3QJRku1r2VlZ3Z\n+xkW8uBWusrCharCBRCH4bvCZlK3aS/Zih2XwjabdRsq2eFlgNTcywIFiQKBgCGe\nOVlM/hOEAxzscfFk+C+aXmfJ4hi6nAVUJI8WQlQYL9VZ49legXmSQ0XXh7yEAH6V\n53FtI7M8yBSCm1w2KESIrG9YP04uebWYc5OcTGz2tmG6AIzfPfHwiHoSHaoHBdgA\n+EpTMny+6aU6ldXKEEN6lV23Rdxm3riTTtTpW3/BAoGBAKATqsn/S1BCZ7kz5RNf\nF1keqsjYmlRj5eLJG9Zl3YZMXv0DyuVYVhmHM6Y1NVZ9XqODgLnTBstux4ddJN1u\nIqRz+fa89fe1rD0QVb2EFlq5hb9jxSb0+v3ey/WliCUCf45S+QOXXLX+UBjS0fHK\nz5LRUVlsF47/YhXVKfQRC2eJ\n-----END PRIVATE KEY-----\n",
  "client_email": "senti-translation@swift-capsule-398908.iam.gserviceaccount.com",
  "client_id": "105921733864080309255",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/senti-translation%40swift-capsule-398908.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

# if os.path.exists('cred.json'):
#     pass
# else:
#     with open('cred.json','w') as credfile:
#         json.dump(cred, credfile)

def translation(str):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cred.json'

    translateClient = translate.Client()

    detect=translateClient.detect_language("str")
    # print(detect['language'])
    if detect == 'en':
        return str

    else:
        translated=translateClient.translate(str,'en')
        return (translated['translatedText'])

s=input("tweet: ")

translation(s)
