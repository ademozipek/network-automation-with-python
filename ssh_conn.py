#Adem ÖZİPEK
#CLI bağlantısı için netmiko kütüphanesinden yararlanıyoruz. / Using netmiko for CLI connections.
from netmiko import ConnectHandler

#Bağlanacağımız cihazı tanımlıyoruz. / Defining the device.
ciscoDevice = {
    'device_type' : 'cisco_ios',
    'host' : '1.1.1.1',
    'username' : 'admin',
    'password' : 'C1sco12345',
    'port' : 22,
    'secret' : ''
}

#Bağlantıyı sağlıyoruz. / Establishing connection.
net_connect = ConnectHandler(**ciscoDevice)

#İstediğimiz komutu gönderiyoruz. / Sending command.
output = net_connect.send_command('sh run')

#Sonuç / Result
print(output)