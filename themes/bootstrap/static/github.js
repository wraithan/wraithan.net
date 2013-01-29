$(function() {
    $.ajax({
        url: 'https://api.github.com/users/wraithan/events?callback=events',
        dataType: 'jsonp',
        success: function(data) {
            var githubList = $('#github-list')
            var count = 0
            console.log(data)
            data.data.forEach(function(element, index){
                if(count < 10) {
                    if (element.type === 'PushEvent') {
                        githubList.append(
                            $('<li>').append($('<a>')
                                             .attr({
                                                 href: element.repo.url
                                             })
                                             .text(element.repo.name)))
                        count++
                    }
                }
            })
        }
    })
})
