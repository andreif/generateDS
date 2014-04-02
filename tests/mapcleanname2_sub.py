#!/usr/bin/env python

#
# Generated  by generateDS.py.
#
# Command line options:
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--silence', '')
#   ('--member-specs', 'list')
#   ('-f', '')
#   ('-o', 'tests/mapcleanname2_sup.py')
#   ('-s', 'tests/mapcleanname2_sub.py')
#   ('--super', 'mapcleanname2_sup')
#
# Command line arguments:
#   tests/mapcleanname.xsd
#
# Command line:
#   generateDS.py --no-dates --no-versions --silence --member-specs="list" -f -o "tests/mapcleanname2_sup.py" -s "tests/mapcleanname2_sub.py" --super="mapcleanname2_sup" tests/mapcleanname.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

import sys

import mapcleanname2_sup as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class complex_type01Sub(supermod.complex_type01):
    def __init__(self, string_value01=None, integer_value01=None, float_value01=None, field01=None):
        super(complex_type01Sub, self).__init__(string_value01, integer_value01, float_value01, field01, )
supermod.complex_type01.subclass = complex_type01Sub
# end class complex_type01Sub


class complex_type02Sub(supermod.complex_type02):
    def __init__(self, string_value02=None, integer_value02=None, float_value02=None, extensiontype_=None):
        super(complex_type02Sub, self).__init__(string_value02, integer_value02, float_value02, extensiontype_, )
supermod.complex_type02.subclass = complex_type02Sub
# end class complex_type02Sub


class complex_type03Sub(supermod.complex_type03):
    def __init__(self, string_value02=None, integer_value02=None, float_value02=None, string_value03=None, integer_value03=None, float_value03=None):
        super(complex_type03Sub, self).__init__(string_value02, integer_value02, float_value02, string_value03, integer_value03, float_value03, )
supermod.complex_type03.subclass = complex_type03Sub
# end class complex_type03Sub


class type_Sub(supermod.type_):
    def __init__(self, string_value02=None, integer_value02=None, float_value02=None, extensiontype_=None):
        super(type_Sub, self).__init__(string_value02, integer_value02, float_value02, extensiontype_, )
supermod.type_.subclass = type_Sub
# end class type_Sub


class complex_type04Sub(supermod.complex_type04):
    def __init__(self, string_value02=None, integer_value02=None, float_value02=None, string_value03=None, integer_value03=None, float_value03=None):
        super(complex_type04Sub, self).__init__(string_value02, integer_value02, float_value02, string_value03, integer_value03, float_value03, )
supermod.complex_type04.subclass = complex_type04Sub
# end class complex_type04Sub


class build_Sub(supermod.build_):
    def __init__(self, string_value02=None, integer_value02=None, float_value02=None, extensiontype_=None):
        super(build_Sub, self).__init__(string_value02, integer_value02, float_value02, extensiontype_, )
supermod.build_.subclass = build_Sub
# end class build_Sub


class complex_type05Sub(supermod.complex_type05):
    def __init__(self, string_value02=None, integer_value02=None, float_value02=None, string_value03=None, integer_value03=None, float_value03=None):
        super(complex_type05Sub, self).__init__(string_value02, integer_value02, float_value02, string_value03, integer_value03, float_value03, )
supermod.complex_type05.subclass = complex_type05Sub
# end class complex_type05Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'complex_type01'
        rootClass = supermod.complex_type01
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='',
##             pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'complex_type01'
        rootClass = supermod.complex_type01
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(content)
##         sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'complex_type01'
        rootClass = supermod.complex_type01
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'complex_type01'
        rootClass = supermod.complex_type01
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('#from mapcleanname2_sup import *\n\n')
##         sys.stdout.write('import mapcleanname2_sup as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
