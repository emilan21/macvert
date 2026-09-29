macvert
-------

Convert 48-bit MAC addresses among colon (``aa:bb:cc:dd:ee:ff``), HP
(``aabb-ccdd-eeff``), no delimiter (``aabbccddeeff``), and dash
(``aa-bb-cc-dd-ee-ff``) forms. Letter case is preserved. Malformed input
returns an error instead of a partial conversion.

Install locally with ``python -m pip install .``; the optional local web UI
needs ``python -m pip install '.[web]'``. The command-line converter has no
runtime dependency beyond Python 3.10 or newer.

::

   macvert cli -m aa:bb:cc:dd:ee:ff -i colon -o hp
   macvert cli -f addresses.txt -i colon -o dash
   macvert server --port 5000

The server binds to localhost only. It has no authentication and is intended
for local use. The existing ``macvert.ini`` and WSGI file are historical;
review them separately before any external deployment.

Run ``python -m unittest discover -s tests -v`` and ``python -m build`` for
local checks. CI runs the same checks but does not deploy or publish a package.
Private Gitea is the source authority; public GitHub is a manually updated
copy. The repository retains historical Python bytecode in Git. Those files
are not needed at runtime and should be removed in a separate reviewed commit.
