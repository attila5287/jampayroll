from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, IntegerField, TextAreaField, RadioField, SelectField, DecimalField, Label 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from jampayroll.models import User, Employee, Employe3

class EmployeeForm(FlaskForm):
   firstName = StringField('first name',validators=[DataRequired()], default = 'Attila')
   middleName = StringField('middle name', default = 'Selcuk')
   lastName = StringField('last name',validators=[DataRequired()], default = 'Turkoz')
   companyName = StringField('company name',validators=[DataRequired()], default = 'JAM')
   allowance = IntegerField('allowance', default=2) 
   hourlyRate = DecimalField('hourly rate', validators=[DataRequired()], default = 44.00)
   def __rpr__(self):
      pass
      print('test add employee')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
# ===================== IMPLEMENT JAMPAYROLL BELOW =======================

class WeeklyHours(FlaskForm):
   pass
   hh_beg_01 = IntegerField(default = '09')
   mm_beg_01 = IntegerField(default = '00')
   ap_beg_01 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_01 = IntegerField(default = "09")
   mm_fin_01 = IntegerField(default = "00") 
   ap_fin_01 = SelectField(choices= [('0', 'a'), ('12', 'p' )])

   hh_beg_02 = IntegerField(default = '09')
   mm_beg_02 = IntegerField(default = '00')
   ap_beg_02 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_02 = IntegerField(default = "09")
   mm_fin_02 = IntegerField(default = "00") 
   ap_fin_02 = SelectField(choices= [('0', 'a'), ('12', 'p' )])

   hh_beg_03 = IntegerField(default = '09')
   mm_beg_03 = IntegerField(default = '00')
   ap_beg_03 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_03 = IntegerField(default = "09")
   mm_fin_03 = IntegerField(default = "00") 
   ap_fin_03 = SelectField(choices= [('0', 'a'), ('12', 'p' )])

   hh_beg_03 = IntegerField(default = '09')
   mm_beg_03 = IntegerField(default = '00')
   ap_beg_03 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_03 = IntegerField(default = "09")
   mm_fin_03 = IntegerField(default = "00") 
   ap_fin_03 = SelectField(choices= [('0', 'a'), ('12', 'p' )])

   hh_beg_04 = IntegerField(default = '09')
   mm_beg_04 = IntegerField(default = '00')
   ap_beg_04 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_04 = IntegerField(default = "09")
   mm_fin_04 = IntegerField(default = "00") 
   ap_fin_04 = SelectField(choices= [('0', 'a'), ('12', 'p' )])

   hh_beg_05 = IntegerField(default = '09')
   mm_beg_05 = IntegerField(default = '00')
   ap_beg_05 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_05 = IntegerField(default = "09")
   mm_fin_05 = IntegerField(default = "00") 
   ap_fin_05 = SelectField(choices= [('0', 'a'), ('12', 'p' )])

   hh_beg_06 = IntegerField(default = '09')
   mm_beg_06 = IntegerField(default = '00')
   ap_beg_06 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_06 = IntegerField(default = "09")
   mm_fin_06 = IntegerField(default = "00") 
   ap_fin_06 = SelectField(choices= [('0', 'a'), ('12', 'p' )])
   
   hh_beg_07 = IntegerField(default = '09')
   mm_beg_07 = IntegerField(default = '00')
   ap_beg_07 = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_fin_07 = IntegerField(default = "09")
   mm_fin_07 = IntegerField(default = "00") 
   ap_fin_07 = SelectField(choices= [('0', 'a'), ('12', 'p' )])
   def __rpr__(self):
      pass
      print('test')

   def calc_daily_totals(self):
      pass
      HourBeginWork = [
         self.hh_beg_01.data,
         self.hh_beg_02.data,
         self.hh_beg_03.data,
         self.hh_beg_04.data,
         self.hh_beg_05.data,
         self.hh_beg_06.data,
         self.hh_beg_07.data
      ]
      MinuteBeginWork = [
         self.mm_beg_01.data,
         self.mm_beg_02.data,
         self.mm_beg_03.data,
         self.mm_beg_04.data,
         self.mm_beg_05.data,
         self.mm_beg_06.data,
         self.mm_beg_07.data
      ]
      AmPmBeginWork = [
         self.ap_beg_01.data,
         self.ap_beg_02.data,
         self.ap_beg_03.data,
         self.ap_beg_04.data,
         self.ap_beg_05.data,
         self.ap_beg_06.data,
         self.ap_beg_07.data
      ]
      HourFinishWork = [
          self.hh_fin_01.data,
          self.hh_fin_02.data,
          self.hh_fin_03.data,
          self.hh_fin_04.data,
          self.hh_fin_05.data,
          self.hh_fin_06.data,
          self.hh_fin_07.data
       ] 
      MinuteFinishWork = [
         self.mm_fin_01.data,
         self.mm_fin_02.data,
         self.mm_fin_03.data,
         self.mm_fin_04.data,
         self.mm_fin_05.data,
         self.mm_fin_06.data, 
         self.mm_fin_07.data
      ]
      AmPmFinishWork = [
         self.ap_fin_01.data,
         self.ap_fin_02.data,
         self.ap_fin_03.data,
         self.ap_fin_04.data,
         self.ap_fin_05.data,
         self.ap_fin_06.data,
         self.ap_fin_07.data
      ] 
      total_hours = [
         ((((hh_out + int(ampm_out))* 60) + mm_out) - (((hh_in + int(ampm_in))* 60) + mm_in))* 1 / 60
         for (hh_out, ampm_out, mm_out, hh_in, ampm_in, mm_in) in zip(
            HourFinishWork,
            AmPmFinishWork,
            MinuteFinishWork,
            HourBeginWork,
            AmPmBeginWork,
            MinuteBeginWork
            )
      ]
      return total_hours

   def calc_daily_total(self):
      pass
      _list = self.calc_daily_totals()
      _sum = sum(_list)
      return float(_sum)

class DailyHours(FlaskForm):
   pass
   hh_in = IntegerField(default = '10')
   mm_in = IntegerField(default = '00')
   ampm_in = SelectField(choices = [('0', 'a'), ('12', 'p' )])
   hh_out = IntegerField(default = "09")
   mm_out = IntegerField(default = "00") 
   ampm_out = SelectField(choices=[('12', 'p'), ('0', 'a')])
   subm1t = SubmitField('S3ND')

   def __rpr__(self):
      pass
      print('test')

   def calc_daily_totals(self):
      pass
      self.hh_in.data = self.hh_in.data + int(self.ampm_in.data)
      self.hh_out.data = self.hh_out.data + int(self.ampm_out.data)
      min_total_in = (self.hh_in.data * 60) + self.mm_in.data
      min_total_out = (self.hh_out.data * 60) + self.mm_out.data
      total_hours = (min_total_out - min_total_in) * 1 / 60
      return total_hours

   def days(self):
      pass
      days=['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
      return days
