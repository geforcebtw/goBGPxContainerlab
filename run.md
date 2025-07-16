## **Order to start services**

1 - Run the lab (clab_up xxx.yml)
    1.1 - Starting debug (docker logs -f xxx)

2 - goBGP daemon configuration (docker exec -it gobgp bash)
    2.2 - adding eth1 address (ip address add dev eth1 192.168.22.2/24)
    2.3 - goBGP daemon starting (gobgpd -t yaml -f /gobgp/gobgp.yml) ==> Don't shut the daemon during the operations

3 - goBGP use (docker exec -it gobgp bash) ==> In new window

4 - Peering BGP checking + release gobgp (gobgp neighbor 192.168.22.2)

5 - RIB checking (gobgp global rib -a 'family')

6 - Exporting RIB to json format (gobgp global rib -a 'family' -j > gobgp/xxx.json) # Importante to put the file in the gobgp container folder cause of binding with MUZTC637

7 - Json script execution on MUZTC637 (python3 extract.py) # Think to rename the json file in the script
