read -p "Are You Sure Deploy django_skeleton To Production @ Amazon AWS (Yes/No)?" choice
if [ "$choice" = "Yes" ]; then 
        # Push git
        cd /Volumes/Data/Workspace/Django/django_skeleton
        git push -u origin master

        # Update code from git
        # ssh -p 2200 admin@django_skeleton.ca "cd /home/admin/django_skeleton/ && /usr/bin/git fetch --all && git reset --hard origin/master"
        ssh -p 2200 admin@django_skeleton.ca "cd /home/admin/django_skeleton/ && /usr/bin/git pull"

        # Update PIP
        ssh -p 2200 admin@ottawastem.com "source /home/admin/venv/bin/activate && pip install pip --upgrade"
        
        # Install new django packages
        ssh -p 2200 admin@django_skeleton.ca "source /home/admin/venv/bin/activate && pip install -r /home/admin/django_skeleton/requirements.txt"

        # Copy static files to STATIC_ROOT
        ssh -p 2200 admin@django_skeleton.ca "source /home/admin/venv/bin/activate && cd /home/admin/django_skeleton/src/ && ./manage.py collectstatic --noinput"

        # Udate Database
        ssh -p 2200 admin@django_skeleton.ca "source /home/admin/venv/bin/activate && cd /home/admin/django_skeleton/src/ && ./manage.py migrate"

        # SEO - Ping Google after update with sitemap
        ssh -p 2200 admin@ottawastem.com "source /home/admin/venv/bin/activate && cd /home/admin/OttawaSTEM/src/ && ./manage.py ping_google"
        
        # Restart Django Server
        ssh -p 2200 admin@django_skeleton.ca "sudo service gunicorn restart"

        echo "Finished"
else
    echo "Deploy Django To Production @ Amazon AWS Is Canceled.";
fi