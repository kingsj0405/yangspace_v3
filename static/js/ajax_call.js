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