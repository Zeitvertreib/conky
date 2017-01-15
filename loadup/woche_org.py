#  import stunden.doppelstunden as doppelstunden
# does the conky stuff
from stunden import doppelstunden
from stunden import woche


def con_to_string(ss):
    sss=""
    for s in ss:
        sss=sss+s
    return sss

def stunden_field(stunde, wochentag):
    width = 10
    #  freistunde = ["${voffset +10}"+"-+-".center(width),"${voffset -10}"+".".center(width)]
    freistunde = ["- -  ".rjust(width), " ".rjust(width)]
    fillstring = wochentag.get(stunde, freistunde)
    #  print("fillstring "+str(fillstring))

    for i, x in enumerate(fillstring):
        #  fillstring[i]=x.rjust(width)
        if x.__len__() < (width-1):
            x = x+" |"
            x = x.rjust(width)
            #  #  print("len "+x)
            fillstring[i]=x
        if x.__len__() < (width):
            x = x+"|"
            x = x.rjust(width)
            #  #  print("len "+x)
            fillstring[i]=x

    #  print(fillstring+[str(fillstring[0].__len__())+" "+str(fillstring[1].__len__())])
    return fillstring


def build_it(doppelstunden):
    count = 0
    #  selection_typeP_stop = "$template2 $color"
    selection_typeP_stop = ""
    greatbreak_a = "$color${if_match $template1==\"pause\"} $color1${endif}" + selection_typeP_stop

    res = [greatbreak_a]
    for stunde in doppelstunden:
        #  controller, not content type
        select_hour = "${if_match $template1==\"" + str(stunde) + ".DS\"}$color1${endif}"
        #  select_break = "${if_match $template1==\"pause" + str(stunde) + "\"}${color1}__${endif}"
        pausenzeile = ["${voffset -10}${if_match $template1==\"pause" + str(stunde) + "\"}${color1}_-------------------_${endif}$color "]
        #  leerzeilen = ["${goto 170} "]
        leerzeilen = [" ".rjust(22)]
        rest_d_woche = []
        for i, wochentag in enumerate(woche):
            j = i+1
            tagesmarkierung = "$color"+"${if_match $template3==\""+str(j)+"\"}$color3"+select_hour+"${endif}"
            #  pausenmarkierung = "$color${if_match $template3==\""+str(j)+"\"}$color3"+select_break+"${endif}"

            ss = stunden_field(stunde, wochentag)
            rest_d_woche.append(tagesmarkierung+ss[0])
            leerzeilen.append(tagesmarkierung+ss[1])

            #  pausenzeile.append(pausenmarkierung)

        count+=1
        resolution = doppelstunden[stunde][0]+" - "+doppelstunden[stunde][1]+" | "+str(stunde)+".DS"
        selection_typeT_stop = "" + resolution + " |$color"

        selection_hour = "$color" + select_hour + selection_typeT_stop + con_to_string(rest_d_woche)
        selection_rooms = "$color" + select_hour + con_to_string(leerzeilen)
        #  selection_break = "${if_match $template1==\"pause" + str(stunde) + "\"} " + selection_typeP_stop
        res.append(selection_hour)
        res.append(selection_rooms)
        res.append(con_to_string(pausenzeile))
    #  res.append(greatbreak_a)
    #  container_end = "${if_match $template1==\"pause"+str(count)+"\"} " + selection_typeP_stop
    #  res.append(container_end)
    return res

def get_hours():
    return f


if __name__ == '__main__':
    X = build_it(doppelstunden)
    sl=""
    for x in X:
        sl=sl+x+'\\n'
    print(sl)
