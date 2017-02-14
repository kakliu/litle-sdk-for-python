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


def remove_absolute_path(_path_to_generated_py):
    """Remove all absolute path in generated file by pyxbgen.

    Args:
        _path_to_generated_py: path of generated file by pyxbgen.

    Returns:
        None

    """
    with open(_path_to_generated_py, 'r') as ori_xsd:
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
        with open(_path_to_generated_py, 'w') as ori_xsd_w:
            ori_xsd_w.writelines(lines)


lib_path = os.path.abspath('litle_sdk_python/litle_xml_fields.py')
remove_absolute_path(lib_path)
