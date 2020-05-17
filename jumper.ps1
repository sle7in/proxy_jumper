
While ($i -lt 9999) {
    # "10 * $i = " + (10 * $i)

    C:\'Program Files (x86)'\NordVPN\NordVPN.exe -c -g "United States"
    for($i=0; $i-le $server_list.length-1; $i++) {
        Write-Host $server_list[$i]
    }
    For ($i=0; $i -le 10; $i++) {
        ./bencode.py $server_list[$i]
    }
    C:\'Program Files (x86)'\NordVPN\NordVPN.exe -d
    #nordvpn --connect  --server-name <name>
    #C:\Users\LonelyMerc\source\repos/proxy_jumper/proxy.py
    #nordvpn --disconnect
    $i++
    }
    
    
# import config

# C:\'Program Files (x86)'\NordVPN\NordVPN.exe -c -g "United States"
# $server_list = {"one","two"}
# nordvpn --groups

# # For ($i=0; $i -le 10; $i++) {
# #For ($i=0; $i -$server_list.length; $i++) {
# While (True) {
#     # $server_list[$i]
#     # "10 * $i = " + (10 * $i)
#     C:\'Program Files (x86)'\NordVPN\NordVPN.exe -c -g "United States"
#     ping www.google.com
#     C:\'Program Files (x86)'\NordVPN\NordVPN.exe -d
#     #nordvpn --connect  --server-name <name>
#     #C:\Users\LonelyMerc\source\repos/proxy_jumper/proxy.py
#     #nordvpn --disconnect
#     }

# #nordvpn --connect  --server-name <name>
# #python C:\Users\LonelyMerc\source\repos/proxy_jumper/proxy.py
# #nordvpn --disconnect

# Write-Host "Script Finished Successfully"