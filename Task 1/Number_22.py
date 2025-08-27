StartingBalance = 100
ShortTrack = 1.79
MediumTrack = 2.5
longTrack = 4.5
AfterShortTrack = (ShortTrack* 3) 
AfterMediumTrack = (MediumTrack * 4)
AfterLongTrack = (longTrack * 2)
CostAltogether = AfterLongTrack + AfterMediumTrack + AfterShortTrack
FinalBalance = StartingBalance - CostAltogether
print("The New Balance is", FinalBalance)
