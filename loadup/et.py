#!/usr/bin/env python3


from lxml import etree
import collections
from helper import update_meta
from helper import abspeichern as abspeichern
import obj_control as ob
#  from collections import OrderedDict
import os.path
from pprint import pprint
from io import StringIO

dir_path = os.path.dirname(os.path.realpath(__file__))
data="faecher/"
directory=os.path.join(dir_path, data)
raw_data_test =os.path.join(dir_path, "fehlersuche/")
findall_chain=[".//div",".//table"]

quality_check_string = ""
relate = {'Woche': 'same_same', 'SWS': 'ignore', 'Lehrveranstaltung': 'Lehrveranstaltung', 'Art': 'ignore', 'Institut': 'ignore', 'DS': 'DS', 'Raum': 'Raum', 'Sprache': 'ignore', 'Module': 'ignore', 'Tag': 'Tag', 'Lehrbeauftragter': 'ignore'}
complex1=["Tag", "DS", "Raum", "Art"]
woche_global = [ "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Wochenede" ]

input_file = 'html/raw2.xml'
input_file2 = 'html/Stundenplan.html'
output_file = 'generated_stunden.py'

#  def write_data(output_file):
    #  output_file= open(output_file, encoding='utf-8')
    #  raw_string = output_file.read()
    #  output_file.close()

def get_data(input_file):
    raw_input= open(input_file)
    raw_string = raw_input.read()
    raw_input.close()
    return raw_string

def get_from_html(input_file=input_file2):
    # gather data
    parser=etree.HTMLParser()
    data=get_data(input_file)
    tree=etree.parse(StringIO(data), parser)
    html=tree.getroot()
    etree.strip_tags(html, "br")

    # gather and process to semantic list from html structure
    things = []
    ret_arr =[]
    category = None
    for ele in html.xpath('//div/h1 | //div/h2 | //div/table'):
        #  print("each ele:")
        if ele.tag in ('h1', 'h2'):
            category = [ele.text]
            things.append(category)
            #  print(type(category))
        if ele.tag in ('table'):
            category.append(ele)
    print("html extracted: "+str( things ))
    # process the list "read faecher"
    for thing in things:
        # 1st is 'name', the follwing are "tables"
        for thi in thing[1:]:
            #  print(thi)
            t=process_tree(thi)
            #  abspeichern(thing[0], t, raw_data_test)
            #  print("t: "+str(t))
            c=create_from_head(t, {'semester':thing[0]})
            #  abspeichern("fromHead_"+thing[0], c, raw_data_test)
            #  print(c.__len__())

            ready_for_file=transform(c)
            abspeichern(thing[0], ready_for_file, directory)
            #  abspeichern("transformed_"+thing[0], ready_for_file, directory)
            ret_arr.append(ready_for_file)

    return ret_arr

def process_string_recusrsion(string):
    """ old version of quality_check, does it w recursion, not working, donno why """
    barrier_lock=2
    starts_wrong=(" ", "\n")
    if string.__len__()>=2:
        for f in starts_wrong:
            if string.startswith(f):
               process_string(string[1:])
            else:
                barrier_lock-=1
        if barrier_lock==0:
            #  print(string)
            ret=string

def create_from_head(larr=[['h1','h2'], ['b1','b2']],meta={'create_from_head':'unset'}):
    #  merges the first table row as header
    #  print("larr: "+str(larr))
    headerlist=larr.pop(0)
    head=headerlist.__len__()
    res_arr=[]
    d={}
    #  d=collections.OrderedDict()
    for h in headerlist:
        d[h]="unset"
    #  print(d)
    for x in larr:
        #  dd={}
        dd=update_meta({}, meta)
        #  dd.update(meta)
        #  dd=collections.OrderedDict()
        if head>=x.__len__():
            for i, xx in enumerate(x):
                #  res_arr.append([headerlist[i], xx])
                dd[headerlist[i]]=xx
                #  res_arr.append(d[headerlist[i]]=xx)
        else:
            # pops on text in table tag, might need to be fixed -> mess header
            # length up
            print("else inside create_from_head")
            print("head: "+str(head)+"!>= x.len: "+str(x.__len__()))
            print("index_size mismatch on "+str(x))
        res_arr.append(dd)
        #  if i=0:
            #  d[x]="unset"
    #  for r in res_arr:
        #  print(r)

    #  print( "from create_from_head, res_arr:" + str(res_arr))
    return res_arr

def quality_check(string):
    """ does sanetize str after it gets read """
    barrier_lock=2
    starts_wrong=(" ", "\n")
    if type(string)==str:
        x=True
        while x:
            if string.__len__()>=2:
                for f in starts_wrong:
                    if string.startswith(f):
                        string = string[1:]
                        break
                    else:
                        barrier_lock-=1
                if barrier_lock==0:
                    x=False
                    return string
            else:
                x=False
                return False

