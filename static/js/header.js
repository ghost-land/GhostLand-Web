function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
}

// Language selector functionality
document.addEventListener('DOMContentLoaded', function() {
    const langSelector = document.getElementById('lang-select')
    if (langSelector) {
        // Set default value to langSelector using URL parameter
        const urlParams = new URLSearchParams(window.location.search)
        const langCode = urlParams.get('lang')
        if (langCode && langCode.length === 2) {
            langSelector.value = langCode
        }

        langSelector.addEventListener('change', function() {
            const selectedLang = this.value
            console.log('Selected language:' + selectedLang);
            const currentUrl = new URL(window.location.href);
            if (selectedLang !== 'en') {
                currentUrl.searchParams.set('lang', selectedLang);
            } else {
                currentUrl.searchParams.delete('lang');
            }
            window.location.href = currentUrl.toString();
        })
    }
})
