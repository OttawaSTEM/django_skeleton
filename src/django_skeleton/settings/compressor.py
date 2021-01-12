# Local - Build paths inside the project like this: join(BASE_DIR, 'directory')
STATICFILES_FINDERS = (                                 # For Django-Compressor
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter', 
    'compressor.filters.cssmin.rCSSMinFilter'
]
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
COMPRESS_JS_FILTERS = [     # Only compress javascript in production
    'compressor.filters.jsmin.JSMinFilter'
]