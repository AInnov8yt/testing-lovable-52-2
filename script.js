document.getElementById("fetchBtn").addEventListener("click", function(){
  fetch('/api/data')
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").innerText = data.message;
    })
    .catch(error => console.error('Error fetching data:', error));
});