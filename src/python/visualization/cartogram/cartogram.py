from folium import Map


def sample():
    mapa = Map(location=[-19.916667, -43.933333])
    mapa.save('teste.html')
