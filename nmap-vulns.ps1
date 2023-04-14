# Given a text file containing a list of hosts (<ip>:<port>), one per line
# Scan each one with nmap scripts: vuln, vulners 

Get-Content ips.txt | ForEach-Object {
    $target = $_
    Write-Host "Scanning target: $target"
    nmap -sV -p $target.Split(':')[1] --script vuln,vulners -oA "out-temp" $target.Split(':')[0]
    Get-Content "out-temp.nmap" | Out-File "all.out.txt" -Append
    Remove-Item "out-temp.gnmap" -Force
    Remove-Item "out-temp.nmap" -Force
    Remove-Item "out-temp.xml" -Force
}
