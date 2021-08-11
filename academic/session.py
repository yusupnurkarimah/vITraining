from odoo import api, fields, models, _
import time

SESSION_STATES =[('draft','Draft'),('confirmed','Confirmed'),
('done','Done')]

class session(models.Model):
	_name = 'academic.session'

	name = fields.Char("Name", required=True, default='New', size=100)
		
	course_id = fields.Many2one(comodel_name="academic.course",	string="Course", required=True, )

	instructor_id = fields.Many2one(comodel_name="res.partner",	string="Instructor", required=True, )

	start_date = fields.Date(string="Start Date", required=False,
		default=lambda self:time.strftime("%Y-%m-%d"))
	duration = fields.Integer(string="Duration")
	seats = fields.Integer(string="Seats")
	active = fields.Boolean(string="Active", default=True)

	attendee_ids = fields.One2many(comodel_name="academic.attendee", inverse_name="session_id", string="Attendees", required=False, )

	taken_seats = fields.Float(compute="_calc_taken_seats",string="Taken Seat", required=False, )

	image_small = fields.Binary(string="Image Small",)

	state = fields.Selection(string="State", selection=SESSION_STATES,
						required=True,
						readonly=True,
						default=SESSION_STATES[0][0])
	
	@api.model
	def create(self, vals):
		if not vals.get('name', False) or vals['name'] == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('academic.session') or 'Error Number!!!'
		return super(session, self).create(vals)
		
	@api.multi
	def action_draft(self):
		self.state = SESSION_STATES[0][0]

	@api.multi
	def action_confirm(self):
		self.state = SESSION_STATES[1][0]

	@api.multi
	def action_done(self):
		self.state = SESSION_STATES[2][0]

	@api.depends('attendee_ids','seats')
	def _calc_taken_seats(self):
		for rec in self:
			if rec.seats>0:
				rec.taken_seats = 100.0 * len(rec.attendee_ids)/rec.seats
			else:
				rec.taken_seats = 0.0
	@api.multi
	def _cek_instruktur(self):
		for session in self:
			x = [att.partner_id.id for att in session.attendee_ids]
			if session.instructor_id.id in x:
				return False
		return True
	_constraints = [(_cek_instruktur, 'Instructor cannot be Attendee',
			['instructor_id', 'attendee_ids'])]