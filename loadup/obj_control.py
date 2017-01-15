#! /bin/python3

todo = {
        'header': 'h1',
        'member': 'table' }

tags = ['h1', 'table']

def convert(todo={}):
    conv={}
    for k, v in todo.items():
        v= './/'+v
        conv[k]=v
    return conv

#  def check_todo(keyword, todo):
    #  if todo.get(keyword):

#  t=convert(todo)
#  print( t )

class Sorted:

    def __init__(self, keymap=todo):
        self.todo = convert(keymap)
        #  self.tags = tags
        self.name_items = []
        print(self.todo)

    def feed(self, tree):
        print("feed: "+str(tree))
        header= [ e.text for e in tree.findall(self.todo['header'])]
        for e in tree.findall(self.todo['header']):
            tables=e.findall(self.todo['member'])
            print(tables)
        print(header)
        if self.todo['header'] == tree.tag:
            self.name_items.append(tree.text)
        if self.todo['member'] == tree.tag:
            self.name_items.append(tree.text)
        #  for self.tag.get('header') == tag.tag:
            #  for s in tag.findall(self.tag.get('member'))
        #  if tag in self.tags:
            #  if 


sobj=Sorted(todo)


