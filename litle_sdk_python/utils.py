# -*- coding: utf-8 -*-
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

import json
import os


class Configuration(object):
    """Setup Configuration variables.
    Attributes:
        user:            authentication.user
        password:        authentication.password
        merchantId:      The unique string to identify the merchant within the system.
        reportGroup:     To separate your transactions into different categories,
        url:             Url for server.
        proxy:           Https proxy server address. Must start with "https://"
        sftp_username:   Username for sftp
        sftp_password:   Password for sftp
        sftp_url:        Address for sftp
        fast_url:        Fast address
        fast_port:       Fast port
        print_xml:       Whether print request and response xml
        timeout:         Timeout
    """

    _VERSION = '9.10'
    _MERCHANTSDK = 'Python 9.10.0'
    _CONFIG_FILE_PATH = os.path.join(os.environ['VANTIV_SDK_CONFIG'], ".VANTIV_PYTHON_SDK.CONF") \
        if 'VANTIV_SDK_CONFIG' in os.environ else os.path.join(os.path.expanduser("~"), ".VANTIV_PYTHON_SDK.CONF")

    def __init__(self):
        """ Initial Configuration

        Load configuration if the config is existing in local file system.
        """
        self.user = ''
        self.password = ''
        self.merchantId = ''
        self.reportGroup = 'Default Report Group'
        self.url = 'https://www.testlitle.com/sandbox/communicator/online'
        self.proxy = ''
        self.sftp_username = ''
        self.sftp_password = ''
        self.sftp_url = ''
        self.fast_url = ''
        self.fast_port = ''
        self.print_xml = False
        self.timeout = 500
        # Load Configuration from local file system.
        try:
            with open(self._CONFIG_FILE_PATH, 'r') as config_file:
                config_json = json.load(config_file)
                self.user = config_json["user"] if "user" in config_json else ""
                self.password = config_json["password"] if "password" in config_json else ""
                self.merchantId = config_json["merchantId"] if "merchantId" in config_json else ""
                self.reportGroup = config_json["reportGroup"] if "reportGroup" in config_json else self.reportGroup
                self.url = config_json["url"] if "url" in config_json else self.url
                self.proxy = config_json["proxy"] if "proxy" in config_json else ""
                self.sftp_username = config_json["sftp_username"] if "sftp_username" in config_json else ""
                self.sftp_password = config_json["sftp_password"] if "sftp_password" in config_json else ""
                self.sftp_url = config_json["sftp_url"] if "sftp_url" in config_json else ""
                self.fast_url = config_json["fast_url"] if "fast_url" in config_json else ""
                self.fast_port = config_json["fast_port"] if "fast_port" in config_json else ""
                self.print_xml = config_json["print_xml"] if "print_xml" in config_json else self.print_xml
                self.timeout = config_json["timeout"] if "timeout" in config_json else self.timeout
        except Exception:
            # If get any exception just pass.
            pass

    def save(self):
        """Save Class Attributes to VANTIV_PYTHON_SDK.CONFIG

        It's a json

        Returns:
            True when the attributes saved successfully.

        Raises:
            IOError: An error occurred
        """
        with open(self._CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(vars(self), config_file)
        return True


def http_post(post_data, conf):
    """Post xml to server via https using requests

    Args:
        post_data: Request XML String
        conf: Instances of Configuration

    Returns:
        XML string for server response.

    Raise:
        When can't communicate with server, Error with Https Request, Please Check Proxy and Url configuration
        When the server response code is not 200, Error with Https Response, Status code: xxx
    """
    import requests
    headers = {'Content-type': 'application/xml'}
    proxies = {'https': conf.proxy} if (conf.proxy is not None and conf.proxy != '') else None
    try:
        response = requests.post(conf.url, data=post_data, headers=headers, proxies=proxies)
    except Exception as e:
        # TODO Change to custom Vantiv Exception.
        raise Exception("Error with Https Request, Please Check Proxy and Url configuration", e.message)
    if response.status_code != 200:
        # TODO Change to custom Vantiv Exception.
        raise Exception("Error with Https Response, Status code: ", response.status_code)
    return response.text
