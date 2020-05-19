from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, html_file):
        self.html_file = html_file
        with open(html_file) as f:
            self.soup = BeautifulSoup(f, 'lxml')

    def get_elem_by_id(self, id):
        return self.soup.find(id=id)

    def get_elems_by_name(self, name):
        return self.soup.find_all(name)

    def __parse_idx(self, idx):
        return '[' + str(idx) + ']'

    def get_element_path(self, elem):
        names = [elem.name]
        indices = []
        prev = elem
        for parent in elem.parents:
            names.insert(0, parent.name)
            idx = parent.findChildren(recursive=False).index(prev)
            indices.insert(0,  self.__parse_idx(idx))
            if parent.name == 'html':
                indices.insert(0, self.__parse_idx(0))
                break
            prev = parent
        return ' > '.join([x+y for x,y in zip(names, indices)])

    def get_element_data(self, elem):
        res = []
        for k,v in elem.attrs.items():
            if type(v) == list:
                res.extend(v)
            else:
                res.append(v)
        if len(elem.contents) > 0:
            content = elem.contents[0].strip()
            res.append(content)
        return set(res)
    
    def get_element_info(self, elem):
        return elem.prettify() + 'Path: ' + self.get_element_path(elem)
