
!
ip access-list standard SIPR-HAIPE-CT-IP-ACL
permit 10.101.155.254 0.0.0.0
ip access-list standard NIPR-HAIPE-CT-IP-ACL
permit 10.255.255.155 0.0.0.0
!
class-map match-all IMEF-BC-SIPR-VOICE-CLASS
description Assured Voice & Non-Assured Voice from SIPR HAIPE
match dscp cs4 41 43 45 EF 47 49
match access-group name SIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-NIPR-VOICE-CLASS
description Assured Voice & Non-Assured Voice from NIPR
match dscp cs4 41 43 45 EF 47 49
match access-group name NIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-COMMON-SIG-CLASS
description Signaling_All Network and VoIP Signaling
match dscp cs5 cs6
class-map match-any IMEF-BC-VTC-CLASS-DSCP
description Assured and Non-Assured Multimedia Conferencing
match dscp af32 af33 af41 af42 af43
match dscp 33 35 37 39 51
class-map match-all IMEF-BC-SIPR-VTC-CLASS
description Assured and Non-Assured Multimedia Conferencing from SIPR HAIPE
match class-map IMEF-BC-VTC-CLASS-DSCP
match access-group name SIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-NIPR-VTC-CLASS
description Assured and Non-Assured Multimedia Conferencing from NIPR
match class-map IMEF-BC-VTC-CLASS-DSCP
match access-group name NIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-SIPR-STREAM-CLASS
description Broadcast Video & Multimedia Streaming from SIPR HAIPE
match dscp cs3 af31 25 27 29 31
match access-group name SIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-NIPR-STREAM-CLASS
description Broadcast Video & Multimedia Streaming from NIPR
match dscp cs3 af31 25 27 29 31
match access-group name NIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-COMMON-OA&M-CLASS
description ALL OA&M Network Management traffic
match dscp cs2
class-map match-any IMEF-BC-MSNDATA-CLASS-DSCP
description High Throughput & Low-Latency Data
match dscp af21 af22 af23
match dscp 9 11 13 15 17 19 21 23
class-map match-all IMEF-BC-SIPR-MSNDATA-CLASS
description Business & Mission Important Data from SIPR HAIPE
match class-map IMEF-BC-MSNDATA-CLASS-DSCP
match access-group name SIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-NIPR-MSNDATA-CLASS
description Business & Mission Important Data from NIPR HAIPE
match class-map IMEF-BC-MSNDATA-CLASS-DSCP
match access-group name NIPR-HAIPE-CT-IP-ACL
class-map match-all IMEF-BC-COMMON-SCAV-CLASS
description All Scavenger Traffic
match dscp cs1
class-map match-all IMEF-BC-SIPR-DEFAULT-CLASS
description Default queue for traffic from SIPR HAIPE
match access-group name SIPR-HAIPE-CT-IP-ACL
!
policy-map BLACK-POLICY-EGRESS-QUEUING
class IMEF-BC-SIPR-VOICE-CLASS 
 priority percent 15
class IMEF-BC-NIPR-VOICE-CLASS
 priority percent 15
class IMEF-BC-COMMON-SIG-CLASS
 bandwidth remaining percent 4
class IMEF-BC-SIPR-VTC-CLASS
 bandwidth remaining percent 20
class IMEF-BC-SIPR-STREAM-CLASS
 bandwidth remaining percent 10
class IMEF-BC-SIPR-MSNDATA-CLASS
 bandwidth remaining percent 20
random-detect dscp-based
class IMEF-BC-NIPR-MSNDATA-CLASS
 bandwidth remaining percent 10
random-detect dscp-based
class IMEF-BC-COMMON-OA&M-CLASS
bandwidth remaining percent 4
class IMEF-BC-COMMON-SCAV-CLASS
bandwidth remaining percent 1
class IMEF-BC-SIPR-DEFAULT-CLASS
 bandwidth remaining percent 15
