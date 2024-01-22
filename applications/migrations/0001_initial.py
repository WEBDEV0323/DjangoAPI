# Generated by Django 1.11.5 on 2017-12-16 21:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("answer", models.TextField()),
            ],
            options={
                "ordering": ("question__order",),
            },
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.PositiveIntegerField(blank=True, default=1)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("submitted", "Application submitted"),
                            ("accepted", "Application accepted"),
                            ("rejected", "Application rejected"),
                            ("waitlisted", "Application on waiting list"),
                            ("declined", "Applicant declined"),
                        ],
                        default="submitted",
                        max_length=50,
                        null=True,
                        verbose_name="State of the application",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("newsletter_optin", models.BooleanField(default=False)),
                (
                    "rsvp_status",
                    models.CharField(
                        choices=[
                            ("waiting", "RSVP: Waiting for response"),
                            ("yes", "RSVP: Confirmed attendance"),
                            ("no", "RSVP: Rejected invitation"),
                        ],
                        default="waiting",
                        max_length=50,
                        verbose_name="RSVP status",
                    ),
                ),
                ("rsvp_yes_code", models.CharField(blank=True, max_length=24, null=True)),
                ("rsvp_no_code", models.CharField(blank=True, max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("subject", models.CharField(max_length=255)),
                (
                    "text",
                    models.TextField(
                        help_text="You can use HTML syntax in this message. Preview on the right.",
                        verbose_name="Content of the email",
                    ),
                ),
                (
                    "recipients_group",
                    models.CharField(
                        choices=[
                            ("submitted", "Application submitted"),
                            ("accepted", "Application accepted"),
                            ("rejected", "Application rejected"),
                            ("waitlisted", "Application on waiting list"),
                            ("declined", "Applicant declined"),
                            ("waiting", "RSVP: Waiting for response"),
                            ("yes", "RSVP: Confirmed attendance"),
                            ("no", "RSVP: Rejected invitation"),
                        ],
                        help_text="Only people assigned to chosen group will receive this email.",
                        max_length=50,
                        verbose_name="Recipients",
                    ),
                ),
                ("number_of_recipients", models.IntegerField(default=0, null=True)),
                ("successfuly_sent", models.TextField(blank=True, null=True)),
                ("failed_to_sent", models.TextField(blank=True, null=True)),
                ("sent_from", models.EmailField(max_length=254)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("sent", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Form",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text_header", models.CharField(default="Apply for a spot at Django Girls [City]!", max_length=255)),
                (
                    "text_description",
                    models.TextField(
                        default="Yay! We're so excited you want to be a part of our workshop. Please mind that filling out the form below does not give you a place on the workshop, but a chance to get one. The application process is open from {INSERT DATE} until {INSERT DATE}. If you're curious about the criteria we use to choose applicants, you can read about it on <a href='http://blog.djangogirls.org/post/91067112853/djangogirls-how-we-scored-applications'>Django Girls blog</a>. Good luck!"
                    ),
                ),
                (
                    "confirmation_mail",
                    models.TextField(
                        default="Hi there!This is a confirmation of your application to <a href=\"http://djangogirls.org/{city}\">Django Girls {CITY}</a>. Yay! That's a huge step already, we're proud of you!\n\nMind that this is not a confirmation of participation in the event, but a confirmation that we received your application.\n\nYou'll receive an email from the team that organizes Django Girls {CITY} soon. You can always reach them by answering to this email or by writing to {your event mail}.\nFor your reference, we're attaching your answers below.\n\nHugs, cupcakes and high-fives!\nDjango Girls",
                        help_text="Mail will be sent from your event mail.\nAlso the answers will be attached.",
                    ),
                ),
                ("open_from", models.DateTimeField(null=True, verbose_name="Application process is open from")),
                ("open_until", models.DateTimeField(null=True, verbose_name="Application process is open until")),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.TextField(verbose_name="Question")),
                (
                    "help_text",
                    models.TextField(blank=True, default="", verbose_name="Additional help text to the question?"),
                ),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("paragraph", "Paragraph"),
                            ("text", "Long text"),
                            ("choices", "Choices"),
                            ("email", "Email"),
                        ],
                        max_length=50,
                        verbose_name="Type of the question",
                    ),
                ),
                (
                    "is_required",
                    models.BooleanField(default=True, verbose_name="Is the answer to the question required?"),
                ),
                (
                    "choices",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text='Used only with "Choices" question type',
                        verbose_name="List all available options, separated with semicolon (;)",
                    ),
                ),
                (
                    "is_multiple_choice",
                    models.BooleanField(
                        default=False,
                        help_text='Used only with "Choices" question type',
                        verbose_name="Are there multiple choices allowed?",
                    ),
                ),
                ("order", models.PositiveIntegerField(help_text="Position of the question")),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "score",
                    models.FloatField(
                        default=0,
                        help_text="5 being the most positive, 1 being the most negative.",
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                ("comment", models.TextField(blank=True, help_text="Any extra comments?", null=True)),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scores",
                        to="applications.Application",
                    ),
                ),
            ],
        ),
    ]
