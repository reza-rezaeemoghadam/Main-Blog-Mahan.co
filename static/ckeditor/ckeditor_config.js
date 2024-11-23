function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.ckeditor').forEach((editorElement) => {
        ClassicEditor
            .create(editorElement, {
                simpleUpload: {
                    uploadUrl: '/ckeditor5/upload/',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                }
            })
            .catch(error => {
                console.error(error);
            });
    });
});