random-detect dscp-based
class IMEF-BC-NIPR-STREAM-CLASS
 bandwidth remaining percent 5
class class-default bandwidth
 remaining percent 10
random-detect dscp-based
!
policy-map BLACK-POLICY-EGRESS-SHAPING-100MB
class class-default
shape average 100000000 1000000 1000000
service-policy BLACK-POLICY-EGRESS-QUEUING
policy-map BLACK-POLICY-EGRESS-SHAPING-50MB
class class-default
shape average 50000000 500000 500000
service-policy BLACK-POLICY-EGRESS-QUEUING
policy-map BLACK-POLICY-EGRESS-SHAPING-14MB
class class-default
shape average 14000000 140000 140000
service-policy BLACK-POLICY-EGRESS-QUEUING
policy-map BLACK-POLICY-EGRESS-SHAPING-8MB
class class-default
shape average 8192000 81920 81920
service-policy BLACK-POLICY-EGRESS-QUEUING
policy-map BLACK-POLICY-EGRESS-SHAPING-6MB
class class-default
shape average 6144000 61440 61440
service-policy BLACK-POLICY-EGRESS-QUEUING
policy-map BLACK-POLICY-EGRESS-SHAPING-4MB
class class-default
shape average 4096000 40960 40960
!
service-policy BLACK-POLICY-EGRESS-QUEUING
policy-map BLACK-POLICY-EGRESS-SHAPING-2MB
class class-default
shape average 2048000 20480 20480
service-policy BLACK-POLICY-EGRESS-QUEUING

policy-map BLACK-POLICY-EGRESS-SHAPING-1MB
class class-default
shape average 1024000 10240 10240
service-policy BLACK-POLICY-EGRESS-QUEUING
!
policy-map BLACK-POLICY-LINKWAY-EGRESS-SHAPING
class class-default 
shape average 3008000 30080 30080 
service-policy BLACK-POLICY-EGRESS-QUEUING
!
crypto key generate rsa mod 2048 label IKEV2-DMVPN
!
crypto key generate rsa label ssh-rsa modulus 2048
!
ntp server vrf bc 10.16.48.121 prefer
ntp server vrf bc 10.20.5.121 
ntp server 137.232.58.123
ntp server 137.232.60.123
!
clock timezone PST -8 0
clock summer-time PST recurring
service timestamps log datetime localtime
!
!
aaa session-id common
!
crypto pki trustpoint 1mardivdm.usmc.mil-CA
 enrollment url http://10.16.145.3:80
 fqdn DIV-155-N-RTR.1mardivdm.usmc.mil
 subject-name CN=DIV-155-N-RTR.1mardivdm.usmc.mil
 vrf bc
 revocation-check none
 rsakeypair IKEV2-DMVPN
!
crypto pki trustpoint 1mardivdm.usmc.mil-CA-ENTERPRISE
 enrollment terminal pem
 fqdn DIV-155-N-RTR.1mardivdm.usmc.mil
 fingerprint 585A0AB86CAE19B35DFB70F237F2C66011056701
 subject-name CN=DIV-155-N-RTR.1mardivdm.usmc.mil
 subject-alt-name DIV-155-N-RTR.1mardivdm.usmc.mil
 revocation-check none
 rsakeypair IKEV2-DMVPN
!
username dnocadmin privilege 15 secret 5 $1$3rmn$ulWkDfy8FpxUd7k1LA14x1
!
vrf definition bc
 !
 address-family ipv4
 exit-address-family
!
vrf definition linkway
 !
 address-family ipv4
 exit-address-family
!
vrf definition mcen
 !
 address-family ipv4
 exit-address-family
!
crypto ikev2 proposal DMVPN-CERT-PROPOSAL 
 encryption aes-gcm-256 aes-gcm-128
 prf sha512
 group 20
!
crypto ikev2 policy DMVPN-CERT-POLICY 
 match fvrf any
 proposal DMVPN-CERT-PROPOSAL
