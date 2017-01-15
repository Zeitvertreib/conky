from lxml import etree


input_file = 'html/rawX.xml'
#  def get_data(input_file):
    #  with open(input_file) as file:
        #  content = file.read()
    #  return content
def get_data(input_file):
    raw_input= open(input_file, encoding='utf-8')
    raw_string = raw_input.read()
    raw_input.close()
    return raw_string


def my_html_parse(content):
    parser = etree.HTMLParser()
    tree = etree.parse(content, parser)
    #  result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
    #  return result
    return tree

def selected(tree):
    for e in tree.findall('.//'):
        #  if type(e):
            #  print(type(e))
        if e.text:
            print(e.text)


def print_events(html):
    parser = etree.HTMLPullParser(events=('start', 'end'))
    parser.feed(html)
    for action, element in parser.read_events():
        if element.text:
        #  if element.tag != "br":
            #  print('%s: %s' % (action, element.tag))
            print(element.text)

content = get_data(input_file)
tt = etree.HTML(content)
#  print(content)
hello="heeeeeeellooo"
#  tree = etree.parse(content)
#  selected(tt)
#  my_html= my_html_parse(content)
#  print_events(my_html)
