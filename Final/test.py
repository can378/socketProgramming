

'''
message=input("입력: ")

m=b'\x02'
message=bytes(m)+message.encode('utf-8')




message=bytes(message)
service_code=message[0]
select_code=message[1:]



print("message= "+str(message))
print("byte= "+str(m))
print(str(service_code)+" "+str(select_code))



if(int(service_code)==1):
    print("service code is 1")
if(int(service_code)==2):
    print("service code is 2")
elif int(service_code)==3:
    print("service code is 3")
    
'''

message=input("입력: ")
message=bytes(message,encoding='utf-8')
service_code=message[0]
select=message[1:]

print(f'{service_code} and {select}')


if service_code==49:
    print("1111111111")
