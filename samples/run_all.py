# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
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

package_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, package_root)

dirs = []
_testfile_re = re.compile('^.*\.py$')

for d in os.listdir(package_root):
    dn = os.path.join(package_root, d)
    if os.path.isdir(dn):
        dirs.append(dn)

# build test file list.
while dirs:
    package_root = os.path.abspath(os.path.dirname(__file__))
    d = os.path.join(package_root, dirs.pop(0))
    for f in os.listdir(d):
        fn = os.path.join(d, f)
        if os.path.isdir(fn):
            dirs.append(fn)
        if _testfile_re.match(f):
            os.system('python %s' % fn)
