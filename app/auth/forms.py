from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField('电子邮箱', validators=[
        DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我（下次自动登录）')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    """Registration Form"""
    email = StringField('电子邮箱', validators=[
        DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               '用户名必须只含有字母，数字，点或者下划线')])
    companyname = StringField('公司名称', validators=[
        DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[
        DataRequired(), EqualTo('password2', message='两次输入的密码必须一致。')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已被注册。')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已被使用。')

    def validate_companyname(self, field):
        if User.query.filter_by(companyname=field.data).first():
            raise ValidationError('该公司名称已被使用。')


class ChangePasswordForm(FlaskForm):
    """Change Password Form"""
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('修改密码')


class PasswordResetRequestForm(FlaskForm):
    """Forget and Reset Password Request Form"""
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('忘了密码？')


class PasswordResetForm(FlaskForm):
    """Password Reset Form"""
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='两次输入的密码必须一致。')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('重设密码')

