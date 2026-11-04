(function () {
    "use strict";

    var sendTo = "AW-18290116215/hZcbCJT8nOQcEPeMtJFE";

    document.addEventListener("click", function (event) {
        var target = event.target;
        if (!(target instanceof Element)) {
            return;
        }

        var phoneLink = target.closest('a[href^="tel:"]');
        if (!phoneLink || typeof window.gtag !== "function") {
            return;
        }

        event.preventDefault();

        var destination = phoneLink.href;
        var hasNavigated = false;
        var openDialer = function () {
            if (hasNavigated) {
                return;
            }
            hasNavigated = true;
            window.location.href = destination;
        };

        window.gtag("event", "conversion", {
            send_to: sendTo,
            event_callback: openDialer,
            event_timeout: 1000
        });

        window.setTimeout(openDialer, 1000);
    }, true);
})();
