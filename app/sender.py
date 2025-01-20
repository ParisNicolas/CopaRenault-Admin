import os
from email.message import EmailMessage
import ssl
import smtplib
import qrcode  #instalar y agregar a requiremets
import base64 #sirve de algo?

# Variables de entorno
MAIL_APP_PASSWORD = os.getenv('MAIL_APP_PASSWORD')
MAIL_APP_ADDRESS = os.getenv('MAIL_APP_ADDRESS')

email_sender = MAIL_APP_ADDRESS
password = MAIL_APP_PASSWORD
email_receiver = "d47173704@alumnos.itr.edu.ar"

subject = "Comunicado Copa Renault"
# welcome_body_email = """
# <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
#     <table role="presentation" style="width: 100%; border-collapse: collapse; background-color: #f4f4f4;">
#         <tr>
#             <td align="center" style="padding: 20px;">
#                 <table role="presentation" style="width: 600px; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);">
#                     <!-- Header -->
#                     <tr style="background-color: #FBAF30;">
#                         <td style="padding: 20px; text-align: center; color: white;">
#                             <h1 style="margin: 0; font-size: 24px;">¡Bienvenido a la Copa Renault!</h1>
#                         </td>
#                     </tr>

#                     <!-- Body -->
#                     <tr>
#                         <td style="padding: 20px; color: #333; text-align: left;">
#                             <p style="margin: 0 0 15px;">
#                                 Estimado/a participante,
#                             </p>
#                             <p style="margin: 0 0 15px;">
#                                 Nos complace informarle que hemos recibido su solicitud para participar en la <strong>Copa Renault</strong>, un evento deportivo único y emocionante que celebra la pasión por el automovilismo.
#                             </p>
#                             <p style="margin: 0 0 15px;">
#                                 A la brevedad, uno de nuestros representantes se pondrá en contacto con usted para brindarle más información y los próximos pasos a seguir.
#                             </p>
#                             <p style="margin: 0 0 15px; font-style: italic;">
#                                 Este correo es exclusivamente para el envío de información relacionada con el evento y no debe considerarse una vía de contacto válida.
#                             </p>
#                         </td>
#                     </tr>

#                     <!-- Contact Section -->
#                     <tr style="background-color: #f9f9f9;">
#                         <td style="padding: 20px;">
#                             <h2 style="margin: 0 0 15px; font-size: 20px; color: #FBAF30; text-align: center;">Nuestros medios de contacto</h2>
#                             <ul style="list-style: none; padding: 0; margin: 0; text-align: center; color: #555;">
#                                 <li style="margin: 5px 0;">📞 Teléfono: +54 11 1234-5678</li>
#                                 <li style="margin: 5px 0;">📧 Email: contacto@coparenault.com</li>
#                                 <li style="margin: 5px 0;">🌐 Sitio web: <a href="https://www.coparenault.com" style="color: #FBAF30; text-decoration: none;">www.coparenault.com</a></li>
#                             </ul>
#                         </td>
#                     </tr>

#                     <!-- Footer -->
#                     <tr>
#                         <td style="padding: 20px; text-align: center; color: #999; font-size: 12px; background-color: #333; color: white;">
#                             Este mensaje es informativo y no requiere respuesta. © 2025 Copa Renault. Todos los derechos reservados.
#                         </td>
#                     </tr>
#                 </table>
#             </td>
#         </tr>
#     </table>
# </body>

# """

confirm_email = """
<html>
<head>
    <style>
        body {
            background-color: #d3d3d3;
            text-align: center;
            padding: 20px;
        }

        img {
            max-width: 50%;
            height: auto;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="content">
        <img src="cid:embedded_image" alt="Copa Renault">
    </div>
</body>
</html>
"""
QR_email = """
##equipos de front/redes##
"""

def send_email(receiver=None, link=None):

    if link is not None:

        # Genera código QR
        qr = qrcode.QRCode(
            version=5,  # link de hasta 154 caracteres
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = "C:/Users/Tomas PC gamar/Desktop/CopaRenault-Admin/app/static/img/qr.png"
        img.save(img_path)

        # Envío del correo
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = receiver
        em["Subject"] = subject
        em.set_content("Tu cliente de correo no soporta HTML.")  # Versión de texto plano
        em.add_alternative(QR_email, subtype="html")  # Versión HTML

        # Enviar el correo
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, receiver, em.as_string())

        # Eliminar el archivo de imagen
        os.remove(img_path)


    else:
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = receiver
        em["Subject"] = subject
        em.set_content("Tu cliente de correo no soporta HTML.")
        em.add_alternative(confirm_email, subtype="html")

        with open("static/img/mail_img1.png", "rb") as img:
            img_data = img.read()
            em.add_attachment(
                img_data,
                maintype="image",
                subtype="png",
                filename="mail_img1.png",
                cid="embedded_image",
            )

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, receiver, em.as_string())

