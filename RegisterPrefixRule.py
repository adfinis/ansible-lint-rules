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

import re

try:
    from ansiblelint.rules import AnsibleLintRule
# Backwards compatibility
except ImportError:
    from ansiblelint import AnsibleLintRule


class RegisterPrefixRule(AnsibleLintRule):
    id = 'ADFINIS0002'
    shortdesc = "Registered variable must always have a prefix " \
                "\"$ROLENAME_register_\""
    description = """
    Each registered variable name must have a prefix "$ROLENAME_register_",
    because each variable should be unique.
    """
    tags = ['formatting']

    def matchtask(self, file, task):
        if 'register' in task:
            register = task['register']
            try:
                role = self.rolename(file['path'])
                prefix = '{0}_register_'.format(role)
            except BaseException:
                prefix = 'register_'
            return not register.startswith(prefix)
        return False

    def rolename(self, filename):
        elements = re.findall(r"[\w']+", filename)
        if 'tasks' in elements:
            # split the file path into elements and
            # get the element before "tasks",
            # which is most likely the full rolename
            idx = elements.index('tasks') - 1
            return elements[idx]
        raise IndexError('tasks not in path')
