import datetime as d
import stunden

now = d.datetime.now().strftime("%H:%M")
ds_dict = stunden.doppelstunden

def find_current_DS(my_dict, now):
    now = str(now)
    #  print("now", now)
    timestate = "pause"
    for key in my_dict.keys():
        #  print("key: ", key)
        if my_dict[key][0] <= now:
            timestate = "pause"+str(key)
            #  print("works for key:", key)
            #  print("my_dict[key][0]", my_dict[key][0], "key: ", key)
            if now <= my_dict[key][1]:
                #  print("should hook here")
                timestate = str(key)+".DS"
                return timestate
    return timestate



if __name__ == "__main__":
    #  print(now)
    #  print(find_current_DS( ds_dict, now ))
    print(find_current_DS( ds_dict, now ))
