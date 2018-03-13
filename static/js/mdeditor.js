function init_editor() {
    var simplemde = new SimpleMDE({ element: $('#content')[0] });
}

$(document).ready(function () {
    init_editor();
});
