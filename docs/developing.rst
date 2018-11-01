Developing
==========

.. code-block:: bash

    pip install -r development-requirements.txt
    pre-commit install



Making a release
----------------

* Increase the version in ``analytical/__init__.py``.
* Update the changelog in ``docs/changelog.rst``.
* Commit the changes.
* Tag the release in git: ``git tag $NEW_VERSION``.
* Push the tag: ``git push --tags origin``
* Upload the changes to PyPI:

  .. code-block:: bash

    rm -rf dist/
    python setup.py sdist bdist_wheel
    twine upload --sign --identity security@readthedocs.org dist/*