!
!
crypto ikev2 profile DMVPN-CERT-PROFILE
 match fvrf bc
 match identity remote fqdn domain 1mardivdm.usmc.mil
 identity local fqdn DIV-155-N-RTR.1mardivdm.usmc.mil
 authentication local rsa-sig
 authentication remote rsa-sig
 pki trustpoint 1mardivdm.usmc.mil-CA
 pki trustpoint 1mardivdm.usmc.mil-CA-ENTERPRISE
!
crypto ikev2 diagnose error 100
crypto ikev2 certificate-cache 100
!
!
crypto ipsec transform-set ESP-AES256 esp-aes 256 esp-sha512-hmac 
 mode transport
!
crypto ipsec profile DMVPN-CERT-IPSEC-PROFILE-IKEV2
 set transform-set ESP-AES256 
 set ikev2-profile DMVPN-CERT-PROFILE
!
!
ip dhcp pool TACTICAL_USERS
 network 137.232.155.0 255.255.255.128
 domain-name 1mardivdm.usmc.mil
 dns-server 137.232.155.194 137.232.155.195 137.232.58.98
 default-router 137.232.155.1
 option 150 ip 137.232.58.104


ip dhcp pool TACTICAL_VOICE
 network 137.232.155.128 255.255.255.224
 domain-name 1mardivdm.usmc.mil
 dns-server 137.232.155.194 137.232.155.195 137.232.58.98
 default-router 137.232.155.129
 option 150 ip 137.232.58.104

ip dhcp pool TACTICAL_ADMINS
 network 137.232.155.216 255.255.255.248
 domain-name 1mardivdm.usmc.mil
 dns-server 137.232.155.194 137.232.155.195 137.232.58.98
 default-router 137.232.155.217
 option 150 ip 137.232.58.104

!
ip dhcp pool MCEN
 vrf mcen
!!!!Contact G6 to Request MCEN Subnet!!!!
 dns-server 158.238.240.249 158.238.240.248 
 domain-name pndl.mcdsus.mcds.usmc.mil
 option 150 ip 158.238.202.18 
!

ip multicast-routing
ip multicast-routing vrf bc
!
interface Loopback250
 description *MANAGEMENT*
 ip address 137.232.155.250 255.255.255.255
!
interface Loopback10
 description *NIPR-DMVPN-Tunnel-Source*
 vrf forwarding bc
 ip address 10.30.155.255 255.255.255.255
!
interface Po155
 description ***MGMT***
!
!
interface Po155.101
 bandwidth 2048
 description ***CONNECTION TO VSAT***
 vrf for linkway
 ip pim sparse-mode
 ip add 10.101.155.2 255.255.255.252
 service-policy output BLACK-POLICY-LINKWAY-EGRESS-SHAPING
 no shutdown
!
interface Po155.175
 description ***SIPR Taclane CT***
 vrf for bc
 ip pim sparse-mode
 ip add 10.101.155.253 255.255.255.252
 no shutdown
!
!
no interface Tunnel1300
interface Tunnel1300
 description *DNOC-TAC-NIPR-CERT-DMVPN*
 bandwidth 2048
 ip address 10.10.30.155 255.255.255.0
 no ip redirects
 ip pim sparse-mode
 ip mtu 1420
 ip nhrp authentication 1300
 ip nhrp network-id 1300
 ip nhrp nhs dynamic nbma 10.16.48.10 multicast
 ip nhrp nhs dynamic nbma 10.20.5.10 multicast
 ip tcp adjust-mss 1380
 delay 700
 qos pre-classify
 bfd interval 1000 min_rx 1000 multiplier 3
 tunnel source Loopback10
 tunnel mode gre multipoint
 tunnel key 1300
 tunnel vrf bc
 tunnel protection ipsec profile DMVPN-CERT-IPSEC-PROFILE-IKEV2 shared
