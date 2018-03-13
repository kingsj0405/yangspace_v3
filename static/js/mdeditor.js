var editor_id = 'content';

function init_editor() {
    var simplemde = new SimpleMDE({ element: $('#' + editor_id)[0] });
}

$(document).ready(function () {
    init_editor();
});
