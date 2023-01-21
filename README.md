# forge-querystats

On each page, the query stats will display how many database queries were performed and how long they took.

[Watch on YouTube](https://www.youtube.com/watch?v=NX8VXxVJm08)

Clicking the stats in the toolbar will show the full SQL query log with tracebacks and timings.
This is even designed to work in production,
making it much easier to discover and debug performance issues on production data!

![Django query stats](https://user-images.githubusercontent.com/649496/213781593-54197bb6-36a8-4c9d-8294-5b43bd86a4c9.png)

It will also point out duplicate queries,
which can typically be removed by using `select_related`,
`prefetch_related`, or otherwise refactoring your code.

## Installation

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "forgequerystats",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "forgequerystats.QueryStatsMiddleware",
    # Put additional middleware below querystats
    # ...
]
```

We strongly recommend using the forge-stafftoolbar along with this,
but if you aren't,
you can add the querystats to your frontend templates with this include:

```html
{% include "querystats/button.html" %}
```

*Note that you will likely want to surround this with an if `DEBUG` or `is_staff` check.*

To view querystats you need to send a POST request (i.e. via a `<form>`),
and the template include is the easiest way to do that.
