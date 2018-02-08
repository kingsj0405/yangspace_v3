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
            // Change control panel href
            $('div.control-panel a:nth-child(2)').attr('href', data.create_url);
            $('div.control-panel a:nth-child(3)').attr('href', data.update_url);
            $('div.control-panel a:nth-child(4)').attr('href', data.delete_url);
            $('div.control-panel a:nth-child(5)').attr('href', data.history_url);
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