def process_tree(tree):
    """ packs it, needs to be extended w delimeters
    also include parsing """

    partial=[]
    res=[]

    #  strips table rows and returns only "content"
    for e in tree.iter():
        #  print(e.tag, e.text)
        text=quality_check(e.text)
        if text:
            partial.append(text)
        if e.tag == "tr":
            res.append(partial)
            partial=[]
    ## remove empty
    for r in res:
        if r.__len__() == 0:
            res.remove(r)
    #  for r in res:
        #  print(str(r.__len__())+" "+str(r) +" ")
    #  print( "from process_tree, res:" + str(res))

    return res

def transform(c_from_h):
    """ sorts all and does transform into output """
    head="Lehrveranstaltung"
    woche=[]
    #  for j, x in enumerate(c_from_h):
    j=0
    for x in c_from_h:
        #  daily=collections.OrderedDict()
        #  print("this:"+str(type(x)))
        #  print(x)
        #  print(j)
        fach=x.get(head, "head not found")
        #  fach2=fach+"enumerated: "+str(j)
        j+=1
        #  update_meta(x, {'fach':fach})
        wdict=collections.OrderedDict({})
        #  meta.update(g.get('meta'))
        #  print(fach)
        #  woche.append(meta)
        #  woche.append({fach:{}})
        for t in woche_global:
            #  print("t found"+str(t))
            daily={}
            #  daily=collections.OrderedDict()
            try:
                t_arr=x["Tag"].split()
                wc=t_arr.count(t)
                while wc>0:
                    for i, dd in enumerate(t_arr):
                        if dd==t:
                            ds=int(x["DS"].split()[i][0])
                            art=x["Art"].split()[i][0]
                            raum=x["Raum"].split()[i]
                            turn=x["Woche"].split()[i][0]
                            info=str(art)+" "+str(raum)+"_"+str(turn)
                            #  print("ds"+str(ds))
                            preoccupied = daily.get(ds, False)
                            #  print(preoccupied, ds, info)
                            if preoccupied:
                                extension = preoccupied
                                preoccupied.append(info)
                                #  print("extension: "+str(extension)+str(type(extension)))
                                daily[ds] = extension
                                #  print(daily[ds])
                            else:
                                daily[ds] = [info]
                            #  daily[ds]=[info] ##restricted to #
                            #  daily[int(ds[0])].append(info) ##restricted to #
                            wc-=1
            except:
                #  basically skips day/hour resolution
                #  might need a keywordhook
                print('exception found, breaking out of transform with:')
                print(x)
            wdict.update({t:daily})
        for k_del in ["Woche", "Tag", "DS", "Art", "Raum" ]:
            x.pop(k_del, None)

        #  cleanup, and restructure
        #  for k_group in list(x.keys()):
            #  if k_group not in ["meta"]:
                #  pi={k_group: x[k_group]}
                #  #  print("pi: "+str(pi))
                #  x.pop(k_group)
                #  update_meta(x, pi, 'default')
        update_meta(x, wdict, 'woche')
        #  x.update(wdict)

            #  Woche
            #  woche[j].get(fach).update({t:daily})
            #  woche[j].update({t:daily})
        woche.append(x)
    #  wpop=woche.pop(0)
    #  print("wpop from transform: "+str(wpop))
    #  print("woche: "+str(woche))
    #  print("x: "+str(x))
    return woche
    #  return x


def safe_the_goods(the_goods):
    # split and distribute to files
    for g in the_goods: ##fach
        f=""
        #  for k in g.keys():
            #  f=k ##name des fachs
        abspeichern(g["meta"].get("fach", "unnamed by call"), g, directory, ".fach")
        #  abspeichern(str(f), g[f])

def write_stuff():
    #  tree = etree.parse(input_file)
    tree = etree.parse(input_file2)
    t=process_tree(tree)
    chunk=create_from_head(t)

    ready_for_file=transform(chunk)
    safe_the_goods(ready_for_file)

def formatting_conversion(loaded_d):
    """ converts from "safed" to "build" """
    result={}
    fach=loaded_d["meta"].get("fach")
    #  loaded_d["formatted"]=[]
    result["fach"]=fach
    result["formatted"]=[]
    for dd in woche_global:
        d_res={}
        d=loaded_d.get(dd)
        try:
            for k in d.keys():
                kk=int(k)
                try:
                    d_res[kk]
                except KeyError:
                    d_res[kk]=[]

                items=d[k].__len__()
                for x in d[k]:
                    sp=x.split(" ")
                    t=sp.pop(0)+" - "
                    raum=sp.pop(0)
                    #  d_res[kk].append([t+" - "+fach, raum])

                    if items==1:
                        d_res[kk]=[t+fach, raum]
                        #  d_res[kk].append([t+fach, raum])
                    else:
                        d_res[kk]=[t+fach, str(items)]
                        #  d_res[kk].append([t+fach, items])
                        break
                    #  print(d_res[kk])
                    #  d_res.update({kk:[t+" - "+fach, raum]})
            #  loaded_d["formatted"].append(d_res)
        except AttributeError:
            print('NOT FOUND: k in d.keys() || d: '+str(d))
        result["formatted"].append(d_res)
    return result

#  write_stuff()
#  write_conkyrc(arr)
#  def read_goods():
    #  files=os.path.
d=get_from_html()

#  for x in d:
    #  print("_________________________________")
    #  print(x)
