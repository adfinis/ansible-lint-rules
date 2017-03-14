#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2017, Adfinis SyGroup AG
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ansiblelint import AnsibleLintRule


class RegisterPrefixRule(AnsibleLintRule):
    id = 'ADFINIS0002'
    shortdesc = "Registered variable must always have a prefix \"$ROLENAME_register_\""
    description = """
    Each registered variable name must have a prefix "$ROLENAME_register_",
    because each variable should be unique.
    """
    tags = ['formatting']

    def match(self, file, line):
        return False

    def matchtask(self, file, task):
        if 'register' in task:
            register = task['register']
            try:
                role = self.rolename(file['path'])
            except BaseException:
                return False
            return not register.startswith('{0}_register_'.format(role))
        return False

    def rolename(self, file):
        elements = file.split('/')
        if 'tasks' in elements:
            idx = elements.index('tasks') - 1
            return elements[idx]
        raise IndexError('tasks not in path')
