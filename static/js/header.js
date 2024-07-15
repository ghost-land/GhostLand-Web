function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
}

// Language selector functionality
document.addEventListener('DOMContentLoaded', function() {
    const langSelector = document.getElementById('lang-select')
    if (langSelector) {
        // Set default value to langSelector using URL
        const currentPath = window.location.pathname
        const langCode = currentPath.split('/')[1]
        if (langCode && langCode.length == 2) {
            langSelector.value = langCode
        }

        langSelector.addEventListener('change', function() {
            const selectedLang = this.value
            console.log('Selected language:' + selectedLang);
            if (langCode && langCode.length == 2) {
                window.location.href = '/' + selectedLang + '/' + window.location.pathname.slice(3)
            } else {
                window.location.href = '/' + selectedLang + '/' + window.location.pathname
            }
        })
    }
})
