(function () {
    'use strict';
    document.querySelectorAll('[data-catalog-filter]').forEach(function (catalog) {
        var form = catalog.querySelector('form');
        var models = Array.from(catalog.querySelectorAll('[data-model]'));
        var count = catalog.querySelector('.nk-filter-count');
        var empty = catalog.querySelector('.nk-filter-empty');
        var area = form.elements.area;
        function update() {
            var rooms = Array.from(form.querySelectorAll('[name="rooms"]:checked')).map(function (input) { return input.value; });
            var spaces = Array.from(form.querySelectorAll('[name="spaces"]:checked')).map(function (input) { return input.value; });
            var shown = 0;
            models.forEach(function (model) {
                var match = (!rooms.length || rooms.includes(model.dataset.rooms)) &&
                    (!spaces.length || spaces.includes(model.dataset.spaces)) &&
                    Number(model.dataset.area) <= Number(area.value);
                model.hidden = !match;
                if (match) shown++;
            });
            catalog.querySelector('[data-area-output]').textContent = area.value + ' m²';
            count.textContent = 'Prikazano ' + shown + ' od ' + models.length + ' modela';
            empty.hidden = shown !== 0;
        }
        form.addEventListener('submit', function (event) { event.preventDefault(); });
        form.addEventListener('input', update);
        form.addEventListener('reset', function (event) {
            event.preventDefault();
            form.querySelectorAll('input[type="checkbox"]').forEach(function (input) { input.checked = false; });
            area.value = area.defaultValue;
            update();
        });
        catalog.querySelector('[data-reset-filters]').addEventListener('click', function () { form.reset(); });
        update();
    });
})();
