function init_tree() {
    $('.glyphicon-chevron-right, .glyphicon-chevron-down').on('click', function () {
        $(this)
            .toggleClass('glyphicon-chevron-right')
            .toggleClass('glyphicon-chevron-down');
    });
}

function select_page(page_title) {
    $('.selected').removeClass('selected');
    $('.list-group-item').each(function () {
        var text = $(this).children('.panel-title').children('.panel-title-content').text();
        if (text === page_title) {
            $(this).addClass('selected');
            $(this).parents('.collapse').each(function () {
                $(this).collapse("show");
                $(this).prev().find('.glyphicon-chevron-right').each(function () {
                    console.log("test2");
                    $(this)
                        .removeClass('glyphicon-chevron-right')
                        .addClass('glyphicon-chevron-down');
                });
            });
        }
    });
}

$(document).ready(function () {
    init_tree();
});