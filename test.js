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
const patientData = {'ID': 0, 
    'name': 'Erika', 
    'age': 0, 
    'recent_changes_in_health_yn': true, 
    'pre-existing_conditions': ['string'], 
    'medications': true, 
    'any_allergies_yn': true, 
}

// Call the function with the patient data
createPatient(patientData);
