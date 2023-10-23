#!/bin/bash
VPNNAME="CREARE-OCI"
BASEDIR=$(dirname "$0")
echo "Configurando VPN..."
echo
USERNAME="guilherme.brida"
PASSWORD="Gg*9695948586"
echo && echo
nmcli connection delete $VPNNAME &> /dev/null
nmcli connection import type openvpn file $BASEDIR/$VPNNAME.ovpn
nmcli connection modify $VPNNAME ipv4.never-default true
nmcli connection modify $VPNNAME ipv6.never-default true
nmcli connection modify $VPNNAME vpn.user-name $USERNAME
TEMPFILE=$(mktemp)
chmod 600 $TEMPFILE
echo "vpn.secrets.password:$PASSWORD" > $TEMPFILE
nmcli connection up id $VPNNAME passwd-file $TEMPFILE
rm -f $TEMPFILE
