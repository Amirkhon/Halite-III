import collections
import itertools
import json
import sendgrid
import sendgrid.helpers
import sendgrid.helpers.mail

from python_http_client.exceptions import HTTPError

from . import app, config


sg = sendgrid.SendGridAPIClient(apikey=config.SENDGRID_API_KEY)


Recipient = collections.namedtuple("Recipient", [
    "user_id",
    "username",
    "email",
    "organization",
    "level",
    "date_created",
])


def send_notification(recipient_email, recipient_name, subject, body,
                      attachments=None):
    mail = sendgrid.helpers.mail.Mail()

    mail.from_email = sendgrid.Email("students24@aciworldwide.ru", "Studets24 Hackathon")
    personalization = sendgrid.helpers.mail.Personalization()
    personalization.add_to(sendgrid.helpers.mail.Email(recipient_email, recipient_name))
    personalization.subject = "Studets24 Hackathon: " + subject
    mail.add_personalization(personalization)

    mail.add_content(sendgrid.helpers.mail.Content("text/html", body))

    settings = sendgrid.helpers.mail.MailSettings()
    settings.sandbox_mode = sendgrid.helpers.mail.SandBoxMode(config.SENDGRID_SANDBOX_MODE)
    mail.mail_settings = settings

    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except HTTPError as e:
        app.logger.error("Could not send email", exc_info=e)
        app.logger.error("Response: {}".format(e.body))


def send_templated_notification(recipient, template_id, substitutions, group_id, category):
    """
    Send an email based on a template.
    :param Recipient recipient: The recipient of the email
    :param str template_id: The template ID of the email.
    :param Dict[str, Any] substitutions: Any other substitution variables to
    :param str group_id: The group ID of the email.
    pass to the email template.
    """
    mail = sendgrid.helpers.mail.Mail()

    if not recipient.organization:
        recipient = recipient._replace(organization="(no affiliation)")

    mail.from_email = sendgrid.Email("students24@aciworldwide.ru", "Studets24 Hackathon")
    personalization = sendgrid.helpers.mail.Personalization()
    personalization.add_to(sendgrid.helpers.mail.Email(recipient.email, recipient.username))

    all_substitutions = itertools.chain(
        recipient._asdict().items(), substitutions.items())
    for substitution_key, substitution_value in all_substitutions:
        personalization.add_substitution(sendgrid.helpers.mail.Substitution(
            "-{}-".format(substitution_key), substitution_value))

    mail.add_personalization(personalization)
    mail.template_id = template_id
    mail.asm = sendgrid.helpers.mail.ASM(group_id, [config.GOODNEWS_ACCOMPLISHMENTS, config.GAME_ERROR_MESSAGES, config.RESEARCH_EMAILS, config.NEWSLETTERS_ARTICLES])
    mail.add_category(sendgrid.helpers.mail.Category(category))
    settings = sendgrid.helpers.mail.MailSettings()
    settings.sandbox_mode = sendgrid.helpers.mail.SandBoxMode(config.SENDGRID_SANDBOX_MODE)
    mail.mail_settings = settings

    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except HTTPError as e:
        app.logger.error("Could not send email", exc_info=e)
        app.logger.error("Response: {}".format(e.body))

def send_templated_notification_simple(email, template_id, group_id, category):
    """
    Send an email based on a template.
    :param str email: The email recipient
    :param str template_id: The template ID of the email.
    :param str template_id: The group ID of the email.
    pass to the email template.
    """
    mail = sendgrid.helpers.mail.Mail()

    mail.from_email = sendgrid.Email("students24@aciworldwide.ru", "Studets24 Hackathon")
    personalization = sendgrid.helpers.mail.Personalization()
    personalization.add_to(sendgrid.helpers.mail.Email(email, email))

    mail.add_personalization(personalization)
    mail.template_id = template_id
    mail.asm = sendgrid.helpers.mail.ASM(group_id, [config.GOODNEWS_ACCOMPLISHMENTS, config.GAME_ERROR_MESSAGES, config.RESEARCH_EMAILS, config.NEWSLETTERS_ARTICLES])
    mail.add_category(sendgrid.helpers.mail.Category(category))
    settings = sendgrid.helpers.mail.MailSettings()
    settings.sandbox_mode = sendgrid.helpers.mail.SandBoxMode(config.SENDGRID_SANDBOX_MODE)
    mail.mail_settings = settings

    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
    except UnauthorizedError as e:
        app.logger.error("Could not send email", exc_info=e)

def add_user_to_contact_list(recipient):
    """
    Send an email based on a template.

    :param Recipient recipient: The recipient of the email
    pass to the email template.
    """
    data = [
                {
                    "email": recipient
                }
            ]
    try:
        response = sg.client.contactdb.recipients.post(request_body=data)
        print(response.status_code)
    except UnauthorizedError as e:
        app.logger.error("Could not add user to contact list", exc_info=e)
