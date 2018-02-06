// General
function init() {
    showdown.setFlavor('github');
}

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

// Page ajax
(function ($) {
    $.fn.convert_and_fill = function (markdown_text) {
        var converter = new showdown.Converter(),
            text = markdown_text,
            html = converter.makeHtml(text);
        this.html(html);
        return this;
    };
})(jQuery);

function select_page(page_title) {
    $('.selected').removeClass('selected');
    $('.list-group-item').each(function () {
        var text = $(this).children('.panel-title').children('.panel-title-content').text();
        if (text === page_title) {
            $(this).addClass('selected');
        }
    });
}

function read_page(page_id) {
    $.ajax({
        url: "/api/v1/page/read/",
        type: "get",
        data: {
            page_id: page_id
        },
        success: function (result) {
            var data = result.content;
            // Change content
            select_page(data.title);
            $('.page-title').html(data.title);
            $('.page-content').convert_and_fill(data.content);
            // Change browser title and url
            document.title = data.browser_title;
            window.history.pushState({
                'title': data.title,
                'content': data.content,
                'browser_title': data.browser_title,
            }, data.browser_title, data.browser_url);
        }
    });
}

$(document).ready(function () {
    init();
    init_editor();

    window.onpopstate = function (e) {
        if (e.state) {
            select_page(e.state.title);
            $('.page-title').html(e.state.title);
            $('.page-content').convert_and_fill(e.state.content);
            document.title = e.state.browser_title;
        }
    }
});