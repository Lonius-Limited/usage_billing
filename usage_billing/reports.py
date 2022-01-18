import frappe
import datetime


@frappe.whitelist(allow_guest=True)
def get_encounters_for_month(*args, **kwargs):
    month = datetime.date.today().month # by default use current month
    year = datetime.date.today().year # by default use current year
    try:
        if 'month' in kwargs:month=int(kwargs['month'])
        if 'year' in kwargs:year=int(kwargs['year'])
    except:
        frappe.local.response.update({"error":"invalid month/year provided"})
        return
    
    month_start = datetime.date.today().replace(day=1, month=month, year=year)
    month_end = (month_start.replace(day=28) + datetime.timedelta(days=4)) 
    month_end = month_end - datetime.timedelta(days=month_end.day)

    encounters = frappe.db.get_list('Patient Encounter', 
        filters={'encounter_date': ['between', (month_start, month_end)]}, 
        fields=['encounter_date', 'patient', 'encounter_time', 'name', 'patient_name', 'appointment', 'appointment_type', ])

    frappe.local.response.update({"encounters":encounters, "from": month_start, "to": month_end, "count": len(encounters)})
    return

def load_credits(token):

    verified_amount = "" # decode and check jwt sent
    pass