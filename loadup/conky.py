import woche
import os.path
import glob, json
from helper import woche_global as woche_global
from helper import abspeichern as abspeichern
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
speicherziel="rc/generated" # output for final conky_rc
speicherziel=os.path.join(dir_path, speicherziel)
#  rc_mini_raw=speicherziel+"conkyrc_mini_raw"
rc_static_raw=os.path.join(dir_path, "conkyrc_static_raw")
rc_static_finish=os.path.join(dir_path, "rc/generated")
rc_raw="conkyrc_raw"
rc_raw=os.path.join(dir_path, rc_raw)
data="faecher/"
directory=os.path.join(dir_path, data)

def build_bigreplace(ganze_woche, fach, semester, fcollection, semesterkeys):
    pre=woche.build_it(ganze_woche)
    #  pre='\n'.join(pre)
    semesterheading="$alignr$color"
    for sh in semesterkeys:
        if sh == semester:
            sh= "${color3}" + str(sh) + "$color"
        semesterheading=semesterheading+" "+sh

    semesterfach="$alignr$color"
    for sf in fcollection[semester]:
        if sf == fach:
            sf= "${color3}" + str(sf) + "$color"
        semesterfach=semesterfach+" "+sf

    replace1 = [
        ('replace_this1','template1 "${execpi 60 python3 '+str(dir_path)+'/clock.py}"'),
        ('replace_this4', semesterheading),
        ('replace_this5', semesterfach),
        #  'insert_line7','template7 '$HOME/xtern
        ('replace_block', str(pre))]
    return replace1

def build_header(fcollection):
    kk=[]
    for k in fcollection:
        fcollection[k].sort()
        kk.append(k)
    kk.sort()
    return kk


def textblock( textlaufvariable=[] ):
    zeile = []
    def container( t1 ):
        return "$color${if_match $template1==\""+str(t1)+"\"}$color1${endif}"+t1+"  "

    for t1 in textlaufvariable:
        zeile.append( container( t1 ) )

    zeile=''.join(zeile)
    return zeile

def get_stuff(directory=directory, semester="[1-9]", formatted=True):
    """ does not get faecher w digit at end! """
    """ has a bug for vertiefugen, change smester patter accorandly to fix """
    res_arr=[]
    cwd=os.getcwd()
    os.chdir(directory)
    semester=glob.glob(semester+'*[!0-9]')
    #  faecher=glob.glob('*[!0-9].fach')
    semester.sort()
    print(semester)
    print("....................................")
    for ff in semester:
        print("going")
        with open(ff, "r") as fx:
            j=json.load(fx)
            #  if formatted:
                #  j=formatting_conversion(j)
        res_arr.append(j)
        #  res_arr.append(j)
    os.chdir(cwd)
    #  for r in res_arr:
        #  print(r)
    return res_arr

#  arr=get_stuff(directory)
#  arr2=get_stuff(directory, False)
#  woche.gather_all(arr2)

def write_conkyrc(name_savegame, replacements_arr, speicherziel, rc_vorlage=rc_raw):
    oldstring=""
    with open(rc_vorlage, "r") as r:
        oldstring=r.read()
    wx=[]
    content=oldstring
    mapping = replacements_arr
    for k, v in mapping:
        #  print("replacing")
        content=content.replace(k, v)
    #  print(content)
    #  abspeichern(r["fach"].get("fach"), pre, rc, ".rc")
    #  speicherziel=os.path.join(dir_path, speicherziel)
    #  abspeichern(r["fach"], pre, rc, ".rc")
    abspeichern(name_savegame, content, speicherziel, ".rc", False)
    pass

def build_conky(arr_big):
    variablenames=[]
    #  collect dirs and faecher
    fcollection={}
    for arr in arr_big:
        for x in arr:
            semester=x["meta"].get("semester", "NOS")
            #  try fcollection["semester"]:
            try:
                fcollection[semester].append(x["Lehrveranstaltung"])
            except KeyError:
                fcollection[ semester ]=[x["Lehrveranstaltung"]]
    #  pprint(fcollection)

    kk=build_header(fcollection)

    #  write conkies using the fcollection
    do_it=True
    if do_it:
        for arr in arr_big:
            for x in arr:
                bigrep=build_bigreplace(x["woche"], x["Lehrveranstaltung"], x["meta"].get("semester"), fcollection, kk)
                dirname=x["meta"].get("semester", "NO_SEMESTER")
                print(dirname)
                #  speicherziel=os.path.join(dir_path, "rc/"+speicherziel)
                speicherziel=os.path.join(dir_path, "rc/generated/"+dirname)
                print(speicherziel)
                if not os.path.exists(speicherziel):
                    print("check")
                    os.makedirs(speicherziel)
                print(speicherziel)
                write_conkyrc(x["Lehrveranstaltung"], bigrep, speicherziel)
                variablenames.append(x["Lehrveranstaltung"])

        faecherzeile=textblock(variablenames)

        mapping_fach = [
                #  ('replace_this2', faecherzeile),
            ('replace_this1', 'template1 "bashvariabe"')]

        write_conkyrc("conkyrc_static", mapping_fach, rc_static_finish, rc_static_raw)

build_conky(get_stuff(directory))
