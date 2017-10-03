tinymce.init({
    selector: "textarea",
    theme: "modern",
    language: "zh_CN",
    plugins: [
        "advlist autolink lists link image charmap print preview hr anchor pagebreak",
        "searchreplace wordcount visualblocks visualchars code fullscreen",
        "insertdatetime media nonbreaking save table contextmenu directionality",
        "emoticons template paste textcolor codesample"
    ],
    toolbar1: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
    toolbar2: "print preview media | forecolor backcolor emoticons codesample",
    image_advtab: true,
    templates: [
        {title: 'Test template 1', content: 'Test 1'},
        {title: 'Test template 2', content: 'Test 2'}
    ],
    codesample_languages: [
        {text: 'HTML/XML', value: 'markup'},
        {text: 'JavaScript', value: 'javascript'},
        {text: 'CSS', value: 'css'},
        {text: 'PHP', value: 'php'},
        {text: 'Ruby', value: 'ruby'},
        {text: 'Python', value: 'python'},
        {text: 'Java', value: 'java'},
        {text: 'C', value: 'c'},
        {text: 'C#', value: 'csharp'},
        {text: 'C++', value: 'cpp'}
    ],
    paste_data_images:true,
    file_browser_callback: function(field_name, url, type, win) {
            if(type=='image') $('#my_form input').click();
        }
});
$( document ).ready(function() {
    h ='<iframe id="form_target" name="form_target" style="display:none"></iframe><form id="my_form" action="/temporary/uploadIMG/" target="form_target" method="post" enctype="multipart/form-data" style="width:0px;height:0;overflow:hidden"><input name="img" type="file" onchange="$(\'#my_form\').submit();this.value=\'\';"></form>';
    $('body').append(h);
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
    var csrftoken = getCookie('csrftoken');
        console.log(csrftoken);
        $('#my_form').append('<input type="hidden" name="csrfmiddlewaretoken" value='+csrftoken+' />');


});

// tinymce.init({
//     selector: "textarea",
//     theme : "modern",
//     // width: '700',
//     // height: '400'
// });

// tinymce.init({
//     selector: 'textarea',
//     theme : "modern",
//     plugins: ["image"],
//     image_advtab: true,
//     paste_data_images:true,
//     file_browser_callback: function(field_name, url, type, win) {
//         if(type=='image') $('#my_form input').click();
//     },
// });
// $( document ).ready(function() {
//     h ='<iframe id="form_target" name="form_target" style="display:none"></iframe><form id="my_form" action="/temporary/uploadIMG/" target="form_target" method="post" enctype="multipart/form-data" style="width:0px;height:0;overflow:hidden"><input name="img" type="file" onchange="$(\'#my_form\').submit();this.value=\'\';"></form>';
//     $('body').append(h);
//     function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
//   }
//     var csrftoken = getCookie('csrftoken');
//         console.log(csrftoken);
//         $('#my_form').append('<input type="hidden" name="csrfmiddlewaretoken" value='+csrftoken+' />');
// });