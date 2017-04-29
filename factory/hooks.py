# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "factory"
app_title = "Factory"
app_publisher = "Mayur"
app_description = "MCPL"
app_icon = "octicon octicon-beaker"
app_color = "grey"
app_email = "mayur@mittalclothing.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/factory/css/factory.css"
# app_include_js = "/assets/factory/js/factory.js"

# include js, css files in header of web template
# web_include_css = "/assets/factory/css/factory.css"
# web_include_js = "/assets/factory/js/factory.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "factory.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "factory.install.before_install"
# after_install = "factory.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "factory.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
    "Change Owner": {
        "after_save": "factory.factory.doctype.change_owner.change_owner.change_own"
    }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"factory.tasks.all"
# 	],
# 	"daily": [
# 		"factory.tasks.daily"
# 	],
# 	"hourly": [
# 		"factory.tasks.hourly"
# 	],
# 	"weekly": [
# 		"factory.tasks.weekly"
# 	]
# 	"monthly": [
# 		"factory.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "factory.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "factory.event.get_events"
# }

