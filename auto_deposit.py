# Import playwright and yaml
from playwright.sync_api import sync_playwright
import yaml

# Read the config file
with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# Get the config values
password = config['password']['user']

