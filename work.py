#This file is part project_invoice_description module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Work']
__metaclass__ = PoolMeta


class Work:
    __name__ = 'project.work'

    def _get_invoice_line(self, key, invoice, lines):
        '''Add note data when invoice method is On Timesheet
        note: date -hour - description'''
        invoice_line = super(Work, self)._get_invoice_line(key, invoice, lines)

        description = []
        for line in lines:
            origin = line['origin']
            product = line['product']

            if origin.__name__ == 'timesheet.line':
                l = []
                l.append(origin.date.strftime("%d-%m-%Y")) #TODO: Date by locale
                l.append('%s %s' % (str(origin.hours), product.default_uom.rec_name))
                if origin.description:
                    l.append(origin.description)
                description.append(' - '.join(l))
                invoice_line.note = '\n'.join(description)

        return invoice_line
