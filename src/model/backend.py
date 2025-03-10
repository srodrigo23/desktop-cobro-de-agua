

class User:

  def __init__(self, coduser:str, firstname:str, lastname:str, phonenumbers:list, emails:list, metters:list):
    self.coduser = coduser
    self.firstname = firstname
    self.lastname = lastname
    self.phonenumbres = phonenumbers
    self.emails = emails
    self.metters = metters


  def __str__(self):
    print(f'{self.coduser} {self.firstname} {self.lastname}')


from faker import Faker
import uuid
fake = Faker()

for _ in range(10):
  user = User(
    coduser=uuid.uuid4(), 
    firstname=fake.first_name(), 
    lastname=fake.last_name(),
    phonenumbers=[fake.phone_number()], 
    emails=[fake.email()],
    metters=[]
  )
  user.__str__()

