import frappe
import datetime


@frappe.whitelist(allow_guest=True)
def get_encounters_for_month(month=datetime.date.today().month):
    month_start = datetime.date.today().replace(day=1, month=month)
    month_end = (month_start.replace(day=28) + datetime.timedelta(days=4)) 
    month_end = month_end - datetime.timedelta(days=month_end.day)

    encounters = frappe.db.get_list('Patient Appointment', 
        filters=[[
        'date', 'between', [month_end, month_start]]],
        fields=['appointment_date', 'patient', 'a ppointment_time', 'name']
    )

    return encounters