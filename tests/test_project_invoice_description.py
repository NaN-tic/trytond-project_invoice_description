# This file is part of the project_invoice_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProjectInvoiceDescriptionTestCase(ModuleTestCase):
    'Test Project Invoice Description module'
    module = 'project_invoice_description'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectInvoiceDescriptionTestCase))
    return suite
