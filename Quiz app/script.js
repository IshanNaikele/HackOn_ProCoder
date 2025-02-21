 // Initialize Map
let map = L.map('map').setView([20, 0], 2); // Center at World View

// Load map tiles (Free OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Country data
let countries = {
    "France": [48.8566, 2.3522],  // Paris
    "India": [28.6139, 77.2090],  // New Delhi
    "USA": [38.9072, -77.0369],   // Washington, D.C.
    "Brazil": [-15.8267, -47.9218], // Brasília
    "Japan": [35.6895, 139.6917]   // Tokyo
};

// Pick a random country for the quiz
let countryNames = Object.keys(countries);
let correctCountry = countryNames[Math.floor(Math.random() * countryNames.length)];

// Update question
document.getElementById('question').innerText = `Where is ${correctCountry}?`;

// Add clickable country markers
Object.entries(countries).forEach(([country, coords]) => {
    let marker = L.marker(coords).addTo(map).bindPopup(country);
    
    marker.on('click', function () {
        if (country === correctCountry) {
            alert("✅ Correct! Well done.");
            location.reload(); // Reload to get a new question
        } else {
            alert("❌ Wrong! Try again.");
        }
    });
});
