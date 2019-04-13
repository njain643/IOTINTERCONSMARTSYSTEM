(function($)
{
    $(document).ready(function()
    {
        var $container = $("#circle");
       $container.load("http://localhost:8000/");
        var refreshId = setInterval(function()
        {
            $container.load('http://localhost:8000/');
        }, 9000);
    });
 })(jQuery);