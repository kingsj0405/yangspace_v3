// Markdown Editor
var editor_id = 'content',
    viewer_id = 'content-viewer';
var $editor, $viewer;

function init_editor() {
    // Initialize variables
    $editor = $('#' + editor_id);
    $('#content').after("<div id='" + viewer_id + "' tabindex='1'></div>");
    $viewer = $('#' + viewer_id);
    $viewer.hide();

    // Initialize content
    showdown.setFlavor('github');

    // Add event function
    $editor.keydown(render_viewer);
    $viewer.keydown(render_editor);
    $viewer.focusout(function () {
        $(this).focus();
    })
}

function render_viewer(e) {
    if (e.ctrlKey && e.keyCode === 13) {
        // Ctrl-Enter
        var text = $editor.val(),
            converter = new showdown.Converter(),
            html = converter.makeHtml(text);
        $viewer.html(html);
        $editor.hide();
        $viewer.show();
        $viewer.focus();
    }
}

function render_editor(e) {
    if (e.keyCode === 27) {
        // ESC
        $viewer.hide();
        $editor.show();
        $editor.focus();
    }
}

$(document).ready(function () {
    init_editor();
});
