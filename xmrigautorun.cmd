sc delete XmrService
sc delete XmrhideService
sc create XmrService binPath= "C:\Program Files\xmrig\xmrigservice.exe" DisplayName= "XmrService" start= auto