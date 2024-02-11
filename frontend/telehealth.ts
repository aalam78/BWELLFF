class TelehealthComponent {
     testPeople = [
        "test1",
        "test2"
    ]
    constructor() {
        this.testPeople = ["test1", "test2"];
    }

    
    ngOnInit() {
        // Initialization logic here
        function search() {
            fetch('/people')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('welcomeMessage').innerHTML = JSON.stringify(data, null, 2);
                     console.log(data); // Array of people
                });

           
                    
            }
        }
    }

// Usage
const telehealthComponent = new TelehealthComponent();
telehealthComponent.ngOnInit(); 