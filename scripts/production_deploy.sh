read -p "Are You Sure Deploy DjangoBase To Production @ Amazon AWS (Yes/No)?" choice
if [ "$choice" = "Yes" ]; then 
        # Push git
        cd /Volumes/Data/Workspace/Django/DjangoBase
        git push -u origin master

        # Update code from git
        # ssh -p 2200 admin@djangobase.ca "cd /home/admin/DjangoBase/ && /usr/bin/git fetch --all && git reset --hard origin/master"
        ssh -p 2200 admin@djangobase.ca "cd /home/admin/DjangoBase/ && /usr/bin/git pull"

        # Update PIP
        ssh -p 2200 admin@ottawastem.com "source /home/admin/venv/bin/activate && pip install pip --upgrade"
        
        # Install new django packages
        ssh -p 2200 admin@djangobase.ca "source /home/admin/venv/bin/activate && pip install -r /home/admin/DjangoBase/requirements.txt"

        # Copy static files to STATIC_ROOT
        ssh -p 2200 admin@djangobase.ca "source /home/admin/venv/bin/activate && cd /home/admin/DjangoBase/src/ && ./manage.py collectstatic --noinput"

        # Udate Database
        ssh -p 2200 admin@djangobase.ca "source /home/admin/venv/bin/activate && cd /home/admin/DjangoBase/src/ && ./manage.py migrate"

        # SEO - Ping Google after update with sitemap
        ssh -p 2200 admin@ottawastem.com "source /home/admin/venv/bin/activate && cd /home/admin/OttawaSTEM/src/ && ./manage.py ping_google"
        
        # Restart Django Server
        ssh -p 2200 admin@djangobase.ca "sudo service gunicorn restart"

        echo "Finished"
else
    echo "Deploy Django To Production @ Amazon AWS Is Canceled.";
fi