
$server_list = ('https://943thex.com/vote-taste-of-fort-collins-local-entertainment-contest/',
        'https://retro1025.com/vote-taste-of-fort-collins-local-entertainment-contest/',
        'https://999thepoint.com/vote-taste-of-fort-collins-local-entertainment-contest/',
        'https://999thepoint.com/vote-taste-of-fort-collins-local-entertainment-contest/',
        'https://power1029noco.com/vote-taste-of-fort-collins-local-entertainment-contest/')

While ($i -lt 9999) {

    C:\'Program Files (x86)'\NordVPN\NordVPN.exe -c -g "United States"
    Start-Sleep -s 3
    for($i=0; $i-le $server_list.length-1; $i++) {
        ./bencode.py $server_list[$i]
    }
    Start-Sleep -s 3
    C:\'Program Files (x86)'\NordVPN\NordVPN.exe -d

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