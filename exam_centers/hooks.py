from . import __version__ as app_version

app_name = "exam_centers"
app_title = "Exam Centers Managements"
app_publisher = "Wael Al-edrisi"
app_description = "for managing exam centers and final exams scheduling"
app_email = "waelaledrisi813636@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/exam_centers/css/exam_centers.css"
# app_include_js = "/assets/exam_centers/js/exam_centers.js"

# include js, css files in header of web template
# web_include_css = "/assets/exam_centers/css/exam_centers.css"
# web_include_js = "/assets/exam_centers/js/exam_centers.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "exam_centers/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "exam_centers.utils.jinja_methods",
#	"filters": "exam_centers.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "exam_centers.install.before_install"
# after_install = "exam_centers.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "exam_centers.uninstall.before_uninstall"
# after_uninstall = "exam_centers.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "exam_centers.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"exam_centers.tasks.all"
#	],
#	"daily": [
#		"exam_centers.tasks.daily"
#	],
#	"hourly": [
#		"exam_centers.tasks.hourly"
#	],
#	"weekly": [
#		"exam_centers.tasks.weekly"
#	],
#	"monthly": [
#		"exam_centers.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "exam_centers.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "exam_centers.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "exam_centers.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["exam_centers.utils.before_request"]
# after_request = ["exam_centers.utils.after_request"]

# Job Events
# ----------
# before_job = ["exam_centers.utils.before_job"]
# after_job = ["exam_centers.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"exam_centers.auth.validate"
# ]
