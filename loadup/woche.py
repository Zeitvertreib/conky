#  import stunden.doppelstunden as doppelstunden
# does the conky stuff
import helper as h
from collections import OrderedDict
from pprint import pprint

ww=h.woche_to_dict()
wflat=h.woche_global
doppelstunden=h.doppelstunden
#  print(doppelstunden)
#  print(ww)

def gather_all(all_arr):
    week=ww
    for fach in all_arr:
        #  print(fach["meta"]["fach"])
        fach_bez=fach["meta"]["fach"]
        #  fach_bez="fach not found"
        #  fach_bez=fach["meta"].get(fach, "fach not found")
        for day in ww:
            fach_day_selected = fach.get(day, False)
            #  week[day]=h.append_by_number_dict(week.get(day, {day:{}}), fach_day_selected, fach_bez)
            if fach_day_selected:
                h.append_by_number_dict(week.get(day), fach_day_selected, fach_bez)
    #  pprint(week)


def stunden_field(stunde, wochentag, woche):
    #  print(str(stunde))
    #  print(str(wochentag))
    width = 10
    #  freistunde = ["${voffset +10}"+"-+-".center(width),"${voffset -10}"+".".center(width)]
    freistunde = ["- -  ".rjust(width), " ".rjust(width)]
    #  fillstring = wochentag.get(stunde, freistunde)
    #  print(woche)
    fillstring=freistunde
    if woche.get(wochentag, None):
        fillstring=woche[wochentag].get(str(stunde), freistunde)
        if fillstring!=freistunde:
            fs=[]
            for x in fillstring:
                #  cuts off the weekly
                x=x[:width]
                for special in ["U", "V"]:
                    if x.startswith(special):
                        x=x.split()
                        if x[0]=="V":
                            x=">"+x[1]+"<"
                        if x[0]=="U":
                            x=" "+x[1]+" "
                fs.append(x)
                fillstring=fs
            #  fillstring=fillstring[0:width-1]
            if fillstring.__len__()<2:
                fillstring.append(" ".rjust(width))
            #  print(fillstring)

    for i, x in enumerate(fillstring):
        #  fillstring[i]=x.rjust(width)
        #  print("fillstring: "+str(fillstring))
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

#  def fillweek_by_fach(fach, days_a_week=days_a_week, hours_a_day=hours_a_day):
#  def fillweek_by_fach(fach, week_array):
    #  for h in hours_a_day:
        #  for d in days_a_week:
            #  hour=fach.get(h)
            #  if hour:


def build_flexible(faecher, doppelstunden=doppelstunden):
    meta= {'faecher': [] } # processed faecher
    for f in faecher:
        fach=f["meta"].get(fach, "unnamed f")
        meta['faecher'].append(fach)
        applyed_fach=fillweek_by_fach(fach)

def build_it(woche, doppelstunden=doppelstunden):
    # string variables
    stunde=0
    selection_typeP_stop = ""
    greatbreak_a = "$alignr$color${if_match $template1==\"pause\"} $color1${endif}" + selection_typeP_stop
    def select_hour_f(hour=0):
        return "${if_match $template1==\"" + str(hour) + ".DS\"}$color1${endif}"

    def pausenzeile_f(hour=0):
        return ["${voffset -10}${if_match $template1==\"pause" + str(stunde) + "\"}${color1}_-------------------_${endif}$color "]

    def tagesmarkierung_f(tag=0, hour_prebuild="should be prebuild"):
        return "$color${if_match $template3==\""+str(tag)+"\"}$color3"+hour_prebuild+"${endif}"

    #  print(woche.__len__(), woche)

    res = [greatbreak_a]
    for stunde in doppelstunden:
        modi= { 'select_hour':select_hour_f(stunde) }
        #  print("stunde & modi: "+str(stunde)+modi["select_hour"])
        number_of_fields=2
        select_hour = select_hour_f(stunde)
        pausenzeile = pausenzeile_f(stunde)
        leerzeilen = [" ".rjust(22)]
        rest_d_woche = []
        j=0
        #  print(wflat)

        #  catch the unloadable order in ordered dict
        for wochentag in wflat:
            #  wochentag=woche[wochentag]
        #  for wochentag in woche:
            j+=1
            tagesmarkierung = tagesmarkierung_f(j, select_hour)
            #  print("stunde: "+str(stunde))
            #  print("wochentag: "+str(wochentag))
            ss = stunden_field(stunde, wochentag, woche)
            #  print(str(ss)+"<-ss")
            rest_d_woche.append(tagesmarkierung+ss[0])
            leerzeilen.append(tagesmarkierung+ss[1])
        #  print(rest_d_woche)

        resolution = doppelstunden[stunde][0]+" - "+doppelstunden[stunde][1]+" | "+str(stunde)+".DS"
        selection_typeT_stop = "" + resolution + " |$color"

        selection_hour = "$color" + select_hour + selection_typeT_stop + ''.join(rest_d_woche)
        selection_rooms = "$color" + select_hour + ''.join(leerzeilen)
        #  selection_break = "${if_match $template1==\"pause" + str(stunde) + "\"} " + selection_typeP_stop
        res.append('$alignr'+selection_hour)
        res.append('$alignr'+selection_rooms)
        res.append('$alignr'+''.join(pausenzeile))
    #  res.append(greatbreak_a)
    #  res.append(container_end)

    res='\n'.join(res)
    return res

if __name__ == '__main__':
    pass
    #  print(build_it(woche, doppelstunden))
    #  X = build_it(woche, doppelstunden)
    #  sl=""
    #  for x in X:
        #  sl=sl+x+'\\n'
    #  print(sl)
