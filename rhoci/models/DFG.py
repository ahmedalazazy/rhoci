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
from __future__ import absolute_import

import re

from rhoci.database import Database


class DFG(object):

    def __init__(self, name, squads=None, components=None,
                 squad_to_components=None):
        self.name = name
        self.squads = squads
        self.components = components
        self.squad_to_components = squad_to_components

    def save_to_db(self):
        if not Database.find_one("DFGs", {"name": self.name}):
            Database.insert(collection='DFGs',
                            data=self.json())

    def json(self):
        return {
            'name': self.name,
            'squads': self.squads,
            'components': self.components,
            'squad_to_components': self.squad_to_components,
        }

    @classmethod
    def get_all_DFGs_based_on_jobs(cls):
        """Returns a list of all DFGs based on job model where it cuts the
        DFG name from the job name and makes sure the set is unique.
        """
        DFGs = []
        regex = re.compile('DFG-', re.IGNORECASE)
        DFG_jobs = Database.find(collection='jobs',
                                 query={'name': regex})
        for job in DFG_jobs:
            jname = job['name']
            DFG_name = jname.split('-')[1] if '-' in jname else jname
            if DFG_name not in DFGs:
                DFGs.append(DFG_name)
        return DFGs

    @classmethod
    def get_all_squads(cls):
        squads = []
        for DFG_db in cls.find():
            if DFG_db['squads']:
                squads.extend(DFG_db['squads'])
        return squads

    @classmethod
    def get_all_components(cls):
        components = []
        for DFG_db in cls.find():
            if DFG_db['components']:
                components.extend(DFG_db['components'])
        return components

    @classmethod
    def get_squad_components(cls, DFG_name, squad):
        """Returns all the components of a given squad."""
        DFG_db = cls.find_one(name=DFG_name)
        return DFG_db['squad_to_components'][squad]

    @classmethod
    def find(cls):
        """Returns find query."""
        query = {}
        DFGs = Database.find(collection="DFGs", query=query)
        return DFGs

    @classmethod
    def find_one(cls, name):
        """Returns one query result."""
        query = {}
        if name:
            query['name'] = name
        DFGs = Database.find_one(collection="DFGs", query=query)
        return DFGs