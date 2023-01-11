from tethys_sdk.base import TethysAppBase


class TestAppStoreAquaveo(TethysAppBase):
    """
    Tethys app class for Test App Store Aquaveo.
    """

    name = 'Test App Store Aquaveo'
    description = 'This is my testing app for submission and installation'
    package = 'test_app_store_aquaveo'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test-app-store-aquaveo'
    color = '#045c34'
    tags = '"Hidrology", "testing" ,"Timeseries"'
    enable_feedback = False
    feedback_emails = []