#!/usr/bin/env python
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
import os
import re
import sys
import inspect
import preGeneration

# Require Python 2.7.9 or higher or Python 3.4 or higher
if (sys.version_info[:3] < (2, 7 ,9)) or ((sys.version_info[0] == 3) and sys.version_info[:2] < (3, 4)):
    raise ValueError('''PyXB requires:
  Python2 version 2.7.9 or later; or
  Python3 version 3.4 or later
(You have %s.)''' % (sys.version,))

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

sys.path.insert(0, package_root)
from litle_sdk_python import fields

def remove_absolute_path(_package_root):
    """Remove all absolute path in generated file by pyxbgen.

    Returns:
        None

    """
    fields_path = os.path.join(_package_root, 'litle_sdk_python', 'fields.py')
    with open(fields_path, 'r') as ori_xsd:
        lines = ori_xsd.readlines()

        lines_index = -1
        abs_location = re.compile('pyxb.utils.utility.Location\(')
        for line in lines:
            lines_index += 1
            if abs_location.search(line):
                abs_path = re.search("pyxb.utils.utility.Location\('(.*?)'", line).group(1).strip()
                new_line = line.replace(abs_path, os.path.basename(abs_path))
                lines[lines_index] = new_line
                print('-', line)
                print('+', new_line)
                print()
        # TODO Not a good way, have to open the file twice.
        with open(fields_path, 'w') as ori_xsd_w:
            ori_xsd_w.writelines(lines)


def generate_index_rst(_package_root):
    _version = preGeneration.get_version(_package_root)
    _path_to_edited_xsd = os.path.join(_package_root, 'SchemaCombined_v%s.xsd' % _version)
    _index_rst_path = os.path.join(_package_root, 'docs/source/index.rst')
    # base string for index.rst
    index_rst_base = "Vantiv eCommerce Python SDK's documentation %s!\n" % _version
    index_rst_base += "%s" % '=' * len(index_rst_base)
    index_rst_base += '\n'
    index_rst_base += """
.. toctree::
   :maxdepth: 2
   :caption: Contents:

Batch
------
batch.stream
............
    .. autofunction:: litle_sdk_python.batch.stream

batch.download
..............
    .. autofunction:: litle_sdk_python.batch.download

batch.submit
............
    .. autofunction:: litle_sdk_python.batch.submit

batch.retrieve
..............
    .. autofunction:: litle_sdk_python.batch.retrieve

batch.Transactions
..................
    .. autoclass:: litle_sdk_python.batch.Transactions
        :members:

Configuration
-------------
    .. autoclass:: litle_sdk_python.utils.Configuration
        :members:

Online
------
    .. autofunction:: litle_sdk_python.online.request

Transactions
------------
"""

    # Get all class
    clsmembers = dict()
    for x in inspect.getmembers(fields, inspect.isclass):
        clsmembers[x[0]] = x[0]
    txns_list = []
    with open(_path_to_edited_xsd, 'r') as xsd_file:
        lines = xsd_file.readlines()
        # element_head = re.compile('<xs:element name="(\w+)">')
        element_head = re.compile('<xs:element name="(\w+)".*>')
        complex_type_head = re.compile('<xs:complexType>')
        txns_head = re.compile('<xs:element name="(\w+)" substitutionGroup="(xp:transaction|xp:recurringTransaction)">')
        lines_index = -1
        for line in lines:
            lines_index += 1
            element_find = element_head.search(line)
            if element_find and complex_type_head.search(lines[lines_index + 1]):
                try:
                    readable_name = element_find.group(1).strip()
                    obj = getattr(fields, readable_name)()
                    typename = type(obj).__name__
                    clsmembers[typename] = readable_name
                    # if 'Response' in readable_name:
                    #     clsmembers.remove(typename)
                    # else:
                    #     clsmembers[typename] = readable_name
                    #     # obj = getattr(fields, readable_name)()
                    #     attrs = dir(obj)
                    #     for x in dir(obj):
                    #         if x[0] == '_':
                    #             attrs.remove(x)
                    #     for x in no_attr_list:
                    #         attrs.remove(x)
                    #     attrs.sort()
                    #     clsmembers_attr[typename] = attrs
                except:
                    pass

            txn_found = txns_head.search(line)
            if txn_found:
                txns_list.append(txn_found.group(1).strip())

        # class readable name and attributes dict
        clsmembers_attr = dict()

        # dir() not attributes
        no_attr_list = ['Factory', 'append', 'content', 'extend', 'orderedContent', 'reset', 'toDOM', 'toxml',
                        'validateBinding', 'value', 'wildcardAttributeMap', 'wildcardElements', 'xsdConstraintsOK']
        for k in clsmembers:
            if 'Response' not in clsmembers[k]:
                obj = getattr(fields, clsmembers[k])()
                attrs = dir(obj)
                for x in dir(obj):
                    if x[0] == '_':
                        attrs.remove(x)
                for x in no_attr_list:
                    attrs.remove(x)
                attrs.sort()
                clsmembers_attr[clsmembers[k]] = attrs

        # Sort class by name
        class_list = list(clsmembers_attr.copy().keys())
        class_list.sort()

        txns_list.sort()

        for class_name in txns_list:
            index_rst_base += '%s\n%s\n' % (class_name, '.' * len(class_name))
            index_rst_base += '    .. py:class:: litle_sdk_python.fields.%s\n\n' % class_name
            for attr_name in clsmembers_attr[class_name]:
                try:
                    obj = getattr(fields, attr_name)()
                    typename = type(obj).__name__
                    index_rst_base += '        :var %s: instance of :py:class:`litle_sdk_python.fields.%s`\n' \
                                      % (attr_name,clsmembers[typename])
                except:
                    index_rst_base += '        :var %s: String or Number\n' % attr_name
            index_rst_base += '\n'
        index_rst_base += 'Complex Types\n-------------\n'
        for class_name in class_list:
            if class_name in txns_list:
                continue
            index_rst_base += '%s\n%s\n' % (class_name, '.' * len(class_name))
            index_rst_base += '    .. py:class:: litle_sdk_python.fields.%s\n\n' % class_name
            for attr_name in clsmembers_attr[class_name]:
                try:
                    obj = getattr(fields, attr_name)()
                    typename = type(obj).__name__
                    index_rst_base += '        :var %s: instance of :py:class:`litle_sdk_python.fields.%s`\n' \
                                      % (attr_name,clsmembers[typename])
                except:
                    index_rst_base += '        :var %s: String or Number\n' % attr_name
            index_rst_base += '\n'

        with open(_index_rst_path, 'w') as index_rst_file_w:
            index_rst_file_w.write(index_rst_base)

if __name__ == '__main__':
    remove_absolute_path(package_root)
    generate_index_rst(package_root)
