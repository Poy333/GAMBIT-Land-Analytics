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
            'name': 'SUITABLE LAND OF BABAG',
            'sitios': [
                {
                    'name': 'Tugop Babag (Sitio 1)',
                    'coordinates': [(10.377220183717416, 123.85310421872815)],
                },
                {
                    'name': 'Babag-1 (Sitio 2)',
                    'coordinates': [(10.365779502155927, 123.85695228449356)],
                },
                {
                    'name': 'Hamtik (Sitio 3)',
                    'coordinates': [(10.369436359861302, 123.8479318797376)],
                }
            ]
        },
                        {
                            'name': 'SUITABLE LAND OF MALUBOG ',
                            'sitios': [
                                {
                    'name': 'Kang-Irag Sitio 1',
                    'coordinates': [
                        (10.398138501838254, 123.863607164473),
                        (10.397830847005448, 123.864125294955)  # Existing second coordinate
                    ],
                },
                {
                    'name': 'Tops Sitio 2',
                    'coordinates': [
                        (10.374431138925361, 123.8706553193261),
                        (10.377305963328025, 123.87193309357745)  # Existing second coordinate
                    ],
                },
               {
                    'name': 'Pung-ol Sitio 3',
                    'coordinates': [
                        (10.386370807140914, 123.87023625997749)
                    ],
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
