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

try:
    from ansiblelint.rules import AnsibleLintRule
# Backwards compatibility
except ImportError:
    from ansiblelint import AnsibleLintRule


class LowerTasknameRule(AnsibleLintRule):
    id = 'ADFINIS0001'
    shortdesc = "Tasknames shouldn't contain uppercase letters"
    description = "Tasknames should only contain lowercase letters and numbers"
    tags = ['formatting']

    def matchtask(self, task):
        return not task.get('name', '').islower()
