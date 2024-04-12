$choice = Get-Content -Path "choice.txt"

if ($choice -eq "1") {
    Get-ChildItem -Path (Get-Content -Path "source.txt")
} 

elseif ($choice -eq "2") {
    New-Item -ItemType Directory -Path (Get-Content -Path "source.txt")
} 

elseif ($choice -eq "3") {
    Remove-Item -Path (Get-Content -Path "source.txt")
} 

elseif ($choice -eq "4") {
    $source = Get-Content -Path "source.txt"
    $newName = Read-Host "Enter the new name for $source"
    Rename-Item -Path $source -NewName $newName
} 

elseif ($choice -eq "5") {
    Copy-Item -Path (Get-Content -Path "source.txt") -Destination (Get-Content -Path "destination.txt")
} 

elseif ($choice -eq "6") {
    Move-Item -Path (Get-Content -Path "source.txt") -Destination (Get-Content -Path "destination.txt")
} 

elseif ($choice -eq "7") {
    Set-Location -Path (Get-Content -Path "source.txt")
}

elseif ($choice -eq "8") {
    exit
}

else {
    Write-Host "Invalid choice"
}
