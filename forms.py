from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegistrationForm(FlaskForm):
    username =  StringField("아이디", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    email =  StringField("이메일", 
                            validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField("비밀번호 확인", 
                            validators=[DataRequired(), EqualTo("password")] )
    submit = SubmitField("가입")


# 일단 FlaskWTF의 FlaskForm를 불러오는데, 내가 원하는 form을 만들기 위해서는 FlaskForm이라는 부모 클래스를 상속 받아 자식 클래스를 만들어 사용하면 된다. (자식클래스를 선언할때 소괄호로 부모클래스를 포함시키게 되면 자식클래스에서는 부모클래스의 속성과 메소드는 기재하지 않아도 알아서 포함이 된다.)
# 그리고 이와 함께 wtforms라는 라이브러리를 사용한다. 예를 들면 문자열인지(StringField), 화면에 표시되지 않아야 할 패스워드인지(PasswordField), 제출 버튼인지(SubmitField)에 따라 원하는 폼을 지정할 수 있고, 이 후 wtforms.validators를 통해 필수입력값인지(DataRequired), 길이는 어떻게 제한하는지(Length), 이메일인지(Emil), 이미 입력한 값과 같은 값을 입력했는지(EqualTo) 등의 유효성 검사를 할 수 있다.
# 예제에서 생성한 클래스를 보면 일단 폼의 종류와 함께, 그 입력란의 label이 무엇인지 적어주고, validators를 통해 유효성 검사 항목을 포함해주면 끝이다.
