#!/usr/bin/env python3
import sys, os, re

#  data="faecher/"
dir_path = os.path.dirname(os.path.realpath(__file__))
#  directory=os.path.join(dir_path, data)

#  tdir=os.path.join(dir_path, "../rc/")
#  try:
tdir=sys.argv[1]
tdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), tdir)
#  print(tdir)

#  construct=["pointer to curr conk, #pos", "curr file", "# dirs", "# files", "files", "#files 2..", "files in 2"]
construct=["#pos", "curr_file", "#_dirs"]

tdir= os.path.join(dir_path, tdir)
tdirs=next(os.walk(tdir))[1]
#  print(tdirs)

def gentail(dir):
    #  print(dir)
    files=[a for a in os.listdir(dir) if re.search("",a)]
    #  [name for name in os.path.join(os.listdir(os.path.join(tdir, str(dir))), dir)]
    #  print(files)

    fdir=[]
    for x in files:
        fdir.append( os.path.join(dir, x))

    #  print(fdir)
    #  fdir=next(os.listdir(dir))
    i=0
    sub_arr=["# files"]
    for fn in fdir:
        #  fn=os.path.join(
        i=i+1
        sub_arr.append(fn)
    sub_arr[0]=i
    return sub_arr

construct[2]=tdirs.__len__()

for x in tdirs:
    construct.append(x)

for x in tdirs:
    xr=gentail(os.path.join(tdir, x))
    for xx in xr:
        construct.append(xx)

cc=""
for x in construct:
    #  print(x)
    cc=cc+str(x)+';'
    #  print(cc)
    print(x)
#  print(construct)
#  print(cc)
