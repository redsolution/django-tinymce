from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from os.path import dirname, join
import shutil

class Make(BaseMake):

    def make(self):
        super(Make, self).make()
        cms_settings = GrandmaSettings.objects.get_settings()
        
        cms_settings.render_to('settings.py', 'tinymce/grandma/settings.py')
        cms_settings.render_to('urls.py', 'tinymce/grandma/urls.py')

    def postmake(self):
        super(Make, self).postmake()
        cms_settings = GrandmaSettings.objects.get_settings()
        tinymce_media_dir = join(dirname(dirname(__file__)), 'media')
        project_media_dir = join(cms_settings.project_dir, 'media')

#       WARNING! Silently delete media dirs
        try:
            shutil.rmtree(join(project_media_dir, 'tinymce'))
#            no such directory
        except OSError:
            pass

        if 'grandma.django-server-config' not in cms_settings.installed_packages:

#           copy files to media directory
            shutil.copytree(
                join(tinymce_media_dir, 'tinymce'),
                join(project_media_dir, 'tinymce'),
            )
