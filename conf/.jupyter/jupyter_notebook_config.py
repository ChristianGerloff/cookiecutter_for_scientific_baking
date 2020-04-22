c = get_config()  # get the config object
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
c.NotebookApp.ip = '0.0.0.0'   # have to be zero not *
# do not open a browser window by default when using notebooks
c.NotebookApp.open_browser = False
# No token. Always use jupyter over ssh tunnel
# required for vs  studio
c.NotebookApp.token = '0bd62b549325a980c439c29ff32e848fb22baab98d5f1149483a457d931981bc'
c.NotebookApp.notebook_dir = '/src'
# Allow to run Jupyter from root user inside Docker container
c.NotebookApp.allow_root = True
c.NotebookApp.allow_origin = '*'
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}
