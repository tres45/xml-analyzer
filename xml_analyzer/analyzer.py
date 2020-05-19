from .html_parser import HtmlParser


class Analyzer:
    def __init__(self, original, target, id):
        self.diff_report = ''
        self.origin_html = HtmlParser(original)
        self.target_html = HtmlParser(target)
        self.origin = self.origin_html.get_elem_by_id(id)
        self.target = self.target_html.get_elem_by_id(id)
        self.analyze_data()
    
    def get_diff(self, target):
        return ''.join([
                'Before:\n',
                self.origin_html.get_element_info(self.origin),
                '\n\nAfter:\n',
                self.target_html.get_element_info(target)
            ])

    def analyze_data(self):
        if not self.origin:
            self.diff_report = 'Cannot found element'
            return
        
        if self.target:
            self.diff_report = self.get_diff(self.target)
            return

        origin_data = self.origin_html.get_element_data(self.origin)
        origin_path = self.origin_html.get_element_path(self.origin)
        elem_list = self.target_html.get_elems_by_name(self.origin.name)
        raw_diff = {}
        for cur_elem in elem_list:
            if len(cur_elem.contents) == 1:
                cur_data = self.target_html.get_element_data(cur_elem)
                cur_path = self.target_html.get_element_path(cur_elem)
                cmp_data = origin_data - cur_data
                if len(cmp_data) <= len(origin_data)/2:
                    raw_diff[len(cmp_data)] = cur_elem
        res = sorted(list(raw_diff.keys()))
        if len(res) == 0:
            self.diff_report = 'Cannot find element similar to the target'
            return
        self.diff_report = self.get_diff(raw_diff[res[0]])
