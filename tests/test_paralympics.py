import requests
from dash.testing.application_runners import import_app
from selenium import webdriver

driver = webdriver.Chrome()


def test_server_live(dash_duo):
    # Create the app
    app = import_app(app_file="student.dash_single.paralympics_dash")
    # Start the server with the app using the dash_duo fixture
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    url = dash_duo.driver.current_url

    # Make an HTTP request to the server url
    response = requests.get(url)

    # Check that the status code in the HTTP response is 200
    assert response.status_code == 200
