import os

from setuptools import setup

def package_data(pkg, roots):
    """Generic function to find package_data.
    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name="portal_api",
    version="0.3",
    author="Oficina EOL UChile",
    author_email="eol-ing@uchile.cl",
    description=".",
    packages=['portal_api','portal_api.settings'],
    package_dir={
        "portal_api": "portal_api",
        "portal_api.settings": "portal_api/settings"
    },
    install_requires=["unidecode>=1.1.1"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "lms.djangoapp": ["portal_api = portal_api.apps:PortalAPIConfig"]
    },
    package_data=package_data("portal_api", ["static", "public"]),
)

