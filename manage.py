import os
import sys

def main():
    if os.environ.get('DJANGO_ENVIRONMENT') == 'Development':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.development')
    elif os.environ.get('DJANGO_ENVIRONMENT') == 'Container':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.container')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.virtualmachine')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
