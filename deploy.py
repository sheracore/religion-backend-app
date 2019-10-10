import re
import sys

from gunicorn.app.wsgiapp import run

from application.app import create_app


app = create_app('application.config.DeploymentConfig')

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(run())
