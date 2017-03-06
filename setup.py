# -*- coding: utf-8 -*-
import sys

from setuptools import setup

# Require Python 2.7.9 or higher or Python 3.4 or higher
if (sys.version_info[:3] < (2, 7, 9)) or ((sys.version_info[0] == 3) and sys.version_info[:2] < (3, 4)):
    raise ValueError('''PyXB requires:
  Python2 version 2.7.9 or later; or
  Python3 version 3.4 or later
(You have %s.)''' % (sys.version,))

setup(name='LitleSdkPython',
      version='11.0.beta',
      description='Vantiv eCommerce Python SDK v2',
      author='Vantiv eCommerce',
      author_email='SDKSupport@vantiv.com',
      url='https://developer.vantiv.com/community/ecommerce',
      packages=['litle_sdk_python','scripts'],
      install_requires=[
          'PyXB==1.2.5',
          'paramiko>=1.14.0',
          'requests>=2.13.0',
          'six>=1.10.0',
          'xmltodict>=0.10.2'
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Environment :: MacOS X'
          'Environment :: Plugins'
          'Environment :: Win32 (MS Windows)'
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent'
          'Operating System :: MacOS',
          'Operating System :: Microsoft',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7.9',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Office/Business :: Financial',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      entry_points={
          'console_scripts': [
              'vantiv_python_sdk_setup = scripts.vantiv_python_sdk_setup:main',
          ],
      },
      )