!
no interface Tunnel13000
interface Tunnel13000
 description *DNOC-MCEN-NIPR-CERT-DMVPN*
 bandwidth 2048
 vrf forwarding mcen
 ip address 10.10.30.155 255.255.255.0
 no ip redirects
 ip mtu 1420
 ip pim sparse-mode
 ip nhrp authentication 13000
 ip nhrp network-id 13000
 ip nhrp nhs dynamic nbma 10.16.48.10 multicast
 ip nhrp nhs dynamic nbma 10.20.5.10 multicast
 ip tcp adjust-mss 1380
 delay 700
 qos pre-classify
 bfd interval 1000 min_rx 1000 multiplier 3
 tunnel source Loopback10
 tunnel mode gre multipoint
 tunnel key 13000
 tunnel vrf bc
 tunnel protection ipsec profile DMVPN-CERT-IPSEC-PROFILE-IKEV2 shared
!
!
no interface Tunnel130
interface Tunnel130
 description *DNOC-TDMA-LINKWAY-DMVPN*
 bandwidth 2048
 vrf forwarding bc
 ip address 10.10.30.155 255.255.255.0
 no ip redirects
 ip mtu 1460
 ip nhrp network-id 130
 ip nhrp shortcut
 ip tcp adjust-mss 1420
 ip nhrp nhs dynamic nbma 10.101.58.25 multicast 
 ip nhrp nhs dynamic nbma 10.101.60.25  multicast 
 delay 700
 qos pre-classify
 bfd interval 500 min_rx 500 multiplier 3
 tunnel source Po155.101
 tunnel mode gre multipoint
 tunnel key 130
 tunnel vrf linkway
 ip pim sparse-mode
!
no interface Tunnel131 
interface Tunnel131 
 description *DIV-MAIN-TDMA-LINKWAY-DMVPN*
 bandwidth 2048
 vrf forwarding bc
 ip address 10.10.30.155 255.255.255.0
 no ip redirects
 ip mtu 1460
 ip nhrp network-id 131
 ip nhrp shortcut
 ip tcp adjust-mss 1420
 ip nhrp nhs dynamic nbma 10.101.57.25 multicast 
 delay 700
 qos pre-classify
 bfd interval 500 min_rx 500 multiplier 3
 tunnel source Po155.131
 tunnel mode gre multipoint
 tunnel key 131
 tunnel vrf linkway
 ip pim sparse-mode
!
interface GigabitEthernet2/0
 ip address 137.232.155.255 255.255.255.254
 description **BACKPLANE INTERFACE TO ES3 MODULE*
 service-policy input ENCLAVE-POLICY-INGRESS-MARKING
 no shutdown
!
interface Po155.30155
 description ***MANAGEMENT***
 encapsulation dot1q 30155
 ip address 10.30.155.11 255.255.255.0
 ip pim sparse-mode
!
router rip
 !
 address-family ipv4 vrf linkway
  network 10.0.0.0
  no auto-summary
  version 2
 exit-address-family
!
router eigrp nipr
 !
 address-family ipv4 unicast autonomous-system 5969
  !
network 0.0.0.0
  af-interface default
   bfd
   passive-interface
  exit-af-interface
  !
  af-interface Po155.155
   no passive-interface
  exit-af-interface
  !
  af-interface Tunnel1300
   no passive-interface
  exit-af-interface
!
 address-family ipv4 unicast vrf mcen autonomous-system 5969
  !
  af-interface default
   bfd
   passive-interface
  exit-af-interface

  !
  af-interface Tunnel13000
   no passive-interface
  exit-af-interface
  !
  af-interface Tunnel13001
   no passive-interface
  exit-af-interface
  !
  !
  topology base
  network 0.0.0.0
!
router eigrp bc

address-family ipv4 unicast vrf bc autonomous-system 65130
 network 10.0.0.0
 af-interface default 
  bfd
  passive-interface 
 af-interface Tunnel130
  no passive-interface
 af-interface Tunnel131 
  no passive-interface

