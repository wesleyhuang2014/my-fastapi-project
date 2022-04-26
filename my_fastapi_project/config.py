import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="my_fastapi_project",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="my_fastapi_project_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from my_fastapi_project.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export my_fastapi_project_KEY=value
export my_fastapi_project_KEY="@int 42"
export my_fastapi_project_KEY="@jinja {{ this.db.uri }}"
export my_fastapi_project_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
my_fastapi_project_ENV=production my_fastapi_project run
```

Read more on https://dynaconf.com
"""
