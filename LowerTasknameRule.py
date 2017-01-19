#!/usr/bin/env python

from ansiblelint import AnsibleLintRule


class LowerTasknameRule(AnsibleLintRule):
    id = 'ADFINIS0001'
    shortdesc = "Tasknames shouldn't contain uppercase letters"
    description = "Tasknames should only contain lowercase letters and numbers"
    tags = ['formatting']

    def matchtask(self, file, task):
        return not task.get('name', '').islower()
