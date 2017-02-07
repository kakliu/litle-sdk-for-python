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
from __future__ import print_function

import os
import re
import sys


def create_edited_xsd(_path_to_ori_xsd, _path_to_edited_xsd):
    """Create a new copy of xsd file, and set minOccurs="0" for all elements with type

    The edited combined xsd will be override if exist.

    Args:
        _path_to_ori_xsd: Path to original combined xsd.
        _path_to_edited_xsd: Path to edited combined xsd.

    Returns: None

    Raise:
        IOError: path_to_ori_xsd does not exist
    """
    with open(_path_to_ori_xsd, 'r') as ori_xsd:
        lines = ori_xsd.readlines()
        # Original idea is setting minOccurs for all typed elements to 0. but didn't work.
        # lines_index = -1
        # xs_element = re.compile('<xs:element.*type=.*')
        # min_occurs_1 = re.compile('minOccurs="1"')
        # min_occurs_0 = re.compile('minOccurs="0"')
        # for line in lines:
        #     lines_index += 1
        #     if xs_element.search(line) and not min_occurs_0.search(line):
        #         newline = line.replace('minOccurs="1"', 'minOccurs="0"') if min_occurs_1.search(line) \
        #             else line.replace('/>', ' minOccurs="0"/>')
        #         print('-', lines_index, line.strip())
        #         print('+', lines_index, newline.strip())
        #         print()
        #         lines[lines_index] = newline
        with open(_path_to_edited_xsd, 'w+') as edited_xsd:
            edited_xsd.writelines(lines)


def fix_paypal_in_credit(_path_to_edited_xsd):
    """ Change element of paypal in credit to complexType payPal

    1. Edit complexType of payPal, add option of payerEmail
    2. Change element of paypal in credit to complexType payPal

    Args:
        _path_to_edited_xsd: Path to edited combined xsd.

    Returns: None

    """
    with open(_path_to_edited_xsd, 'r') as ori_xsd:
        lines = ori_xsd.readlines()

        # Edit complexType of payPal, add option of payerEmail
        type_paypal_head = re.compile('<xs:complexType name="payPal">')
        type_paypal_end = re.compile('</xs:complexType>')
        found_type_paypal_head = False
        # Have to set minOccurs of transactionId to 0, because when payPal is used in Credit, only payerId needed.
        old_paypal = ''
        new_paypal = '    <xs:complexType name="payPal">\n' \
                     '        <xs:choice>\n' \
                     '            <xs:sequence>\n' \
                     '                <xs:element name="payerEmail" type="xs:string" minOccurs="1" />\n' \
                     '            </xs:sequence>\n' \
                     '            <xs:sequence>\n' \
                     '                <xs:element name="payerId" type="xs:string" minOccurs="1" />\n' \
                     '                <xs:element name="token" type="xs:string" minOccurs="0" />\n' \
                     '                <xs:element name="transactionId" type="xs:string" minOccurs="0" />\n' \
                     '            </xs:sequence>\n' \
                     '        </xs:choice>\n' \
                     '    </xs:complexType>\n'
        lines_index = -1
        for line in lines:
            lines_index += 1
            if not found_type_paypal_head:
                if type_paypal_head.search(line):
                    found_type_paypal_head = True
                    old_paypal += lines[lines_index]
                    lines[lines_index] = ''
            else:
                old_paypal += lines[lines_index]
                lines[lines_index] = ''
                if type_paypal_end.search(line):
                    lines[lines_index] = new_paypal
                    break
        print('-', old_paypal)
        print('+', new_paypal)
        print()

        # 2. Change element of paypal in credit to complexType payPal
        lines_index = -1
        old_paypal = ''
        new_paypal = '                                    ' \
                     '<xs:element name="paypal" type="xp:payPal" />\n'
        credit_head = re.compile('<xs:element name="credit" substitutionGroup="xp:transaction">')
        found_credit_head = False
        paypal_elm_head = re.compile('<xs:element name="paypal">')
        found_paypal_elm_head = False
        paypal_ct_end = re.compile('</xs:complexType>')
        found_paypal_ct_end = False
        paypal_elm_end = re.compile('</xs:element>')
        for line in lines:
            lines_index += 1
            if not found_credit_head:
                if credit_head.search(line):
                    found_credit_head = True
            elif found_credit_head and not found_paypal_elm_head:
                if paypal_elm_head.search(line):
                    found_paypal_elm_head = True
                    old_paypal += lines[lines_index]
                    lines[lines_index] = ''
            else:
                old_paypal += lines[lines_index]
                lines[lines_index] = ''
                if not found_paypal_ct_end and paypal_ct_end.search(line):
                    found_paypal_ct_end = True
                if found_paypal_ct_end and paypal_elm_end.search(line):
                    lines[lines_index] = new_paypal
                    break
        print('-', old_paypal)
        print('+', new_paypal)
        print()

        # TODO Not a good way, have to open the file twice.
        with open(_path_to_edited_xsd, 'w') as ori_xsd_w:
            ori_xsd_w.writelines(lines)


