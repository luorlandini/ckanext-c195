# ckanext-c195

CKAN extension for L&F customization

Available plugins:
- `c195`: currently only L&F customization 


## Requirements

This extension has been tested with CKAN 2.9.2 only.

## Installation

To install ckanext-c195:

1. Activate your CKAN virtual environment, for example:

       . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

       git clone https://github.com/geosolutions-it/ckanext-c195.git
       cd ckanext-c195
       pip install -e .
       pip install -r requirements.txt

3. Add `c195` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

       sudo service apache2 reload


## Config settings

None at present

## Developer installation

To install ckanext-c195 for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/geosolutions-it/ckanext-c195.git
    cd ckanext-c195
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
