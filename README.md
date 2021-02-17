# template-dash-multipage-app

This repository will allow you to make a web app quickly and easily. No more wasting your time with HTTP port routing, Flask, Gunicorn, or any of the other rabbit holes when all you want to do is to create a responsive design website that can be customly themed in one line of code, have virtually any layout, and may contain buttons, dropdowns, forms or any other element connected to Python functions. At the end, all you want to do is put this website on the internet.

## Features

* Contains several example pages with reference code on how to structure the layout of your page, create `callbacks` to add functionality and interactivity
* Can be used to create a single or multi-page webapp with your code neatly separated into different `.py` files for easy organizations
* Uses `poetry` as a package manager for `Python` dependencies, which separates your `dev` tools such as `autopep8` from the actual dependencies required for your app such as `Dash`
* Configured to be easily deployed to an `Azure` cloud environment to be hosted online and accessible by anyone simply by pointing the deployment slot on `Azure` to the `GitHub` repository link of your WebApp. Furthermore, any changes pushed to `master` automatically update the live webapp.

## Background

The app uses
* [Dash](https://dash.plotly.com/)
* [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)

`Dash` can create out-of-the-box interactive with
* [Plotly](https://plotly.com/python/)

## Installation

Use the package manager [poetry](https://python-poetry.org/) to install this project.

```bash
# Clone the repository
git clone git@github.com:Machine-Learning-Academy-of-Sciences/template-dash-multipage-app.git
# cd into the source code directory
cd template-dash-multipage-app\template_dash_multipage_app
# Launch the virtualenv or create it if it doesn't exist
poetry shell
# install all requirements if they need to be installed
poetry update
# launch web app
python index.py
```

## Usage

Edit `app.py`, `index.py` and add/delete/edit any of the pages in the folder `pages/` as you build your web app.

## Authors and acknowledgment

Created by Alekandr Gontcharov with support by Jason Carayanniotis.

## Contributing
Pull requests are welcome. 

## Support

For help on this project or how to use it, feel free to contact Aleksandr Gontcharov.
