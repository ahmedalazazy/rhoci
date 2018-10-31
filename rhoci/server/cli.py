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
import argparse

import rhoci.web

APP_NAME = "RHOCI"


def create_parser():
    """Returns argparse parser."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        dest="%s_DEBUG" % APP_NAME, help='Turn DEBUG on')
    parser.add_argument('--conf', '-c', dest="%s_CONFIG_FILE" % APP_NAME,
                        help='Configuration file')
    parser.add_argument('--port', '-p', dest="%s_SERVER_PORT" % APP_NAME,
                        help='Server port')

    return parser


def launch_app(args=None):
    """Runs Web application."""
    web_server = rhoci.web.Server(APP_NAME.lower(), args)
    web_server.run()


def main():
    """Main entry for running the web server."""
    parser = create_parser()
    args = parser.parse_args()
    launch_app(args)
