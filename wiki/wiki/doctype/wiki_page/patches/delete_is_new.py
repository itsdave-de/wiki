# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def execute():
	try:
		frappe.db.sql('alter table `tabWiki Page Patch` drop column is_new;')
		frappe.db.commit()
	except:
		pass
