from flask import Flask, render_template  # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/soil_science')
def soil_science():
    return render_template('soil_science.html')

@app.route('/land_mapping')
def land_mapping():
    barangays = [
        {
            'name': 'Babag',
            'sitios': [
                {
                    'name': 'Tugop Babag (Sitio 1)',
                    'coordinates': [(10.377220183717416, 123.85310421872815)],
                    'suitable': [
                        'land_mapping/babag/tugop/suitable1.jpg',
                        'land_mapping/babag/tugop/suitable2.jpg',
                        'land_mapping/babag/tugop/suitable3.jpg',
                        'land_mapping/babag/tugop/suitable4.jpg',
                        'land_mapping/babag/tugop/suitable5.jpg'
                    ],
                    'not_suitable': [
                        'land_mapping/babag/tugop/not_suitable1.jpg',
                        'land_mapping/babag/tugop/not_suitable2.jpg',
                        'land_mapping/babag/tugop/not_suitable3.jpg',
                        'land_mapping/babag/tugop/not_suitable4.jpg',
                        'land_mapping/babag/tugop/not_suitable5.jpg'
                    ]
                },
                {
                    'name': 'Babag Sitio 2',
                    'coordinates': [(10.365779502155927, 123.85695228449356)],
                    'suitable': [
                        'land_mapping/babag/sitio2/suitable1.jpg',
                        'land_mapping/babag/sitio2/suitable2.jpg',
                        'land_mapping/babag/sitio2/suitable3.jpg',
                        'land_mapping/babag/sitio2/suitable4.jpg',
                        'land_mapping/babag/sitio2/suitable5.jpg'
                    ],
                    'not_suitable': [
                        'land_mapping/babag/sitio2/not_suitable1.jpg',
                        'land_mapping/babag/sitio2/not_suitable2.jpg',
                        'land_mapping/babag/sitio2/not_suitable3.jpg',
                        'land_mapping/babag/sitio2/not_suitable4.jpg',
                        'land_mapping/babag/sitio2/not_suitable5.jpg'
                    ]
                },
                {
                    'name': 'Babag Sitio 3',
                    'coordinates': [(10.369436359861302, 123.8479318797376)],
                    'suitable': [
                        'land_mapping/babag/sitio3/suitable1.jpg',
                        'land_mapping/babag/sitio3/suitable2.jpg',
                        'land_mapping/babag/sitio3/suitable3.jpg',
                        'land_mapping/babag/sitio3/suitable4.jpg',
                        'land_mapping/babag/sitio3/suitable5.jpg'
                    ],
                    'not_suitable': [
                        'land_mapping/babag/sitio3/not_suitable1.jpg',
                        'land_mapping/babag/sitio3/not_suitable2.jpg',
                        'land_mapping/babag/sitio3/not_suitable3.jpg',
                        'land_mapping/babag/sitio3/not_suitable4.jpg',
                        'land_mapping/babag/sitio3/not_suitable5.jpg'
                    ]
                }
            ]
        }
    ]

    def calculate_bbox_and_center(coords):
        lats = [c[0] for c in coords]
        lngs = [c[1] for c in coords]
        min_lat, max_lat = min(lats), max(lats)
        min_lng, max_lng = min(lngs), max(lngs)
        center_lat = (min_lat + max_lat) / 2
        center_lng = (min_lng + max_lng) / 2
        bbox = [min_lng, min_lat, max_lng, max_lat]
        center = (center_lat, center_lng)
        return bbox, center

    for barangay in barangays:
        for sitio in barangay['sitios']:
            coords = sitio.get('coordinates')
            if coords:
                bbox, center = calculate_bbox_and_center(coords)
                sitio['bbox'] = bbox
                sitio['center'] = center
                sitio['latitude'], sitio['longitude'] = center

            sitio['suitable_images'] = sitio['suitable']
            sitio['not_suitable_images'] = sitio['not_suitable']

    map_sitios = []
    for barangay in barangays:
        for sitio in barangay['sitios']:
            lat = sitio.get('latitude')
            lng = sitio.get('longitude')
            if lat is not None and lng is not None:
                map_sitios.append({
                    'name': f"{barangay['name']} - {sitio['name']}",
                    'lat': lat,
                    'lng': lng
                })

    return render_template('land_mapping.html', barangays=barangays, map_sitios=map_sitios)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
