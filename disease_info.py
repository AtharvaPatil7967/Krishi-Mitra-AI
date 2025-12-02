# disease_info.py

DISEASE_DATABASE = {
    "Bacterial_spot": {
        "disease_name": "Bacterial Spot",
        "description": "Bacterial disease causing dark spots with yellow halos on leaves",
        "severity": "High",
        "treatment": {
            "chemical": "Copper-based fungicide @ 2g/L water every 10 days",
            "organic": "Neem oil spray 5ml/L + remove infected leaves",
            "frequency": "Spray every 7-10 days until symptoms disappear"
        },
        "prevention": [
            "Use disease-free seeds",
            "Avoid overhead watering",
            "Crop rotation with non-solanaceous crops",
            "Remove and destroy infected plant debris"
        ],
        "cultural_practices": [
            "Improve air circulation between plants",
            "Water at base early morning",
            "Sanitize tools between plants",
            "Avoid working with wet plants"
        ]
    },
    "Early_blight": {
        "disease_name": "Early Blight",
        "description": "Fungal disease with concentric ring patterns on older leaves",
        "severity": "Medium",
        "treatment": {
            "chemical": "Mancozeb 75% WP @ 2-2.5g/L water",
            "organic": "Trichoderma viride 5g/L + Neem cake application",
            "frequency": "Every 7-10 days, start at first symptoms"
        },
        "prevention": [
            "Use resistant varieties",
            "Balanced fertilization (avoid excess nitrogen)",
            "Crop rotation (2-3 years)",
            "Deep plowing to bury infected debris"
        ],
        "cultural_practices": [
            "Remove lower infected leaves",
            "Mulch around plants to prevent soil splash",
            "Improve air circulation",
            "Water at base in morning"
        ]
    },
    "Late_blight": {
        "disease_name": "Late Blight",
        "description": "Severe fungal disease causing water-soaked lesions and white mold",
        "severity": "Very High",
        "treatment": {
            "chemical": "Metalaxyl + Mancozeb @ 2.5g/L water immediately",
            "organic": "Bordeaux mixture 1% + destroy infected plants",
            "frequency": "Every 5-7 days in humid conditions"
        },
        "prevention": [
            "Plant resistant varieties",
            "Avoid planting near potato fields",
            "Ensure good drainage",
            "Destroy all infected plant material"
        ],
        "cultural_practices": [
            "Space plants for air movement",
            "Avoid evening watering",
            "Remove volunteer tomato plants",
            "Monitor weather for high humidity"
        ]
    },
    "Leaf_Mold": {
        "disease_name": "Leaf Mold",
        "description": "Fungal disease causing pale spots with olive-green mold on leaf undersides",
        "severity": "Medium",
        "treatment": {
            "chemical": "Chlorothalonil @ 2g/L water",
            "organic": "Potassium bicarbonate spray + improve ventilation",
            "frequency": "Every 10-14 days"
        },
        "prevention": [
            "Maintain low humidity (<85%)",
            "Use resistant varieties",
            "Adequate plant spacing",
            "Good greenhouse ventilation"
        ],
        "cultural_practices": [
            "Remove lower leaves for air flow",
            "Avoid wetting foliage",
            "Prune for better air circulation",
            "Control greenhouse humidity"
        ]
    },
    "Septoria_leaf_spot": {
        "disease_name": "Septoria Leaf Spot",
        "description": "Fungal disease with small circular spots with dark borders",
        "severity": "Medium",
        "treatment": {
            "chemical": "Chlorothalonil or Copper fungicide @ 2g/L",
            "organic": "Neem oil 5ml/L + remove infected leaves",
            "frequency": "Every 7-10 days during wet weather"
        },
        "prevention": [
            "Crop rotation (3 years minimum)",
            "Mulch to prevent soil splash",
            "Space plants properly",
            "Remove plant debris after harvest"
        ],
        "cultural_practices": [
            "Remove lower leaves touching soil",
            "Water at base only",
            "Stake plants off ground",
            "Avoid overhead irrigation"
        ]
    },
    "Target_Spot": {
        "disease_name": "Target Spot",
        "description": "Fungal disease with concentric rings forming target-like patterns",
        "severity": "Medium",
        "treatment": {
            "chemical": "Azoxystrobin @ 1ml/L water",
            "organic": "Copper-based organic fungicide",
            "frequency": "Every 10-14 days"
        },
        "prevention": [
            "Use certified disease-free seeds",
            "Crop rotation",
            "Avoid excess nitrogen fertilizer",
            "Good field sanitation"
        ],
        "cultural_practices": [
            "Prune for air circulation",
            "Remove infected leaves",
            "Mulch soil surface",
            "Drip irrigation preferred"
        ]
    },
    "Tomato_mosaic_virus": {
        "disease_name": "Tomato Mosaic Virus",
        "description": "Viral disease causing mottled light and dark green patterns",
        "severity": "High",
        "treatment": {
            "chemical": "No chemical cure - remove infected plants immediately",
            "organic": "Remove and destroy infected plants",
            "frequency": "Immediate action required"
        },
        "prevention": [
            "Use virus-free certified seeds",
            "Disinfect tools with 10% bleach",
            "Control aphids and whiteflies",
            "Wash hands before handling plants"
        ],
        "cultural_practices": [
            "Remove infected plants completely",
            "Do not smoke near plants",
            "Sterilize stakes and cages",
            "Plant resistant varieties"
        ]
    },
    "Tomato_Yellow_Leaf_Curl_Virus": {
        "disease_name": "Yellow Leaf Curl Virus",
        "description": "Viral disease causing upward leaf curling and yellowing",
        "severity": "Very High",
        "treatment": {
            "chemical": "Insecticides for whitefly control (Imidacloprid)",
            "organic": "Neem oil for whitefly + yellow sticky traps",
            "frequency": "Weekly insecticide rotation"
        },
        "prevention": [
            "Use resistant varieties (highly recommended)",
            "Install insect-proof nets",
            "Control whitefly population",
            "Remove infected plants immediately"
        ],
        "cultural_practices": [
            "Use reflective mulch",
            "Plant marigold as trap crop",
            "Monitor for whiteflies daily",
            "Maintain weed-free surroundings"
        ]
    },
    "Two_spotted_spider_mite": {
        "disease_name": "Two-Spotted Spider Mite",
        "description": "Pest causing yellow stippling and fine webbing on leaves",
        "severity": "Medium",
        "treatment": {
            "chemical": "Abamectin @ 0.5ml/L water",
            "organic": "Neem oil spray + predatory mites release",
            "frequency": "Every 5-7 days, rotate chemicals"
        },
        "prevention": [
            "Maintain adequate moisture",
            "Avoid water stress",
            "Encourage beneficial insects",
            "Regular monitoring"
        ],
        "cultural_practices": [
            "Spray water on leaf undersides",
            "Avoid dusty conditions",
            "Remove heavily infested leaves",
            "Maintain humidity >50%"
        ]
    },
    "healthy": {
        "disease_name": "Healthy Plant",
        "description": "No disease detected - plant appears healthy",
        "severity": "None",
        "treatment": {
            "chemical": "No treatment needed",
            "organic": "Continue regular care",
            "frequency": "N/A"
        },
        "prevention": [
            "Maintain good cultural practices",
            "Regular monitoring for early disease detection",
            "Balanced nutrition",
            "Proper watering schedule"
        ],
        "cultural_practices": [
            "Continue regular watering and fertilization",
            "Monitor for any changes",
            "Maintain plant hygiene",
            "Ensure adequate spacing"
        ]
    }
}
