from odoo import models, fields


class VisitResult(models.Model):
    _name = 'visit_result'
    _description = 'VisitResult'

    # اتصال به مدل medical.doctors
    Doctor = fields.Many2many(
        comodel_name='medical.doctors',
        relation='visit_result_doctor_rel', # نام جدول واسط
        string="پزشک معالج"
    )
    
    # اتصال به مدل medical.patient
    Patient = fields.Many2many(
        comodel_name='medical.patient',
        relation='visit_result_patient_rel', # نام جدول واسط
        string="نام بیمار"
    )
    
    factor_consultation_fee = fields.Float(string="هزینه ویزیت", default=280000.0)
    
    Status = fields.Selection(
        string="وضعیت", 
        required=True, 
        selection=[('pending','در حال انجام'),('done','ویزیت انجام شده است'),('cancel','لغو شده')]
    )
    
    is_active = fields.Boolean(default=True)