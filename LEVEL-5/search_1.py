import pytest
from task1_1 import B
from task5_searcher import FileSearcher
class Test_Drive:
    def test_DriveCase(self):
        obj=B()
        self.expected=obj.getdrives()
        self.actual=['C:\\','D:\\']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileSearcher()
        d=obj.search_for_file('c','hcl_program1.txt')
        self.expected_file_name=d[0]
        self.actual_res='c:\hcl_programs\hcl_program1.txt'
        assert self.expected_file_name == self.actual_res