ip tacacs source-interface GigabitEthernet2/0
!
no service config 
no service tcp-small-servers 
no service udp-small-servers 
no service call-home 
no service pad 
service tcp-keepalives-in 
service tcp-keepalives-out 
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption 
!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!NIPR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
!
ip access-list extended STREAMING
 permit ip host <STREAMING SOURCE IP> any
remark add new entry for each video feed (GBS FEED)
!
ip access-list extended VOIP-SECURE-SIGNALING-PROTOCOL-ACL
remark MATCHES STANDARD VOIP SECURE SIGNALING PROTOCOLS WHICH NBAR CANNOT YET IDENTIFY
remark Secure SCCP (Skinny Client Control Protocol)
permit tcp any any eq 2443
permit tcp any any eq 2445
remark Secure SIP (Session Initiation Protocol)
permit tcp any any eq 5061
permit udp any any eq 5061
remark CAPF (Certificate Authority Proxy Function)
permit tcp any any eq 3804
!
class-map match-any VOICE-QUEUE
description VOICE
match dscp CS4 41 43 45 47 49 EF
class-map match-any VOICE-MARKING
description MARK VOICE ON INGRESS
match protocol rtp audio
class-map match-any SIG-QUEUE
description SIGNALING
match dscp CS6 CS5
class-map match-any SIG-MARKING
description MARK-SIGNALING ON INGRESS
match protocol sip
match protocol skinny
match protocol h323
match protocol rtcp
match protocol cisco-phone
match protocol mgcp
match protocol ipsec
match access-group name VOIP-SECURE-SIGNALING-PROTOCOL-ACL
class-map match-any VTC-QUEUE
description ASSURED, NONASSURED MEDIA CONF
match dscp 33 35 37 39 51
match dscp af32 af33 af41 af42 af43
class-map match-any VTC-MARKING
description MARK VTC ON INGRESS
match protocol rtp video
class-map match-any STREAM-QUEUE
description STREAMING, BROADCAST VIDEO
match dscp CS3 25 27 29 31 AF31
class-map match-any STREAM-MARKING
description MARK STREAMING VIDEO
match access-group name STREAMING
!
class-map match-any MSNDATA-QUEUE
description LOW LATENCY & HIGH THROUGHPUT MISSION IMPORTANT DATA
match dscp 17 19 21 23 af21 af22 af23
match dscp 9 11 13 15 af11 af12 af13
match access-group name C2-SYSTEMS
class-map match-any MSNDATA-MARKING-LOW-LATENCY
match protocol http host "*(.mil|.gov|.edu)"
class-map match-any MSNDATA-MARKING-HIGH-THRPT
match protocol smtp
match protocol exchange
class-map match-any OA&M-QUEUE
description OA&M
match protocol snmp
match protocol netflow
match protocol ntp
match protocol syslog
match protocol tacacs
match dscp cs2
class-map match-any SCAV-QUEUE
description SCAVENGER
match dscp cs1
class-map match-any SCAV-MARKING
match protocol aol-messenger
match protocol bittorrent
match protocol blizwow
match protocol directconnect
match protocol edonkey
match protocol fasttrack
match protocol gnutella
match protocol kazaa2
match protocol Konspire2b
match protocol skype
match protocol winmx
match protocol yahoo-messenger
match protocol youtube
match protocol http host "*(aol|apple.|audible|audio|game|hulu|mail|movie|mp3|music|netflix|pandora)*"
match protocol http host "*(radio|teaser|torrent|trailer|tube|tunein|video|yahoo)*"
match protocol http url "*(aol|audible|audio|game|itunes|mail|movie|mp3|music|radio|torrent|trailer)*"
!
!
policy-map ENCLAVE-POLICY-INGRESS-MARKING
class VOICE-QUEUE
class SIG-QUEUE
class VTC-QUEUE
class STREAM-QUEUE
class MSNDATA-QUEUE
class OA&M-QUEUE
set dscp cs2
class SCAV-QUEUE
class VOICE-MARKING
set dscp 49
class SIG-MARKING
set dscp CS5
class VTC-MARKING
set dscp 38
class STREAM-MARKING
set dscp 26
class MSNDATA-MARKING-LOW-LATENCY
set dscp AF21
class MSNDATA-MARKING-HIGH-THRPT
set dscp AF11
class SCAV-MARKING
set dscp CS1
class class-default
set dscp 0
!
snmp-server group solarwinds v3 priv
snmp-server user solarwinds solarwinds v3 auth sha $0!arW!nd$ priv aes 256 $0!arW!nd$
!
!
!
archive
 log config
 hidekeys
 logging enable
