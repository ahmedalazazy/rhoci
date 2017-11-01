# Copyright 2017 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

""" RHOCI base exception handling. """


class RHOCIException(Exception):
    """Base RHOCI Exception.

    To use this class, inherit from it and define a 'message' property.
    """
    message = "An unknown exception occurred."

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        super(RHOCIException, self).__init__(self.message % kwargs)
        self.msg = self.message % kwargs


class APIException(RHOCIException):
    msg = "Something, somewhere went terribly wrong"
    code = 500
