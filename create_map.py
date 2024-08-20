import folium

# İHA'nın başlangıç konumu (YTÜ Beşiktaş kordinatları)
lat = 41.05149
lon = 29.01191

# Harita oluşturma
map = folium.Map(location=[lat, lon], zoom_start=15)

# İHA'nın konumunu işaretleyin
folium.Marker([lat, lon], popup="İHA").add_to(map)

# Haritayı kaydet
map.save("drone_map.html")