!
logging on
logging 137.232.58.107
logging trap informational
logging console notifications
logging source-interface Tunnel1300
!
banner login ^
You are accessing a U.S. Government (USG) Information System (IS) that is
provided for USG-authorized use only. By using this IS (which includes any
device attached to this IS), you consent to the
following conditions:
-The USG routinely intercepts and monitors communications on this IS for
purposes including, but not limited to, penetration testing, COMSEC monitoring,
network operations and defense, personnel misconduct (PM), law enforcement
(LE), and counterintelligence (CI) investigations.
-At any time, the USG may inspect and seize data stored on this IS.
-Communications using, or data stored on, this IS are not private, are subject to
routine monitoring, interception, and search, and may be disclosed or used for
any USG-authorized purpose.
-This IS includes security measures (e.g., authentication and access controls) to
protect USG interests--not for your personal benefit or privacy.
-Notwithstanding the above, using this IS does not constitute consent to PM, LE
or CI investigative searching or monitoring of the content of privileged
communications, or work product, related to personal representation or services
by attorneys,
psychotherapists, or clergy, and their assistants. Such communications and work
product are private and confidential. See User Agreement for details.
^
!
ip domain-name 1mardivdm.usmc.mil
no ip domain-lookup 
!
ip ssh ver 2
!
enable secret 5 $1$DBUH$Ppxxv23xzyfN5ZicFR/zq.
!
aaa new-model
aaa authentication login default group tacacs+ local
aaa authentication enable default group tacacs+ enable
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 0 default start-stop group tacacs+
aaa accounting commands 15 default start-stop group tacacs+
aaa session-id common
!
tacacs server DNOC
 address ipv4 137.232.58.111
 key 7 05290A1A24684708140A19165A55507B6A6C6C72
!
!
crypto pki trustpoint CA2
 enrollment terminal
 revocation-check none
 rsakeypair ssh-rsa
 authorization username alt-subjectname userprinciplename 
!
crypto pki trustpoint CA3
 enrollment terminal
 revocation-check none
 rsakeypair ssh-rsa
 authorization username alt-subjectname userprinciplename 
!

