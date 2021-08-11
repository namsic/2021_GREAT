import setuptools

install_requires = [
    'gym',
]

setup_kwargs = {
    'name': 'namjae-sim',
    'version': '0.1',
    'description': '2021_GREAT',
    'author': 'Namjae Kim',
    'author_email': 'kimnj3050@kookmin.ac.kr',
    'install_requires': install_requires
}

if __name__ == '__main__':
    setuptools.setup(**setup_kwargs)
