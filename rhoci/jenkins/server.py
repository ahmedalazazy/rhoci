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
import jenkins
import logging

LOG = logging.getLogger(__name__)


def get_connection(url, user, password):
    """Given authentication details return a Jenkins connection."""
    try:
        conn = jenkins.Jenkins(url, user, password)
        return conn
    except Exception:
        LOG.info("Couldn't connect")
        return None