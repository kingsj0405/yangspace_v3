// Global Function
(function ($) {
    $.fn.convert_and_fill = function (markdown_text) {
        var converter = new showdown.Converter(),
            text = markdown_text,
            html = converter.makeHtml(text);
        this.html(html);
        return this;
    };
})(jQuery);

// Page ajax
function init() {
    showdown.setFlavor('github');

    window.onpopstate = function (e) {
        if (e.state) {
            select_page(e.state.title);
            $('.page-title').html(e.state.title);
            $('.page-content').convert_and_fill(e.state.content);
            document.title = e.state.browser_title;
        }
    }
}

$(document).ready(function () {
    init();
});