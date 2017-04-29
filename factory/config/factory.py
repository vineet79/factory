from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("Production"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Cutting Register"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Loading Register"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Hourly Production"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Outsourced Sewing"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Packing Register"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Standard Minute Value"
                                }
                        ]
                },
                {
                        "label": _("Masters"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Operations SMV"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Sampling"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Machine"
                                }
                        ]
                },
                {
                        "label": _("Setup"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Change Owner"
                                }
                        ]
                }
        ]
