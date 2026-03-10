Write-Output "=== SYSTEM MEMORY OVERVIEW ==="
$os = Get-CimInstance Win32_OperatingSystem
$total = [math]::Round($os.TotalVisibleMemorySize/1MB,2)
$free = [math]::Round($os.FreePhysicalMemory/1MB,2)
$used = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory)/1MB,2)
$pct = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory)/$os.TotalVisibleMemorySize*100,1)
Write-Output "Total Physical: $total GB"
Write-Output "Used Physical:  $used GB"  
Write-Output "Free Physical:  $free GB"
Write-Output "Percent Used:   $pct%"
Write-Output ""

Write-Output "=== TOP 30 PROCESSES BY WORKING SET ==="
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 30 Name, Id, 
    @{N='WorkingSet_MB';E={[math]::Round($_.WorkingSet64/1MB,1)}},
    @{N='PrivateBytes_MB';E={[math]::Round($_.PrivateMemorySize64/1MB,1)}},
    @{N='VirtualMem_GB';E={[math]::Round($_.VirtualMemorySize64/1GB,2)}} | Format-Table -AutoSize
Write-Output ""

Write-Output "=== PROCESSES GROUPED BY NAME (TOTAL MEMORY) ==="
Get-Process | Group-Object -Property Name | ForEach-Object {
    [PSCustomObject]@{
        Name=$_.Name
        Count=$_.Count
        TotalWorkingSet_MB=[math]::Round(($_.Group | Measure-Object WorkingSet64 -Sum).Sum/1MB,1)
        TotalPrivate_MB=[math]::Round(($_.Group | Measure-Object PrivateMemorySize64 -Sum).Sum/1MB,1)
    }
} | Sort-Object TotalWorkingSet_MB -Descending | Select-Object -First 25 | Format-Table -AutoSize
Write-Output ""

Write-Output "=== COMMITTED MEMORY (WHAT WINDOWS ACTUALLY ALLOCATED) ==="
$cs = Get-CimInstance Win32_PageFileUsage
$perfOS = Get-CimInstance Win32_PerfFormattedData_PerfOS_Memory
Write-Output "Committed Bytes:     $([math]::Round([long]$perfOS.CommittedBytes/1GB,2)) GB"
Write-Output "Commit Limit:        $([math]::Round([long]$perfOS.CommitLimit/1GB,2)) GB"
Write-Output "Available MB:        $($perfOS.AvailableMBytes) MB"
Write-Output "Cache Bytes:         $([math]::Round([long]$perfOS.CacheBytes/1GB,2)) GB"
Write-Output "Pool Paged:          $([math]::Round([long]$perfOS.PoolPagedBytes/1MB,1)) MB"
Write-Output "Pool NonPaged:       $([math]::Round([long]$perfOS.PoolNonpagedBytes/1MB,1)) MB"
Write-Output "Modified Page List:  $([math]::Round([long]$perfOS.ModifiedPageListBytes/1MB,1)) MB"
Write-Output "Standby Cache (Normal+Reserve): $([math]::Round(([long]$perfOS.StandbyCacheNormalPriorityBytes + [long]$perfOS.StandbyCacheReserveBytes)/1GB,2)) GB"
Write-Output ""

Write-Output "=== KERNEL POOL TAGS (DRIVER MEMORY - OFTEN WHERE LEAKS HIDE) ==="
Write-Output "(If NonPaged Pool is abnormally high, a driver is leaking)"
Write-Output ""

Write-Output "=== SERVICES WITH HIGH MEMORY ==="
Get-Process -IncludeUserName -ErrorAction SilentlyContinue | 
    Where-Object { $_.WorkingSet64 -gt 100MB } |
    Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, UserName,
        @{N='WorkingSet_MB';E={[math]::Round($_.WorkingSet64/1MB,1)}},
        @{N='Private_MB';E={[math]::Round($_.PrivateMemorySize64/1MB,1)}} |
    Format-Table -AutoSize
