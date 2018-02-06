function init() {
    showdown.setFlavor('github');
}

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

    window.onpopstate = function (e) {
        if (e.state) {
            select_page(e.state.title);
            $('.page-title').html(e.state.title);
            $('.page-content').convert_and_fill(e.state.content);
            document.title = e.state.browser_title;
        }
    }
});