crypto pki certificate chain CA2
 certificate ca 05
  30820370 30820258 A0030201 02020105 300D0609 2A864886 F70D0101 05050030 
  5B310B30 09060355 04061302 55533118 30160603 55040A13 0F552E53 2E20476F 
  7665726E 6D656E74 310C300A 06035504 0B130344 6F44310C 300A0603 55040B13 
  03504B49 31163014 06035504 03130D44 6F442052 6F6F7420 43412032 301E170D 
  30343132 31333135 30303130 5A170D32 39313230 35313530 3031305A 305B310B 
  30090603 55040613 02555331 18301606 0355040A 130F552E 532E2047 6F766572 
  6E6D656E 74310C30 0A060355 040B1303 446F4431 0C300A06 0355040B 1303504B 
  49311630 14060355 0403130D 446F4420 526F6F74 20434120 32308201 22300D06 
  092A8648 86F70D01 01010500 0382010F 00308201 0A028201 0100C02C C1F68D3B 
  ACFF3F3C D671BEB8 742207EC 704115FC AB40E307 AAC1C3D8 9FFEDA4C 3ABF3FC8 
  D8287B4B 3601C0AC 4525C3D2 0E0A8F85 1864103D 1A13702A 6F8ED7DC 8D93B341 
  0F3821CD ADABC23D 2A05D357 11370DCD 8C51F993 E3CC4649 218E14B4 CDCB143E 
  38CD7231 EEAB12F2 65EA342E 565DFFEE 6375CB6D BA9134FC 9EF3F42D 1CBE50C4 
  42DF5988 FF6AB3FA A86C3DCB 56717105 96BB9F80 E5804559 6741B0EB C3AD60A4 
  80750617 9C0EF443 E0990E1B FB7FF5B3 CCB28182 B1FD32C1 B8BE41A4 64B5603A 
  5A51308C CEDE412C 19475C49 1064B974 A98741AF 7D6EBAC1 B8A1BF65 313A0467 
  F9B5BB8E 928A0063 B8B1E68C 385F83FF 50D53BA2 5D6BB210 CC630203 010001A3 
  3F303D30 1D060355 1D0E0416 04144974 BB0C5EBA 7AFE0254 EF7BA0C6 95C60980 
  7096300B 0603551D 0F040403 02018630 0F060355 1D130101 FF040530 030101FF 
  300D0609 2A864886 F70D0101 05050003 82010100 98918D3F 89C8BBF5 C0697329 
  3B35ACBA B308763D 700992E9 84442101 7D14761B EE516C1D 8D15372D 7B3169F4 
  9A44B8AF 46CC34FA 23CB0327 19D28321 752BE7E0 1B9926DC 844095E8 A8D2CCF6 
  585C66EF 3F4A9710 821DBA0A A2DD5B06 2B9DA764 4EEB2E01 35A4B43F 13AD55E4 
  D573A869 9B11F198 F2311E6F 40D4F878 9F8E91A0 6F700490 66AA062B CEE17A92 
  B57DE1E0 D196E7A1 3A2DCCB1 9D1F0544 ED8799D3 4D1A7039 C1040CE5 7ED9F1AF 
  D7200EF1 227A25A4 7399CC3F A4072796 A8A295ED 82B916D3 9E0B87C2 C1F288F5 
  62DF68DF C7BC6951 EDB15CDC 5454290F 09399AAC 03C1DB0C 4DAE6F0A 7A1649F1 
  BF91D238 94D3F695 2CB76CC9 42B68DCA 908D85D9
        quit
