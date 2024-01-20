from test import x


def django_syntax(x):
    x = x.replace("assets", "{% static 'assets")
    x = x.replace(".js", ".js' %}")
    x = x.replace(".css", ".css' %}")
    x = x.replace(".jpg", ".jpg' %}")
    x = x.replace(".png", ".png' %}")
    return x


print(django_syntax(x))

