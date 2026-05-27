class TunjaData:
    
    NODOS = {
        "Plaza Bolívar": {
        "coords": [5.5354, -73.3624],
        "icono":  "🏛️",
        "info": "Centro histórico de Tunja"
        },
        "Catedral Santiago": {
            "coords": [5.5350, -73.3622],
            "icono":  "⛪",
            "info": "Catedral Santiago de Tunja"
        },
        "Gobernación de Boyacá": {
            "coords": [5.5360, -73.3614],
            "icono":  "🏢",
            "info": "Sede de la Gobernación de Boyacá"
        },
        "Parque Santander": {
            "coords": [5.5344, -73.3607],
            "icono":  "🌳",
            "info": "Parque tradicional del centro de Tunja"
        },
        "Colegio de Boyacá": {
            "coords": [5.5366, -73.3641],
            "icono":  "🏫",
            "info": "Colegio de Boyacá — institución histórica"
        },
        "Hospital San Rafael": {
            "coords": [5.5370, -73.3548],
            "icono":  "🏥",
            "info": "Hospital San Rafael de Tunja"
        },
        "UPTC": {
            "coords": [5.5443, -73.3528],
            "icono":  "🎓",
            "info": "Universidad Pedagógica y Tecnológica de Colombia"
        },
        "Parque del Bosque": {
            "coords": [5.5476, -73.3597],
            "icono":  "🌲",
            "info": "Parque ecológico norte de Tunja"
        },
        "Viva Tunja": {
            "coords": [5.5430, -73.3587],
            "icono":  "🛍️",
            "info": "Centro Comercial Viva Tunja"
        },
        "Parque Pinzón": {
            "coords": [5.5332, -73.3594],
            "icono":  "🏞️",
            "info": "Parque Pinzón — zona centro-sur"
        },
        "SENA Tunja": {
            "coords": [5.5296, -73.3516],
            "icono":  "🔧",
            "info": "Servicio Nacional de Aprendizaje — Regional Boyacá"
        },
        "ESE Santiago de Tunja": {
            "coords": [5.5308, -73.3648],
            "icono":  "🩺",
            "info": "Empresa Social del Estado Santiago de Tunja"
        },
        "Estadio La Independencia": {
            "coords": [5.5272, -73.3705],
            "icono":  "⚽",
            "info": "Estadio La Independencia"
        },
        "Terminal de Transportes": {
            "coords": [5.5211, -73.3649],
            "icono":  "🚌",
            "info": "Terminal de transportes de Tunja"
        },
        "Unicentro Tunja": {
            "coords": [5.5184, -73.3583],
            "icono":  "🏬",
            "info": "Centro Comercial Unicentro Tunja"
        },
        "Universidad Santo Tomás": {
            "coords": [5.5197, -73.3508],
            "icono": "📚",
            "info": "Universidad Santo Tomás — Sede Tunja"
        },
    }


# (nodo_origen, nodo_destino, distancia_en_km)
    ARISTAS = [
         
        ("Plaza Bolívar", "Catedral Santiago", 0.1),
        ("Plaza Bolívar", "Gobernación de Boyacá", 0.2),
        ("Plaza Bolívar", "Colegio de Boyacá", 0.4),
        ("Catedral Santiago", "Parque Santander", 0.4),
        ("Gobernación de Boyacá", "Colegio de Boyacá", 0.3),
     
        ("Gobernación de Boyacá", "Hospital San Rafael", 0.9),
        ("Hospital San Rafael",  "UPTC", 1.2),
        ("Hospital San Rafael", "Viva Tunja", 1.1),
        ("UPTC", "Parque del Bosque", 0.8),
        ("UPTC", "Viva Tunja", 0.6),
        ("Parque del Bosque", "Viva Tunja", 0.7),
    
        ("Parque Santander", "Parque Pinzón", 0.6),
        ("Parque Santander", "ESE Santiago de Tunja", 0.8),
        ("Parque Pinzón", "SENA Tunja", 0.9),
        ("Parque Pinzón", "ESE Santiago de Tunja", 0.8),

        ("SENA Tunja", "Unicentro Tunja", 1.2),
        ("SENA Tunja", "Universidad Santo Tomás", 0.7),
        ("ESE Santiago de Tunja", "Estadio La Independencia",0.8),
        ("ESE Santiago de Tunja", "Terminal de Transportes", 0.6),

        ("Estadio La Independencia","Terminal de Transportes",1.8),
        ("Terminal de Transportes", "Unicentro Tunja",        1.0),
        ("Unicentro Tunja","Universidad Santo Tomás",      0.8),
    ]

    