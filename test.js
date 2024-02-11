async function testPatientSend() {
    async function createPatient(patientData) {
        const url = 'http://localhost:8000/api/patient'; // Adjust the URL based on where your API is hosted

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(patientData)
            });

            if (response.ok) {
                const jsonResponse = await response.json();
                console.log('Patient created:', jsonResponse);
                return jsonResponse;
            } else {
                console.error('Failed to create patient. Status:', response.status);
            }
        } catch (error) {
            console.error('Error creating patient:', error);
        }
    }

    // Example patient data
    const testPatient = {
        "ID": 101,
        "name": "Jane Doe",
        "age": 28,
        "recent_changes_in_health_yn": true,
        "pre-existing_conditions": [
            "Asthma"
        ],
        "medications": [
            {
                "name": "Albuterol",
                "dosage": "2 puffs every 4 hours as needed",
                "reason_for_taking": "Prevent asthma symptoms"
            }
        ],
        "any_allergies_yn": true,
        "allergies": [
            {
                "substance": "Peanuts",
                "reaction": "Anaphylaxis"
            }
        ],
        "symptoms": [
            {
                "symptom": "Shortness of breath",
                "duration": "3 days",
                "severity": "Moderate",
                "how_it_affects_daily_life": "Difficulty performing physical activities"
            },
            {
                "symptom": "Wheezing",
                "duration": "2 days",
                "severity": "Mild",
                "how_it_affects_daily_life": "Some discomfort during the night"
            }
        ],
        "lifestyle_factors": {
            "diet": "Vegetarian, high in fruits and vegetables",
            "exercise": "Jogging 30 minutes daily",
            "stress_level": "Moderate, due to work deadlines",
            "sleep_quality": "Good, approximately 7-8 hours nightly"
        },
        "recent_travel_history": "No recent travel",
        "recent_exposure_to_sick_individuals": "No known exposure",
        "family_history_of_illnesses": "Father has type 2 diabetes, mother has hypertension",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "zip": "12345"
        },
        "contact": {
            "phone": "555-123-4567",
            "email": "janedoe@example.com"
        },
        "emergency_contact": {
            "name": "John Doe",
            "relationship": "Brother",
            "phone": "555-987-6543",
            "email": "johndoe@example.com"
        },
        
        "questions": [
            {
                "question": "How often do you experience asthma attacks?",
                "answer": "2-3 times a month",
                "timestamp": "2023-10-05T14:48:00Z"
            },
            {
                "question": "Have you been using your inhaler more frequently lately?",
                "answer": "Yes, especially in the past week",
                "timestamp": "2023-10-06T09:22:00Z"
            }
        ]
    }

// Call the function with the patient data
createPatient(testPatient);

}