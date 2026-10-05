document.getElementById('searchBtn').addEventListener('click', doSearch);

if (!document.cookie.includes('session')) {
  document.cookie = "session=SECRET123";
}

window.onload = function () {
  const params = new URLSearchParams(location.hash.slice(1));
  const term = params.get('q');
  if (term) {
    document.getElementById('searchBox').value = term;
    renderResults(term);
  }
};

function doSearch() {
  const term = document.getElementById('searchBox').value;
  location.hash = 'q=' + encodeURIComponent(term);
  renderResults(term);
}

// fixed: use textContent instead of innerHTML so the browser
// never treats the search term as HTML
function renderResults(term) {
  const resultsEl = document.getElementById('results');
  resultsEl.innerHTML = "";

  const heading = document.createElement('p');
  heading.textContent = "Showing results for: " + term;
  resultsEl.appendChild(heading);

  const count = document.createElement('p');
  count.textContent = "0 products found.";
  resultsEl.appendChild(count);
}