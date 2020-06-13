import folium
import googlemaps


class Gmap:
    def updateLocation(find_loc):
        # 찾을 위치. 한글이므로 유니코드의 u를 붙여줘야한다.
        gmaps = googlemaps.Client(key="-")
        geo = gmaps.geocode(find_loc)
        lat_long = [geo[0]['geometry']['location']['lat'], geo[0]['geometry']['location']['lng']]

        map_2 = folium.Map(location=lat_long,
                           zoom_start=13)
        folium.CircleMarker(location=lat_long, radius=200,
                            popup=find_loc, line_color='#3186cc',
                            fill_color='#3186cc').add_to(map_2)
        map_2.save('osm.html')
        return map_2.get_root().render()


