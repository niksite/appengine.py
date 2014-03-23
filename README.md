appengine.py
============

GAE SDK download script.

	$ python appengine.py path/to/install
	WARNING:root:fetching new 1.9.1 version of GAE SDK
	WARNING:root:trying url http://googleappengine.googlecode.com/files/google_appengine_1.9.1.zip
	ERROR:root:cannot fetch url http://googleappengine.googlecode.com/files/google_appengine_{0}.zip because of HTTP404 error
	WARNING:root:trying url https://commondatastorage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.1.zip
	WARNING:root:release notes: https://code.google.com/p/googleappengine/wiki/SdkReleaseNotes
	WARNING:root:

	All
	==============================
	- The Performance Settings section of the Application settings page in the
	  Admin Console, Backends API and all backends related management tools are now
	  deprecated and will be removed in a future release. Users of Backends are
	  recommended to migrate to the App Engine Modules API, which provides a more
	  flexible implementation of the same functionality. These settings are now all
	  configurable via Modules configuration files.
	  See the Modules documentation for more information:
	  https://developers.google.com/appengine/docs/python/modules/
	  #Python_Configuration

	PHP
	==============================
	- Fixed an issue with ZendFramework causing App Engine project to crash when
	  using APC caching.
	    https://code.google.com/p/googleappengine/issues/detail?id=9553
	- Fixed an issue with URLFetch not sending strings with null characters
	  correctly.
	    https://code.google.com/p/googleappengine/issues/detail?id=10477
	- Fixed an issue with uploading files to a Google Cloud Storage failing
	  in 1.9.0.
	    https://code.google.com/p/googleappengine/issues/detail?id=10634


	WARNING:root:done

	$ python appengine.py path/to/install
	WARNING:root:current version of SDK is already installed
