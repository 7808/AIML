document.getElementById('generateButton').addEventListener('click', () => {
    const codeSnippet = document.getElementById('codeSnippet').value;
    fetch('http://localhost:5000/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ code: codeSnippet })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('output').innerText = data.test_cases;
    })
    .catch(error => console.error('Error:', error));
  });
  