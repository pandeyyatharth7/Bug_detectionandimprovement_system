// script.js
const codeInput = document.getElementById('code-input');
const outputBox = document.getElementById('output-box');

// Simulate real-time analysis as the user types
codeInput.addEventListener('input', () => {
  const code = codeInput.value;

  // Simulate analysis (replace with actual backend call)
  if (code.trim() === "") {
    outputBox.innerHTML = ""; // Clear output if no code is entered
  } else {
    outputBox.innerHTML = `
      <p><strong>Analysis Results:</strong></p>
      <p>1. No syntax errors found.</p>
      <p>2. Potential performance improvement in line 10.</p>
      <p>3. Consider adding comments for better readability.</p>
    `;
  }
});

document.getElementById('thumbs-up').addEventListener('click', () => {
  alert('Thank you for your feedback! 👍');
});

document.getElementById('thumbs-down').addEventListener('click', () => {
  alert('Thank you for your feedback! 👎');
});

document.getElementById('regenerate-button').addEventListener('click', () => {
  const code = codeInput.value;
  outputBox.innerHTML = `<p>Regenerating analysis...</p>`;

  // Simulate regeneration (replace with actual backend call)
  setTimeout(() => {
    outputBox.innerHTML = `
      <p><strong>Regenerated Analysis Results:</strong></p>
      <p>1. No syntax errors found.</p>
      <p>2. Consider using list comprehension in line 15.</p>
    `;
  }, 2000);
});