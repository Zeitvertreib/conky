doppelstunden = {
        1 : ["07:30", "09:00"],
        2 : ["09:20", "10:50"],
        3 : ["11:10", "12:40"],
        4 : ["13:00", "14:30"],
        5 : ["14:50", "16:20"],
        6 : ["16:40", "18:10"],
        7 : ["18:30", "20:00"],
        }

Montag = {
        2 : [ "TiLogic", "ABS E023" ],
        3 : [ "SWT", "HSZ 02" ],
        4 : [ "IuK - U" , "APB E008"]}
Dienstag =  {
        1 : [ "U - RN" , "SCHA A185"],
        2 : [ "IuK", "HSZ 02"],
        3 : [ "DB", "HSZ 03"]}
Mittwoch = {
        1 : [ "U - SWT", "ASB E010"]}
Donnerstag = {
        3 : [ "RN", "HSZ 03"],
        4 : [ "ECG", "HSZ 02"],
        5 : [ "U - ECG", "AVO"]}
Freitag = {
        2 : [ "Prog", "HSZ 03"],
        3 : [ "MA II", "HSZ 03"],
        4 : [ "U - DB", "WIL C206"]}
Wochenede = {}
woche = [ Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Wochenede ]

#  selection_start = "${if_match $template1==" + timeX + "} "
#  selection_container_stop = "$color1${endif} $alignr - - - $color"
#  selection_typeP_stop = "$color1${endif} $template2 $color"
#  selection_typeT_stop = "$color1${endif} $alignr " + timeslot + " |$color"

#  defaultlines = {
#  $color1${endif} $alignr - - - $color
   #  $color1${endif} $alignr 7:30 - 09:00 | 1.DS |$color
#  $color1${endif} $template2 $color
   #  $color1${endif} $alignr 9:20 - 10:50 | 2.DS |$color
#  $color1${endif} $template2 $color
   #  $color1${endif} $alignr 11:10 - 12:40 | 3.DS |$color
#  $color1${endif} $template2 $color
   #  $color1${endif} $alignr 13:00 - 14:30 | 4.DS |$color
#  $color1${endif} $template2 $color
   #  $color1${endif} $alignr 14:50 - 16:20 | 5.DS |$color
#  $color1${endif} $template2 $color
   #  $color1${endif} $alignr 16:40 - 18:10 | 6.DS |$color
#  $color1${endif} $template2 $color
   #  $color1${endif} $alignr 18:30 - 20:00 | 7.DS |$color
#  $color1${endif} $alignr - - - $color

#  ${if_match $template1=="pause"}
#  ${if_match $template1=="1.DS"}
#  ${if_match $template1=="pause1"}
#  ${if_match $template1=="2.DS"}
#  ${if_match $template1=="pause2"}
#  ${if_match $template1=="3.DS"}
#  ${if_match $template1=="pause3"}
#  ${if_match $template1=="4.DS"}
#  ${if_match $template1=="pause4"}
#  ${if_match $template1=="5.DS"}
#  ${if_match $template1=="pause5"}
#  ${if_match $template1=="6.DS"}
#  ${if_match $template1=="pause6"}
#  ${if_match $template1=="7.DS"}
#  ${if_match $template1=="pause8"}
