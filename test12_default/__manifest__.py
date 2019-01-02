# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'test12',
    'version': '12.0.0.0.0',
    'category': 'Tools',
    'summary': "Test for v12",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/module-repo',
    'license': 'AGPL-3',
    'depends': [
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-test12', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'backend-theme', 'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',
         'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting', 'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '12.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '12.0'},
        {'usr': 'OCA', 'repo': 'partner-contact', 'branch': '12.0'},
        {'usr': 'OCA', 'repo': 'web', 'branch': '12.0'},
        {'usr': 'OCA', 'repo': 'server-tools', 'branch': '12.0'},

    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '12.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.6'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
    ]

}