def clear_simple_type(_path_to_edited_xsd):
    """Delete all simple types that have names.

    The xml validation will be performed on server. The purpose is to reduce the complexity of the xsd.
    Delete all simple types that have names, the elements used those will be replaced by build-in type.

    Args:
        _path_to_edited_xsd: Path to edited combined xsd.

    Returns: None

    """

    type_dict = {}
    with open(_path_to_edited_xsd, 'r') as ori_xsd:
        lines = ori_xsd.readlines()

        # build simple type to build-in type mapping dict, and delete the simple type definition.
        # {"xp:simple_type_name": "xs:build-in_type_name"}
        lines_index = -1
        simple_type_head = re.compile('<xs:simpleType.*name')
        simple_type_restriction = re.compile('<xs:restriction')
        simple_type_end = re.compile('</xs:simpleType>')
        found_simple_type_head = False
        old_content = ''
        for line in lines:
            lines_index += 1
            if not found_simple_type_head:
                if simple_type_head.search(line) and simple_type_restriction.search(lines[lines_index + 1]):
                    found_simple_type_head = True
                    old_content += lines[lines_index]
                    type_name = 'xp:' + re.search(' name="(.*)"', line).group(1).strip()
                    base_type_name = re.search(' base="(.*)"', lines[lines_index + 1]).group(1).strip()
                    type_dict[type_name] = base_type_name
                    lines[lines_index] = ''
            else:
                old_content += lines[lines_index]
                lines[lines_index] = ''
                if simple_type_end.search(line):
                    found_simple_type_head = False

        # Replace the simple types that deleted before with build-in type.
        lines_index = -1
        elm_with_simple_type = re.compile(' type="')
        elm_base_simple_type = re.compile(' base="')
        for line in lines:
            lines_index += 1
            if elm_with_simple_type.search(line):
                type_name = re.search(' type="(.*?)"', line).group(1)
                print(type_name)
                if type_name in type_dict.keys():
                    new_line = line.replace(type_name, type_dict[type_name])
                    print('-', lines_index, line)
                    print('+', lines_index, new_line)
                    print()
                    lines[lines_index] = new_line
            elif elm_base_simple_type.search(line):
                type_name = re.search(' base="(.*?)"', line).group(1)
                print(type_name)
                if type_name in type_dict.keys():
                    new_line = line.replace(type_name, type_dict[type_name])
                    print('-', lines_index, line)
                    print('+', lines_index, new_line)
                    print()
                    lines[lines_index] = new_line

        # TODO Not a good way, have to open the file twice.
        with open(_path_to_edited_xsd, 'w') as ori_xsd_w:
            ori_xsd_w.writelines(lines)


if len(sys.argv) != 2:
    print('Wrong arguments! please using: "python preGeneration.py PATH-TO-COMBINED_XMLSCHEMA"')
elif not os.path.isfile(os.path.abspath(sys.argv[1])):
    print("Combined XML Schema doesn't exist")
else:
    path_to_ori_xsd = os.path.abspath(sys.argv[1])

    # Generate absolute path edited combined xsd
    path_to_ori_xsd_split_ext = os.path.splitext(path_to_ori_xsd)
    path_to_edited_xsd = path_to_ori_xsd_split_ext[0] + '-edited' + path_to_ori_xsd_split_ext[1]

    # Create edited xsd
    create_edited_xsd(path_to_ori_xsd, path_to_edited_xsd)

    # Fix PayPal in Credit
    fix_paypal_in_credit(path_to_edited_xsd)

    # Fix PayPal in Credit
    clear_simple_type(path_to_edited_xsd)
