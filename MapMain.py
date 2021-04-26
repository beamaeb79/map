import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource, MapMarker

class MapMainApp(App):

    def build(self):
        print(MapSource.providers.keys())
        box_layout = BoxLayout()
        map_view = MapView(lat=7.8949508772650425,
                           lon=98.3531484281775,
                           zoom=50)
        map_view.map_source = "cyclemap"
        map_marker = MapMarker()
        map_marker.lat = 7.8949508772650425
        map_marker.lon = 98.3531484281775
        map_marker.source = "map-marker.png"
        map_view.add_widget(map_marker)
        box_layout.add_widget(map_view)
        return box_layout

if __name__ == "__main__":
    MapMainApp().run()