// async function createPatient(patientData) {
//         const url = 'http://localhost:8000'; // Adjust the URL based on where your API is hosted

//         try {
//             const response = await fetch(url, {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify(patientData)
//             });

//             if (response.ok) {
//                 const jsonResponse = await response.json();
//                 console.log('Patient created:', jsonResponse);
//                 return jsonResponse;
//             } else {
//                 console.error('Failed to create patient. Status:', response.status);
//             }
//         } catch (error) {
//             console.error('Error creating patient:', error);
//         }
//     }

    // Example patient data
    const testPatient = {
        "ID": 30,
        "name": "Armin E. Arlert",
        "age": 25,
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

// // Call the function with the patient data
// createPatient(testPatient);

// go to home page
async function fetchRoot() {
    const url = 'http://localhost:8000'; // URL pointing to the root route

    try {
        const response = await fetch(url, {
            method: 'GET', // Use GET to retrieve data
        });

        if (response.ok) {
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.includes('application/json')) {
                const jsonResponse = await response.json();
                console.log('Received JSON:', jsonResponse);
            } else {
                const textResponse = await response.text();
                console.log('Received HTML/text:', textResponse);
            }
        } else {
            console.error('Failed to fetch from root. Status:', response.status);
        }
    } catch (error) {
        console.error('Error fetching from root:', error);
    }
}

// get a patient

async function fetchPatient(id) {
    const url = `http://localhost:8000/api/patient/${id}`; // URL pointing to the patient route

    try {
        const response = await fetch(url, {
            method: 'GET', // Use GET to retrieve data
        });

        if (response.ok) {
            const jsonResponse = await response.json();
            console.log('Patient:', jsonResponse);
        } else {
            console.error('Failed to fetch patient. Status:', response.status);
        }
    } catch (error) {
        console.error('Error fetching patient:', error);
    }
}

// Call the function to initiate the fetch request
//fetchPatient(101);


// create patient
async function createChat(patientData) {
    const url = 'http://localhost:8000/api/chat'; // URL pointing to the patient route

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
        } else {
            console.error('Failed to create patient. Status:', response.status);
        }
    } catch (error) {
        console.error('Error creating patient:', error);
    }
}

testchat = {
    "ID": 101,
    "prompt": "I am feeling better today"
}

createChat(testchat);

// FOR SURE problem with CORS
//node test.js does not need to use CORS because it is not a request from the browser

// the server.js file does need to use CORS to allow the request to go through
// the fetch request from the browser does need to use CORS to allow the request to go through

// request from browser does need to use CORS to allow the request to go through 