#  import stunden.doppelstunden as doppelstunden
from stunden import doppelstunden
from stunden import woche

def con_to_string(ss, voffset="0"):
    sss=""
    offset = 60
    #  o_cal = offset*6
    o_cal = 200
    for s in ss:
        day_seperator = "${goto " +str(o_cal) + "}"
        #  day_seperator = "${goto " +str(o_cal) + "}${voffset "+voffset+"}"

        #  day_seperator = "${goto " +str(o_cal) + "} ${alignr " + str(5) + "}"
        o_cal=o_cal+offset
        sss=sss+day_seperator+s
    sss+= "${goto " +str(o_cal-20) + "}"
    return sss

#  def week(woche):

def build_it(doppelstunden):
    count = 0
    #  selection_typeP_stop = "$template2 $color"
    selection_typeP_stop = ""
    greatbreak_a = "$color${if_match $template1==\"pause\"} $color1${endif}" + selection_typeP_stop
    freistunde = ["-+-", ""]
    res = [greatbreak_a]
    for stunde in doppelstunden:
        select_hour = "${if_match $template1==\"" + str(stunde) + ".DS\"}$color1${endif}"
        select_break = "${if_match $template1==\"pause" + str(stunde) + "\"}${color1}__${endif}"
        select_break_first_column = "${if_match $template1==\"pause" + str(stunde) + "\"}$color1 __  __  __  __${endif}"
        pausenzeile = []
        leerzeilen = []
        rest_d_woche = []
        for i, wochentag in enumerate(woche):
            j = i+1
            tagesmarkierung = "${if_match $template3==\""+str(j)+"\"}$color3"+select_hour+"${endif}"
            pausenmarkierung = "${if_match $template3==\""+str(j)+"\"}$color3"+select_break+"${endif}"

            ss = wochentag.get(stunde, freistunde)
            if ss[0] != freistunde[0]:
                ss[0] = "${offset -11 }"+ss[0]

            if ss[1] != freistunde[1]:
                ss[1] = "${offset -17 }"+ss[1]

            rest_d_woche.append(tagesmarkierung+ss[0]+"$color")
            leerzeilen.append(tagesmarkierung+ss[1]+"$color")
            pausenzeile.append(pausenmarkierung)
        #  print(pausenzeile)

        count+=1
        resolution = doppelstunden[stunde][0]+" - "+doppelstunden[stunde][1]+" | "+str(stunde)+".DS"
        selection_typeT_stop = " ${goto 50} " + resolution + " |$color"

        selection_hour = "$color" + select_hour + selection_typeT_stop + con_to_string(rest_d_woche)
        selection_rooms = "$color" + select_hour + con_to_string(leerzeilen)
        selection_break = "${goto 50}${voffset -13}"+select_break_first_column + " $color"
        #  selection_break = "${if_match $template1==\"pause" + str(stunde) + "\"} " + selection_typeP_stop
        res.append(selection_hour)
        res.append(selection_rooms)
        res.append(selection_break + con_to_string(pausenzeile))
    #  res.append(greatbreak_a)
    #  container_end = "${if_match $template1==\"pause"+str(count)+"\"} " + selection_typeP_stop
    #  res.append(container_end)
    res.append("${color}")
    return res

def get_hours():
    return f


X = build_it(doppelstunden)
sl=""
for x in X:
    sl=sl+x+'\\n'
print(sl)
