hostname R2
ip name-server 8.8.8.8
!

interface GigabitEthernet1/0
  description WAN UPLINK
  ip address 192.168.0.11 255.255.255.240
  no shutdown
!

interface FastEthernet0/0
  description WAN
  ip address 192.168.0.18 255.255.255.240
  no shutdown
!


banner login ^c This is a test banner ^c