crypto pki certificate chain CA3
 certificate ca 01
  30820373 3082025B A0030201 02020101 300D0609 2A864886 F70D0101 0B050030 
  5B310B30 09060355 04061302 55533118 30160603 55040A13 0F552E53 2E20476F 
  7665726E 6D656E74 310C300A 06035504 0B130344 6F44310C 300A0603 55040B13 
  03504B49 31163014 06035504 03130D44 6F442052 6F6F7420 43412033 301E170D 
  31323033 32303138 34363431 5A170D32 39313233 30313834 3634315A 305B310B 
  30090603 55040613 02555331 18301606 0355040A 130F552E 532E2047 6F766572 
  6E6D656E 74310C30 0A060355 040B1303 446F4431 0C300A06 0355040B 1303504B 
  49311630 14060355 0403130D 446F4420 526F6F74 20434120 33308201 22300D06 
  092A8648 86F70D01 01010500 0382010F 00308201 0A028201 0100A9EC 14728AE8 
  4B70A3DA 100384A6 FBA7360D 2A3A5216 BF301552 86054720 CFAAA6CD 75C4646E 
  EFF16023 CB0A6640 AEB4C868 2A005168 4937E959 324D95BC 4327E940 8D3A10CE 
  14BC4318 A1F9DECC E7857673 5E181A23 5BBD3F1F F2ED8D19 CC03D140 A48FA720 
  024C275A 7936F6A3 37218E00 5A0616CA D355966F 3129BB72 0ECBE248 51F2D437 
  A435D66F EE17B3B1 06AB0B19 86E8236D 311B2878 65C5DE62 52BCC17D EBEEA05D 
  5404FBB2 CB2BB223 5491824C F0BFBA74 403B0C04 4580675C C5EBA257 C31A7F0A 
  2DBD7FB9 DCC199B0 C807E40C 8636943A 252FF27D E6973C1B 94B49759 06C93AE4 
  0BD9EAE9 FC3B7334 6FFDE798 E4F3A1C2 905F1CF5 3F2ED719 D37F0203 010001A3 
  42304030 1D060355 1D0E0416 04146C8A 94A277B1 80721D81 7A16AAF2 DCCE66EE 
  45C0300E 0603551D 0F0101FF 04040302 0186300F 0603551D 130101FF 04053003 
  0101FF30 0D06092A 864886F7 0D01010B 05000382 0101009F 71A4C0B6 96D28043 
  A048E91F 7604F9C5 3CAD6618 58639BC3 B6E8688A 855A4266 12B4D2E6 8B887F87 
  F498F5A8 C609C91F F02C1FEC 82B8F4A5 4738C133 2BDF4C7E 9ABE0B0B B1CB0F7C 
  502810CF 8A8DA2E9 BAAC86D7 D4B1935F 228F9605 B44E0C75 917DD3F2 E794C294 
  14764F8F 0CAB1087 58328507 7586120B 5EEA53B4 0AC84C84 921FEBE8 41863CBA 
  F44E414A D16C5847 41C3865A F2EEE9F2 982782EA 2E36D6F8 065E82F1 A0529344 
  09BAD2A9 195A58A3 A85D206D 4F64F830 871B9013 4881CDCA 90C70DC1 D4983F8E 
  F20E5768 33128E99 09B1F0E4 F610F436 F249BDEA A338C856 4123839A DFA11B35 
  7CEB3F41 B3F56F4B 3A5EAE6F 937698D2 F1999D45 C48E72
        quit
!
!
no ftp-server enable 
no ip bootp server 
no ip source-route 
no ip gratuitous-arps 
no ip domain-lookup 
no ip finger 
no ip http server 
ip cef 
ip tcp synwait-time 10 
ip ssh time-out 60 
ip ssh authentication-retries 3 
ip ssh rsa keypair-name ssh-rsa
ip ssh version 2
ip ssh server certificate profile
 user
  trustpoint verify CA2
  trustpoint verify CA3
ip ssh server algorithm hostkey ssh-rsa
ip ssh server algorithm authentication publickey password
ip ssh server algorithm publickey x509v3-ssh-rsa
!
line con 0
 exec-timeout 5 0
 privilege level 15
 logging synchronous
!
line vty 0 15 
 exec-timeout 5 0
 privilege level 15
 logging synchronous
 transport input ssh
 transport output ssh
!
line 131
 no activation-character
 no exec
 transport preferred none
 transport input all
 transport output all
 stopbits 1


********************************************************************
********************************************************************
********************************************************************



 
DNOC POP ROUTER CA Request Process
STEP 1: Type: crypto pki authenticate 1mardivdm.usmc.mil-CA
STEP 2: Follow prompts to accept fingerprint
STEP 3: Type: crypto pki enroll 1mardivdm.usmc.mil-CA
STEP 4: Follow prompts (say no to serial number and IP address) yes to accept cert



Microsoft CA  Request Process 
STEP 1: Type: crypto pki authenticate 1mardivdm.usmc.mil-CA-ENTERPRISE
STEP 2: Paste Root CA certificate from Microsoft Root CA
STEP 3: Type: crypto pki enroll 1mardivdm.usmc.mil-CA-ENTERPRISE
STEP 4: Get cert on the terminal signed by the microsoft CA (https://crl/certsrv/)
STEP 5: Type: crypto pki import 1mardivdm.usmc.mil-CA-ENTERPRISE certificate
STEP 6: Paste the newly signed cert from the CA 