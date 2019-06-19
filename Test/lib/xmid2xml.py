# encoding=utf-8

#from xmind2testlink.xmind_parser import parse_xmind_file
from lib.xmind_parser_u import parse_xmind_file
from xmind2testlink.testlink_parser import to_testlink_xml_file


def xmind2xml(file_path):
    return parse_xmind_file(file_path)


def suite2xml(suite,xml):
    return to_testlink_xml_file(suite, xml_out)

if __name__ == '__main__':
    rs = xmind2xml('/Users/yangcaihua/Documents/用户画像/用户画像-测试用例.xmind')
    suites = rs.sub_suites
    print(suites[2])
