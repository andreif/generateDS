#!/usr/bin/env python

#
# Generated  by generateDS.py.
#

import sys

import simplecontent_restriction2_sup as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
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

class IdentifierTypeSub(supermod.IdentifierType):
    def __init__(self, schemeDataURI=None, schemeID=None, schemeAgencyName=None, schemeAgencyID=None, schemeName=None, schemeVersionID=None, schemeURI=None, valueOf_=None, extensiontype_=None):
        super(IdentifierTypeSub, self).__init__(schemeDataURI, schemeID, schemeAgencyName, schemeAgencyID, schemeName, schemeVersionID, schemeURI, valueOf_, extensiontype_, )
supermod.IdentifierType.subclass = IdentifierTypeSub
# end class IdentifierTypeSub


class BillOfResourcesIDTypeSub(supermod.BillOfResourcesIDType):
    def __init__(self, schemeDataURI=None, schemeID=None, schemeAgencyName=None, schemeAgencyID=None, schemeName=None, schemeVersionID=None, schemeURI=None, valueOf_=None):
        super(BillOfResourcesIDTypeSub, self).__init__(schemeDataURI, schemeID, schemeAgencyName, schemeAgencyID, schemeName, schemeVersionID, schemeURI, valueOf_, )
supermod.BillOfResourcesIDType.subclass = BillOfResourcesIDTypeSub
# end class BillOfResourcesIDTypeSub


class BillOfMaterialIDTypeSub(supermod.BillOfMaterialIDType):
    def __init__(self, schemeDataURI=None, schemeID=None, schemeAgencyName=None, schemeAgencyID=None, schemeName=None, schemeVersionID=None, schemeURI=None, valueOf_=None):
        super(BillOfMaterialIDTypeSub, self).__init__(schemeDataURI, schemeID, schemeAgencyName, schemeAgencyID, schemeName, schemeVersionID, schemeURI, valueOf_, )
supermod.BillOfMaterialIDType.subclass = BillOfMaterialIDTypeSub
# end class BillOfMaterialIDTypeSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = supermod.IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_=rootTag,
##         namespacedef_='',
##         pretty_print=True)
    return rootObj


def parseEtree(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = supermod.IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
##     content = etree_.tostring(rootElement, pretty_print=True,
##         xml_declaration=True, encoding="utf-8")
##     sys.stdout.write(content)
##     sys.stdout.write('\n')
    return rootObj, rootElement


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = supermod.IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_=rootTag,
##         namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = supermod.IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('#from simplecontent_restriction2_sup import *\n\n')
##     sys.stdout.write('import simplecontent_restriction2_sup as model_\n\n')
##     sys.stdout.write('rootObj = model_.IdentifierType(\n')
##     rootObj.exportLiteral(sys.stdout, 0, name_="IdentifierType")
##     sys.stdout.write(')\n')
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
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


