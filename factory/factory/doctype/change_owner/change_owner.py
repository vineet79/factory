# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ChangeOwner(Document):
	pass

@frappe.whitelist
def change_own(self):
	frappe.db.sql("""update `tabProject` set owner=%s where name=%s""",(self.user,self.project))
