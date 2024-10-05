document.getElementById('price-form').addEventListener('submit', function (e) {
  e.preventDefault(); // Prevent the default form submission

  // Collect form values
  const area = document.getElementById('area').value;
  const bedrooms = document.getElementById('bedrooms').value;
  const bathrooms = document.getElementById('bathrooms').value;
  const stories = document.getElementById('stories').value;
  const parking = document.getElementById('parking').value;

  // Prepare the data object to be sent in the request body
  const data = {
    area: parseFloat(area),        // Convert to float
    bedrooms: parseInt(bedrooms),  // Convert to integer
    bathrooms: parseInt(bathrooms),
    stories: parseInt(stories),
    parking: parseInt(parking)
  };
  console.log('Sending data:', data);
  // Send POST request to Flask backend
  fetch('http://127.0.0.1:5000/predict', {  // URL of your Flask server
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',  // Ensure JSON format
    },
    body: JSON.stringify(data),  // Send the data as JSON
  })
    .then(response => response.json())  // Parse JSON response
    .then(result => {
      // Update the DOM with the predicted price
      if (result.prediction) {
        document.getElementById('predicted-price').textContent = result.prediction.toFixed(2);
      } else {
        document.getElementById('predicted-price').textContent = 'Error in prediction';
      }
    })
    .catch(error => {
      console.error('Error:', error);  // Log errors if any
      document.getElementById('predicted-price').textContent = 'Prediction failed';
    });
});
