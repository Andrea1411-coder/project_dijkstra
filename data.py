class TunjaData:
    
    NODOS = {
        "Plaza de Bolívar": (5.5324, -73.3617),
        "UPTC (Sede Central)": (5.5539, -73.3512),
        "C.C. Viva Tunja": (5.5471, -73.3514),
        "C.C. Unicentro": (5.5562, -73.3444),
        "Glorieta Norte": (5.5606, -73.3421),
        "Uniboyacá": (5.5678, -73.3364),
        "Hospital San Rafael": (5.5347, -73.3524),
        "Terminal Antigua": (5.5310, -73.3560),
        "Terminal Nueva (Sur)": (5.5020, -73.3850),
        "Estadio La Independencia": (5.5434, -73.3541),
        "Viaducto": (5.5376, -73.3575),
        "Bosque de la República": (5.5292, -73.3615),
        "Iglesia Santo Domingo": (5.5332, -73.3631),
        "Alto de San Lázaro": (5.5262, -73.3705),
        "Plaza del Sur": (5.5150, -73.3750)
    }

    CONEXIONES = [
        ("Plaza de Bolívar", "Iglesia Santo Domingo"),
        ("Plaza de Bolívar", "Bosque de la República"),
        ("Plaza de Bolívar", "Terminal Antigua"),
        ("Iglesia Santo Domingo", "Alto de San Lázaro"),
        ("Bosque de la República", "Alto de San Lázaro"),
        ("Terminal Antigua", "Hospital San Rafael"),
        ("Terminal Antigua", "Viaducto"),
        ("Terminal Antigua", "Plaza del Sur"),
        ("Hospital San Rafael", "Viaducto"),
        ("Hospital San Rafael", "Estadio La Independencia"),
        ("Viaducto", "C.C. Viva Tunja"),
        ("Estadio La Independencia", "C.C. Viva Tunja"),
        ("Estadio La Independencia", "UPTC (Sede Central)"),
        ("C.C. Viva Tunja", "UPTC (Sede Central)"),
        ("C.C. Viva Tunja", "C.C. Unicentro"),
        ("UPTC (Sede Central)", "C.C. Unicentro"),
        ("UPTC (Sede Central)", "Glorieta Norte"),
        ("C.C. Unicentro", "Glorieta Norte"),
        ("Glorieta Norte", "Uniboyacá"),
        ("Plaza del Sur", "Terminal Nueva (Sur)")
    ]

    