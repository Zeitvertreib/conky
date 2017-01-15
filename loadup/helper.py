from collections import OrderedDict
from inspect import stack
import os.path
import codecs
import json
import shutil


doppelstunden = {
        1 : ["07:30", "09:00"],
        2 : ["09:20", "10:50"],
        3 : ["11:10", "12:40"],
        4 : ["13:00", "14:30"],
        5 : ["14:50", "16:20"],
        6 : ["16:40", "18:10"],
        7 : ["18:30", "20:00"],
        }

todo = {
        'header': 'h1',
        'member': 'table' }

findall_chain=[".//div",".//table"]
#  functions={"f2":woche_global}
woche_global = [ "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Wochenede" ]
#  meta = collections.OrderedDict({'meta':{'fach':'placeholder fach'}})

data="faecher/"
dir_path = os.path.dirname(os.path.realpath(__file__))
directory=os.path.join(dir_path, data)

def woche_to_dict():
    w=OrderedDict()
    for wx in woche_global:
        d={wx:{}}
        w.update(d)
    return w

def update_meta(d_target={}, key_s={'update_meta':'unset value'}, meta='meta', extend=False):
    #  somewhere was a bug
    try:
        #  if extend:
            #  d_target[meta]=key_s
        #  else:
        d_target[meta].update(key_s)
    except:
        #  print(str(stack()[1][3])+' inserted from update_meta new meta, this:'+str(key_s))
        d_target[meta]=key_s
        #  print('resulting dict: '+str(d_target))
    return d_target

def merge_dict_key(d_target, d_source, keyattribute):
    try:
        d_target[keyattribute].update(d_source[keyattribute])
    except:
        print(stack()[1][3])


def append_by_number_dict(d1="target",d2="source", fach=None):
    d_target={}
    for kk in d2.keys():
        d1[kk]=d1.get(kk, {})
        #  print("d1kk: "+str(d1[kk]))
        d_target=d1[kk]
        value=d2[kk]
        fachx={fach:value}
        d_target.update(fachx)
    #  return d_target

def generate_list(y):
    x=[]
    for y in range(1,y):
        x.append('')
        return x

def week_array():
    x=[]
    for y in range(6):
        for z in range(5):
            x.append('')

#  days_a_week=generate_list(5)
#  hours_a_day=generate_list(6)

def abspeichern(name_savegame="unnamed", content="no content", directory=directory, ending="", json_of=True):
    iterator=0
    file_found=False
    #  name_savegame=name_savegame.encode("ascii","ignore")
    #  name_savegame=name_savegame.decode("utf-8")
    #  print(name_savegame)
    safefile=os.path.join(directory,str(name_savegame))
    safefile_org=os.path.join(directory,str(name_savegame))
    #  content=json.loads(content)
    while os.path.isfile(safefile+ending):
        #  print("file found")
        safefile=safefile_org+'_'+str(iterator)
        iterator+=1
        file_found=True

    safefile=safefile+ending
    if file_found:
        print("file found.. copying")
        shutil.copy(safefile_org+ending, safefile)
    if json_of:
        with codecs.open(safefile_org+ending, "wt") as fileobj:
            json.dump(content, fileobj, indent=2)
    else:
        #  fileobj=open(safefile_org+ending)
        #  fileobj.write(content)
        #  fileobj.close()
        with open(safefile_org+ending, 'w') as fileobj:
            #  for line in content:
                #  print(line, fileobj)
            fileobj.write(content)
            #  fileobj.write("line2\nline1\n")
    #  print(str(type(content)))

    #  print(safefile)


