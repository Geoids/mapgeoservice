from tethys_sdk.base import TethysAppBase, url_map_maker


class Mapapp(TethysAppBase):
    """
    Tethys app class for Map App.
    """

    name = 'Map App'
    index = 'mapapp:home'
    icon = 'mapapp/images/icon.gif'
    package = 'mapapp'
    root_url = 'mapapp'
    color = '#ffa500'
    description = 'This app has a MAP'
    tags = 'map'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='mapapp',
                controller='mapapp.controllers.home'
            ),
            UrlMap(
                name='bufferrings',
                url='mapapp/bufferrings',
                controller='mapapp.controllers.bufferrings'
            ),
            UrlMap(
                name='bufferpop',
                url='mapapp/bufferpop',
                controller='mapapp.controllers.bufferpop'
            ),
            UrlMap(
                name='about',
                url='mapapp/about',
                controller='mapapp.controllers.about'
            ),
        )

        return url_maps