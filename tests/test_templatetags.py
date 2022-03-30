from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

from forge.templatetags.sentry import sentry_js

SENTRY_TEST_DSN = "https://publickey@1.ingest.sentry.io/1"


def test_sentry_tag(settings, rf):
    settings.SENTRY_DSN = SENTRY_TEST_DSN
    settings.SENTRY_JS_ENABLED = True

    view = TemplateView.as_view(template_name="forge_base.html")
    request = rf.get("/")
    response = view(request)
    response.render()

    assert (
        b'<script src="https://js.sentry-cdn.com/publickey.min.js" crossorigin="anonymous"></script>'
        in response.content
    )

    settings.SENTRY_DSN = SENTRY_TEST_DSN
    settings.SENTRY_JS_ENABLED = False
    response = view(request)
    response.render()
    assert b"sentry-cdn" not in response.content

    settings.SENTRY_DSN = ""
    settings.SENTRY_JS_ENABLED = True
    response = view(request)
    response.render()
    assert b"sentry-cdn" not in response.content


def test_sentry_pii_enabled(settings, rf):
    settings.SENTRY_DSN = SENTRY_TEST_DSN
    settings.SENTRY_PII_ENABLED = True

    request = rf.get("/")
    request.user = get_user_model()(id=1, email="test@example.com", username="test")

    assert sentry_js({"request": request}) == {
        "sentry_js_enabled": True,
        "sentry_public_key": "publickey",
        "sentry_dialog_event_id": None,
        "sentry_init": {
            "release": None,
            "environment": "production",
            "sendDefaultPii": True,
            "initialScope": {
                "user": {
                    "id": 1,
                    "email": "test@example.com",
                    "username": "test",
                }
            },
        },
    }


def test_sentry_pii_enabled_without_user(settings, rf):
    settings.SENTRY_DSN = SENTRY_TEST_DSN
    settings.SENTRY_PII_ENABLED = True

    request = rf.get("/")

    assert sentry_js({"request": request}) == {
        "sentry_js_enabled": True,
        "sentry_public_key": "publickey",
        "sentry_dialog_event_id": None,
        "sentry_init": {
            "release": None,
            "environment": "production",
            "sendDefaultPii": True,
        },
    }


def test_sentry_pii_disabled(settings, rf):
    settings.SENTRY_DSN = SENTRY_TEST_DSN
    settings.SENTRY_PII_ENABLED = False

    request = rf.get("/")
    request.user = get_user_model()(id=1, email="test@example.com", username="test")

    assert sentry_js({"request": request}) == {
        "sentry_js_enabled": True,
        "sentry_public_key": "publickey",
        "sentry_dialog_event_id": None,
        "sentry_init": {
            "release": None,
            "environment": "production",
            "sendDefaultPii": False,
        },
    }


def test_sentry_release_env(settings, rf):
    settings.SENTRY_DSN = SENTRY_TEST_DSN
    settings.SENTRY_PII_ENABLED = False
    settings.SENTRY_RELEASE = "v1"
    settings.SENTRY_ENVIRONMENT = "production"

    request = rf.get("/")
    request.user = get_user_model()(id=1, email="test@example.com", username="test")

    assert sentry_js({"request": request}) == {
        "sentry_js_enabled": True,
        "sentry_public_key": "publickey",
        "sentry_dialog_event_id": None,
        "sentry_init": {
            "release": "v1",
            "environment": "production",
            "sendDefaultPii": False,
        },
    }
