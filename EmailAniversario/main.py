import win32com.client as win32

#criar integração com o email
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

#configurar as informações do email
email.To = "pizricardo@gmail.com"
email.CC = "aewvsf@hotmail.com"
email.Subject = "E-mail de demonstração"
email.HTMLBody = """
<p>Tentativa de envio de e-mail automático</p>

essa tentativa está sem data agendada para envio
"""

email.Send()
print('E-mail enviado')