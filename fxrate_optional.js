// FXRatesService.js


class FXRatesService {
    constructor() {
        // Mock data representing FX rates for different currencies
        this.fxRates = {
            'USD': {
                '2024-09-25': {
                    'EUR': 0.85,
                    'JPY': 110.53,
                    'GBP': 0.75,
                    'AUD': 1.36,
                    'CAD': 1.25,
                    'INR': 74.57,
                    'CNY': 6.45,
                    'BRL': 5.25,
                    'ZAR': 14.35,
                    'SGD': 1.35,
                },
                // Add other dates as needed
            },
            // Add other base currencies with their rates
        };
    }


    // Method to get FX rates based on the base currency and date
    getRates(baseCurrency, date) {
        const rates = this.fxRates[baseCurrency] && this.fxRates[baseCurrency][date];
        if (!rates) {
            throw new Error('Rates not available for the specified base currency and date.');
        }
        return rates;
    }
}


// Main app logic
const fxService = new FXRatesService();


document.getElementById('fetch-rates').addEventListener('click', () => {
    const baseCurrency = document.getElementById('base-currency').value;
    const date = document.getElementById('date-picker').value; // Get date from date picker


    if (!date) {
        alert('Please select a date.');
        return;
    }


    try {
        const rates = fxService.getRates(baseCurrency, date);
        displayRates(baseCurrency, rates);
    } catch (error) {
        document.getElementById('rates-display').innerHTML = `<p>${error.message}</p>`;
    }
});


// Function to display the rates
function displayRates(baseCurrency, rates) {
    const ratesDisplay = document.getElementById('rates-display');
    ratesDisplay.innerHTML = `<h2>Exchange Rates for ${baseCurrency}</h2>`;
    for (const [currency, rate] of Object.entries(rates)) {
        ratesDisplay.innerHTML += `<p>${currency}: ${rate}</p>`;
    }
}
