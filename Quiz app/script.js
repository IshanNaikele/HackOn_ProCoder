 // Initialize Map
let map = L.map('map').setView([20, 0], 2);

// Load map tiles (Free OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{y}/{x}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Country data variable
let countries = {};
let remainingCountries = [];
let correctCountry = "";

// Fetch country data from JSON
$.getJSON("quiz_data.json", function(data) {
    // Map the country data to countries object
    countries = {};
    data.forEach(item => {
        // You might want to include coordinates for each country here
        // Example: countries["Country Name"] = [latitude, longitude]
        // For now, just creating an empty object
        countries[item.country_name] = item.coordinates; // Assuming you add coordinates in JSON
    });

    // Initialize remaining countries
    remainingCountries = Object.keys(countries);
    generateQuestion();
});

// Generate the first question
function generateQuestion() {
    if (remainingCountries.length === 0) {
        document.getElementById('question').innerText = "🎉 Quiz Completed!";
        return;
    }

    // Pick a random country from remaining
    let index = Math.floor(Math.random() * remainingCountries.length);
    correctCountry = remainingCountries[index];  // Correct country to answer
    document.getElementById('question').innerText = `Where is ${correctCountry}?`;
}

// Handle clicks
Object.entries(countries).forEach(([country, coords]) => {
    let marker = L.marker(coords).addTo(map).bindPopup(country);

    marker.on('click', function () {
        if (country === correctCountry) {
            alert("✅ Correct! Well done.");
            // Remove the correct country from the remaining questions
            remainingCountries.splice(remainingCountries.indexOf(correctCountry), 1);
            setTimeout(generateQuestion, 1000); // Ask a new question after a short delay
        } else {
            alert("❌ Wrong! Try again.");
        }
    });
});
