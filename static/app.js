document.getElementById('fetch-trends').addEventListener('click', () => {
    // Clear previous results
    document.getElementById('trends-list').innerHTML = '';
    document.getElementById('ip-info').innerText = '';

    // Trigger the backend script
    fetch('/scrape-trends')
        .then(response => response.json())
        .then(data => {
            // Display trends
            const trendsList = document.getElementById('trends-list');
            data.trends.forEach(trend => {
                const listItem = document.createElement('li');
                listItem.textContent = trend;
                trendsList.appendChild(listItem);
            });

            // Display IP address
            document.getElementById('ip-info').textContent = `IP Address: ${data.ip_address}`;

            // Visualize data with Chart.js
            const ctx = document.getElementById('trends-chart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.trends,
                    datasets: [{
                        label: 'Trending Topics',
                        data: data.trends.map((_, index) => index + 1),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error fetching trends:', error);
        });
});
