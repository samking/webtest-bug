webtest-bug
===========

A minimal App Engine app that demonstrates a bug with `PATH_INFO`.

You can verify that `os.environ.PATH_INFO` is set in a production environment
by:

* Installing the Google Cloud SDK (https://developers.google.com/cloud/sdk/)
* Running `dev_appserver.py .` while in the app directory
* Going to http://localhost:8080/ and verifying that that the path `/` is
  printed and that `not set` is not printed.

You can verify that `os.environ.PATH_INFO` is NOT set in a webtest environment
by:

* Installing webapp2 (eg, `easy_install webapp2`)
* Running `python test.py` and verifying that the test doesn't pass.

Note that if you uncomment the `path_info = self.request.path_info` line, the
test will pass: webtest is setting only `self.request.path_info`, not
`os.environ['PATH_INFO']`.
