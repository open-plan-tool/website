Welcome to the open_plan website repository,

All topics concerning our static website project will be posted here. If you spot a typo on the website or have a question feel free to create a new [Issue](https://github.com/open-plan-tool/website/issues) or leave a comment at the [discussion section](https://github.com/open-plan-tool/website/discussions).

If you want to get in contact with the open_plan team please send an email to open_plan@rl-institut.de.

The open_plan team

![open_plan_logo (10X1)](https://user-images.githubusercontent.com/70587431/144256918-974fcefd-29f5-4b2f-b68b-6468327ef50b.png)

Learn more about the open_plan project on our [website](https://open-plan-tool.org/).


## Framework

[fastapi](https://fastapi.tiangolo.com/)

## Requirements

* python 3.8.10 or higher

## Getting started

1. Clone the repository locally
2. [Setup](https://oemof.readthedocs.io/en/latest/installation_and_setup.html#using-virtualenv-community-driven) a virtual environment.
3. Install the dependencies `pip install -r requirements.txt`
4. run the app locally with `. run_app.sh` (linux), or `uvicorn webapp:app --reload --port 5001` (windows or linux) you can visualize it in your browser under  `http://127.0.0.1:5001`

## Scss files

Any `.scss` file in `static/css` folder will be converted to a `.css` file automatically, to add it to one of your html template, use the following command

    <link rel="stylesheet" href="{{ url_for('static', path='/css/<name of your scss file>.css') }}">

Note the file name is the same, only the extension changes from `.scss` to `.css`

## Generate files for a static website

Execute the script

    python create_static_website.py

from the repository's root, the file will be generated automatically in the repository's root.

The index page is `index.html`