[Setup]
AppName=Car Rental Manager
AppVersion=1.0
DefaultDirName={pf}\CarRentalManager
OutputDir=Output
OutputBaseFilename=CarRentalManager_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Car Rental Manager"; Filename: "{app}\app.exe"
